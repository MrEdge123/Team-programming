#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ptrace.h>
#include <sys/resource.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

//基本单位
#define UNIT_KB 1024
#define UNIT_MB 1048576

//语言
#define LANG_C 1
#define LANG_CPP 2
#define LANG_PY3 3
#define LANG_JAVA 4 //未完成

//评测状态
#define STATUS_AC 1
#define STATUS_WA 2
#define STATUS_CE 3
#define STATUS_RE 4
#define STATUS_TE 5
#define STATUS_ME 6

//基础内存
#define MEM_C 4416
#define MEM_CPP 13900
#define MEM_PY3 30000

//文本对比模式
#define IGNORE_NOT 0
#define IGNORE_SPACE 1
#define IGNORE_LINE 2
#define IGNORE_ALL_EMPTY 3
#define IGNORE_CASE 4

const char *STATUS[10] = {"", "AC", "WA", "CE", "RE", "TE", "ME"};

int result = STATUS_AC;
long long timeUsed = 0;
long long memoryUsed = 0;

/*
文件:
数据: input.txt, answer.txt
运行输出: output.txt
错误信息: error.txt
结果信息: result.json

result.json的内容:
例子:
{
    "result":"AC"
    "timeUsed":0
    "memoryUsed":0
}

具体信息:
"result": 评测结果, 可能的值:
    "AC": 答案正确
    "WA": 答案错误
    "CE": 编译错误
    "RE": 运行错误
    "TE": 时间超限
    "ME": 内存超限

"timeUsed": 运行的时间, 值为整数, 单位为毫秒(ms)
"memoryUsed": 使用的内存, 值为整数, 单位为KB

日志: log.txt

命令行参数:
-path: 程序执行路径
-mode: cp:编译, run:运行
-lang: C, C++, Python3
-tl: 1000 (单位:ms)
-ml: 1024 (单位:KB)
-check:
    ignore-not: 什么都不忽略
    ignore-space: 忽略空格字符
    ignore-line: 忽略空白行
    ignore-empty: 忽略所有空白字符
    ignore-case: 忽略大小写
*/

//写日志
void write_log(const char *format, ...) {
    va_list arg;

    FILE *fp = fopen("log.txt", "a+");
    char buf[UNIT_KB];

    va_start(arg, format);
    vsprintf(buf, format, arg);
    va_end(arg);

    fprintf(fp, buf, NULL);
    fclose(fp);
}

//写错误
void write_error(const char *s) {
    FILE *fp = fopen("error.txt", "a+");
    fprintf(fp, s, NULL);
    fclose(fp);
}

//编译
void complile(int lang) {
    int pid = fork();

    if (pid == 0) {
        freopen("error.txt", "w", stderr);
        if (lang == LANG_PY3)
            return; // Python不需要编译

        switch (lang) {
        case LANG_C:
            execlp("gcc", "gcc", "Main.c", "-o", "Main", "-O2", NULL);
            break;
        case LANG_CPP:
            execlp("g++", "g++", "Main.cpp", "-o", "Main", "-O2", NULL);
            break;
        default:
            break;
        }
    } else {
        waitpid(-1, NULL, 0);
        int ok = system("grep -i \"error\" error.txt");
        if (ok == 0)
            result = STATUS_CE;
    }
}

//跑程序
void run(int lang, long long timeLimit, long long memoryLimit) {
    //设置被跟踪
    ptrace(PTRACE_TRACEME, 0, NULL, NULL);

    struct rlimit LIM;

    //设置时间限制
    LIM.rlim_cur = timeLimit / 1.0 / 1000;
    LIM.rlim_max = LIM.rlim_cur;
    if (setrlimit(RLIMIT_CPU, &LIM))
        write_log("set cpu limit failed!\n");

    //设置栈空间限制
    LIM.rlim_cur = 128 * UNIT_MB;
    LIM.rlim_max = LIM.rlim_cur;
    if (setrlimit(RLIMIT_STACK, &LIM))
        write_log("set stack limit failed\n");

    //设置程序运行空间限制
    LIM.rlim_cur = memoryLimit * UNIT_KB + 10 * UNIT_MB;
    LIM.rlim_max = LIM.rlim_cur;
    if (setrlimit(RLIMIT_AS, &LIM))
        write_log("set memory limit failed\n");

    //重定向
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    freopen("error.txt", "a+", stderr);

    write_log("ready to run program\n");

    //运行程序
    switch (lang) {
    case LANG_C:
        execl("./Main", "./Main", NULL);
        break;
    case LANG_CPP:
        execl("./Main", "./Main", NULL);
        break;
    case LANG_PY3:
        execlp("python3", "python3", "Main.py", NULL);
        break;
    default:
        break;
    }

    fflush(stdout);

    write_log("end run program\n");
}

//获得进程使用空间
long long get_memory_used(pid_t pid) {
    long long ans = 0;

    char path[UNIT_KB] = "";
    char buf[UNIT_KB] = "";

    sprintf(path, "/proc/%d/status", pid);
    FILE *fp = fopen(path, "r");

    int len = strlen("VmPeak:");

    while (fp && fgets(buf, UNIT_KB, fp)) {
        // write_log("memory log:%s", buf);
        if (strncmp(buf, "VmPeak:", len) == 0) {
            sscanf(buf + len + 1, "%lld", &ans);
        }
    }

    if (fp)
        fclose(fp);

    return ans;
}

//监测程序
void monitor(pid_t pidRunning, int lang, long long timeLimit,
             long long memoryLimit) {
    int runStatus, sig, exitCode;
    struct rusage resouceUsed;

    long long tempMemoryUsed = 0;

    while (1) {
        wait4(pidRunning, &runStatus, 0, &resouceUsed);

        //监控内存使用
        if (lang == LANG_JAVA) {
            tempMemoryUsed = resouceUsed.ru_minflt * getpagesize() / UNIT_KB;
        } else {
            tempMemoryUsed = get_memory_used(pidRunning);
        }

        if (tempMemoryUsed > memoryUsed)
            memoryUsed = tempMemoryUsed;

        if (memoryUsed > memoryLimit) {
            memoryUsed = memoryLimit;
            if (result == STATUS_AC)
                result = STATUS_ME;
            write_log("out of memoryLimit\n");
            ptrace(PTRACE_KILL, pidRunning, NULL, NULL);
            break;
        }

        //程序正常退出
        if (WIFEXITED(runStatus)) {
            write_log("program exit\n");
            break;
        }

        exitCode = WEXITSTATUS(runStatus);

        // 5: 等待CPU分配
        if (exitCode == 0 || exitCode == 5)
            ;
        else {
            //程序异常
            if (result == STATUS_AC) {
                switch (exitCode) {
                case SIGCHLD:
                case SIGALRM:
                    alarm(0);
                case SIGKILL:
                case SIGXCPU:
                    result = STATUS_TE;
                    break;
                default:
                    result = STATUS_RE;
                }
            }
            ptrace(PTRACE_KILL, pidRunning, NULL, NULL);

            if (result == STATUS_RE)
                write_error(strsignal(exitCode));

            break;
        }

        //程序因终止信号结束
        if (WIFSIGNALED(runStatus)) {
            write_log("program error\n");
            sig = WTERMSIG(runStatus);

            if (result == STATUS_AC) {
                switch (sig) {
                case SIGCHLD:
                case SIGALRM:
                    alarm(0);
                case SIGKILL:
                case SIGXCPU:
                    result = STATUS_TE;
                    break;
                default:
                    result = STATUS_RE;
                }
            }
            ptrace(PTRACE_KILL, pidRunning, NULL, NULL);
            break;
        }

        // write_log("running\n");

        ptrace(PTRACE_SYSCALL, pidRunning, NULL, NULL); //回调
    }

    if (result == STATUS_TE) {
        timeUsed = timeLimit;
        return;
    }

    //计算总花费时间
    timeUsed = resouceUsed.ru_utime.tv_sec * 1000 +
               resouceUsed.ru_utime.tv_usec / 1000;
    timeUsed += resouceUsed.ru_stime.tv_sec * 1000 +
                resouceUsed.ru_stime.tv_usec / 1000;
}

//对比结果
bool compare_output(int mode = IGNORE_NOT) {
    //逐行比较: -a
    //忽略空格字符: -b
    //忽略空白行: -B
    //忽略大小写: -i
    //忽略输出信息: -q
    char cmd[1024] = "";
    int pos = 0;

    sprintf(cmd + pos, "diff answer.txt output.txt -a -q");
    pos = strlen(cmd);

    if (mode & IGNORE_SPACE) {
        sprintf(cmd + pos, " -b");
        pos = strlen(cmd);
    }

    if (mode & IGNORE_LINE) {
        sprintf(cmd + pos, " -B");
        pos = strlen(cmd);
    }

    if (mode & IGNORE_CASE) {
        sprintf(cmd + pos, " -i");
        pos = strlen(cmd);
    }

    write_log("compare cmd: %s\n", cmd);

    int ok = system(cmd);
    if (ok == 0)
        return true;
    return false;
}

//回写结果
void write_result() {
    FILE *resultFp = fopen("result.json", "w");
    FILE *errorFp = fopen("error.txt", "r");

    fprintf(resultFp, "{\n");

    fprintf(resultFp, "\t");
    fprintf(resultFp, "\"result\":\"%s\",\n", STATUS[result]);

    fprintf(resultFp, "\t");
    fprintf(resultFp, "\"timeUsed\":%lld,\n", timeUsed);

    fprintf(resultFp, "\t");
    fprintf(resultFp, "\"memoryUsed\":%lld\n", memoryUsed);

    fprintf(resultFp, "}\n");

    fclose(resultFp);
    fclose(errorFp);
}

int main(int argc, char **argv) {
    char path[UNIT_KB];        //工作路径
    int mode = 0;              //运行模式, 1:编译, 2:运行
    int lang = 0;              //语言, 1:C, 2:C++, 3:Python3
    long long timeLimit = 0;   //时间限制
    long long memoryLimit = 0; //空间限制
    int checkMode = 0;         //结果对比模式

    //接收命令行参数
    for (int i = 1; i < argc - 1; i++) {
        if (strcmp(argv[i], "-path") == 0) {
            sprintf(path, "%s", argv[i + 1]);
        }
    }

    if(strlen(path) == 0) return 1;

    chdir(path);

    for (int i = 1; i < argc - 1; i++) {
        if (strcmp(argv[i], "-path") == 0) {
            sprintf(path, "%s", argv[i + 1]);
        }
        if (strcmp(argv[i], "-mode") == 0) {
            if (strcmp(argv[i + 1], "cp") == 0)
                mode = 1;
            else if (strcmp(argv[i + 1], "run") == 0)
                mode = 2;
            else {
                write_log("parameter error!!\n");
                write_log("error:%s\n", argv[i + 1]);
                return 1;
            }

            write_log("mode:%d\n", mode);
        }
        if (strcmp(argv[i], "-lang") == 0) {
            if (strcmp(argv[i + 1], "C") == 0)
                lang = LANG_C;
            else if (strcmp(argv[i + 1], "C++") == 0)
                lang = LANG_CPP;
            else if (strcmp(argv[i + 1], "Python3") == 0)
                lang = LANG_PY3;
            else {
                write_log("parameter error!!\n");
                write_log("error:%s\n", argv[i + 1]);
                return 1;
            }
            write_log("lang:%d\n", lang);
        }
        if (strcmp(argv[i], "-tl") == 0) {
            timeLimit = atoll(argv[i + 1]);
            write_log("timeLimit:%lld\n", timeLimit);
        }
        if (strcmp(argv[i], "-ml") == 0) {
            memoryLimit = atoll(argv[i + 1]);
            write_log("memoryLimit:%lld\n", memoryLimit);
        }
        if (strcmp(argv[i], "-check") == 0) {
            if (strcmp(argv[i + 1], "ignore-not") == 0)
                checkMode = IGNORE_NOT;
            else if (strcmp(argv[i + 1], "ignore-space") == 0)
                checkMode = IGNORE_SPACE;
            else if (strcmp(argv[i + 1], "ignore-line") == 0)
                checkMode = IGNORE_LINE;
            else if (strcmp(argv[i + 1], "ignore-empty") == 0)
                checkMode = IGNORE_ALL_EMPTY;
            else if (strcmp(argv[i + 1], "ignore-case") == 0)
                checkMode = IGNORE_CASE;
            else {
                write_log("parameter error!!\n");
                write_log("error:%s\n", argv[i + 1]);
                return 1;
            }
        }
    }

    write_log("path:%s\n", path);
    write_log("begin core\n");

    if (argc < 3) {
        write_log("parameter error!!\n");
        write_log("argc: %d\n", argc);
        return 1;
    }

    //检查是否合法
    if (mode == 0 || lang == 0) {
        write_log("parameter error!!\n");
        write_log("lack of mode or lang or path\n");
        return 1;
    }
    if (mode == 2 && (timeLimit == 0 || memoryLimit == 0)) {
        write_log("parameter error!!\n");
        write_log("timeLimit:%lld\n", timeLimit);
        write_log("memoryLimit:%lld\n", memoryLimit);
        return 1;
    }

    //修改内存限制
    switch (lang) {
    case LANG_C:
        memoryLimit += MEM_C;
        break;
    case LANG_CPP:
        memoryLimit += MEM_CPP;
        break;
    case LANG_PY3:
        memoryLimit += MEM_PY3;
        break;
    default:
        break;
    }

    if (mode == 1) //编译模式
    {
        write_log("compile mode\n");
        complile(lang);
    } else //运行模式
    {
        write_log("run mode\n");

        int pid = fork();
        if (pid == 0) {
            write_log("run program\n");
            run(lang, timeLimit, memoryLimit);
        } else {
            write_log("monitor program\n");
            monitor(pid, lang, timeLimit, memoryLimit);

            int ok = system("grep \"error\" error.txt -i");
            if (ok == 0)
                result = STATUS_RE;

            if (result == STATUS_AC) {
                write_log("compare output\n");
                if (!compare_output(checkMode))
                    result = STATUS_WA;
            }
        }
    }

    //修改内存使用
    switch (lang) {
    case LANG_C:
        memoryUsed -= MEM_C;
        break;
    case LANG_CPP:
        memoryUsed -= MEM_CPP;
        break;
    case LANG_PY3:
        memoryUsed -= MEM_PY3;
        break;
    default:
        break;
    }
    if (memoryUsed < 0)
        memoryUsed = 0;

    write_result();

    write_log("end core\n");

    return 0;
}
