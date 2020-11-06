import os
import json
import pymysql
import random

# 外部接口部分

'''
void submitCode(userName, problmeId, code, language, submitTime)

1.传入参数
userName: 用户名, 类型为字符串, 用于数据库查询
problemId: 题目编号, 类型为数字, 用于数据库查询
code: 评测代码, 类型为字符串
language: 评测语言, 类型为字符串, 暂时支持的语言有: "C", "C++", "Python3" (注意大小写)
submitTime: 提交时间, 类型为字符串, 格式为: YYYY-MM-DD HH:MM:SS, 例子: "1000-01-01 00:00:00"

'''

def submitCode(userName, problmeId, code, language, submitTime):
    # 创建判题文件夹
    basePath = "/home/OJ/judge"
    
    path_id = random.randint(1, 100000)
    path = basePath + "/" + str(path_id)

    while os.path.exists(path):
        path_id = random.randint(1, 100000)
        path = basePath + "/" + str(path_id)
    
    os.makedirs(path)

    # 连接数据库(待修改)
    db = pymysql.connect("localhost","username","password","dbname")
    cur = db.cursor()

    # 添加判题状态
    sql = '''
    insert into submitStatus(
        problemId, userName, judgeResult,
        usedMemory, usedTime, language,
        submitTime, code
    )
    values (%d, '%s', '%s', %d, %d, '%s', '%s', '%s')
    '''

    try:
        cur.execute(sql, [problmeId, userName, "评测中", 
                            -1, -1, language, 
                            submitTime, code]
                    )
        db.commit()
    except:
        db.rollback()
        cur.close()
        db.close()
        return

    # 判题
    result = judgeProblem(path, problmeId, code, language)

    meaning = {"AC":"通过", "WA":"答案错误", 
                "TE":"运行超时", "ME":"空间超限",
                "CE":"编译错误", "RE":"运行错误"
                }

    # 修改判题状态
    sql = '''
    update submitStatus
    set judgeResult='%s', usedMemory=%d, usedTime=%d
    where submitTime='%s' and userName='%s' and problemId=%d
    '''

    try:
        cur.execute(sql, 
            [meaning[result["result"]], result["usedMemory"], result["usedTime"],
                submitTime, userName, problmeId]
        )
        db.commit()
    except:
        db.rollback()
        cur.close()
        db.close()
        return

    cur.close()
    db.close()

    # 删除判题文件夹
    delList = os.listdir(path)
    for fileName in delList:
        os.remove(path + "/" + fileName)
    
    os.rmdir(path)


# 内部模块部分

'''
文件位置存放:
程序: Main.*
数据: input.txt, answer.txt
运行输出: output.txt
错误信息: error.txt
单次评测结果: result.json

'''

'''
dict judgeProblem(path, problmeId, code, language)

1.传入参数
path: 评测路径, 在改路径会生成评测数据, 类型为字符串
problemId: 题目编号, 类型为数字
code: 评测代码, 类型为字符串
language: 评测语言, 类型为字符串

2.返回参数
字典, key有: "result", "timeUsed", "memoryUsed", "errorMessage"

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
"errorMessege": 运行错误信息, 值为字符串

例子:
{"result":"AC", "timeUsed":30, "memoryUsed":1024, "errorMessage"}

'''

def judgeProblem(path, problemId, code, language):
    # 判题核心位置(待修改)
    if not os.path.exists("judgeCore.cpp"):
        return
    
    os.system("g++ judgeCore.cpp -o {}/core".format(path))

    result = {"result":"AC", "timeUsed":0, "memoryUsed":0, "errorMessage":""}

    # 代码
    if language == "C":
        with open("{}/Main.c".format(path), "w", encoding="utf-8") as codeFile:
            codeFile.write(code)
    elif language == "C++":
        with open("{}/Main.cpp".format(path), "w", encoding="utf-8") as codeFile:
            codeFile.write(code)
    elif language == "Python3":
        with open("{}/Main.py".format(path), "w", encoding="utf-8") as codeFile:
            codeFile.write(code)
    else:
        print("language error!!")
        return

    # 编译
    result = compileCode(path, language)
    if result["result"] == "CE": return result

    '''
    读取数据库, 然后单个数据评测

    数据: input.txt, answer.txt

    runJudge(path, language, timeLimit, memoryLimit, checkMode)

    timeLimit: 时间限制, 单位为毫秒(ms)
    memoryLimit: 空间限制, 单位为KB
    checkMode: 结果对比模式, 类型为字符串
    '''

    # 连接数据库(待修改)
    db = pymysql.connect("localhost","username","password","dbname")
    cur = db.cursor()

    # 获得时间限制和空间限制
    sql = '''
    select timeLimit, memoryLimit
    from problemContent
    where problmeId = %d
    '''

    cur.execute(sql, [problemId])

    line = cur.fetchone()
    timeLimit = line[0]
    memoryLimit = line[1]

    # 获取题目评测数据
    sql = '''
    select inputData, outputData
    from problmeTestData
    where problmeId = %d
    '''

    row = cur.execute(sql, [problemId])
    while row:
        line = cur.fetchone()

        # 写入一组评测数据
        with open("input.txt", "w", encoding="utf-8") as inputFile:
            inputFile.write(line[0])
        with open("answer.txt", "w", encoding="utf-8") as answerFile:
            answerFile.write(line[1])
        
        # 评测一组数据
        tmp_result = runJudge(path, language, timeLimit, memoryLimit)
        if tmp_result["result"] != "AC":
            result = tmp_result
            break

        # 更新状态
        result["timeUsed"] = max(result["timeUsed"], tmp_result["timeUsed"])
        result["memoryUsed"] = max(result["memoryUsed"], tmp_result["memoryUsed"])

        row -= 1
    
    cur.close()
    db.close()

    return result


'''
dict complileCode(language)

1.传入参数
language: 评测语言, 类型为字符串

2.返回参数
字典, key有: "result", "timeUsed", "memoryUsed", "errorMessage"

'''

def compileCode(path, language):
    # 创建文件
    with open("{}/error.txt".format(path), "w", encoding="utf-8") as errorFile:
        pass

    # 运行core
    os.system("{0}/core -mode {1} -lang {2}".format(path, "cp", language))

    # 解析结果
    result_json = ""
    with open("{}/result.json".format(path), "r", encoding="utf-8") as json_file:
        result_json = json_file.read()
    result = json.loads(result_json)

    # 读取错误信息
    with open("{}/error.txt".format(path), "r", encoding="utf-8") as errorFile:
        result["errorMessege"] = errorFile.read()
    
    return result


'''
dict runJudge(path, language, timeLimit, memoryLimit, checkMode)

1.传入参数
language: 评测语言, 类型为字符串
timeLimit: 时间限制, 类型为整数, 单位为毫秒(ms)
memoryLimit: 空间限制, 类型为整数, 单位为KB
checkMode: 结果对比模式, 类型为字符串, 默认: ignore-not

checkMode模式选项:
    ignore-not: 什么都不忽略
    ignore-space: 忽略空格字符
    ignore-line: 忽略空白行
    ignore-empty: 忽略所有空白字符
    ignore-case: 忽略大小写


2.返回参数
字典, key有: "result", "timeUsed", "memoryUsed", "errorMessage"

'''

def runJudge(path, language, timeLimit, memoryLimit, checkMode = "ignore-not"):
    # 创建文件
    with open("{}/error.txt".format(path), "w", encoding="utf-8") as errorFile:
        pass

    # 运行core
    os.system("{0}/core -mode {1} -lang {2} -tl {3} -ml {4} -check {5}".format(
            path, "run", language, timeLimit, memoryLimit, checkMode
        )
    )

    # 解析结果
    result_json = ""
    with open("{}/result.json".format(path), "r", encoding="utf-8") as json_file:
        result_json = json_file.read()
    result = json.loads(result_json)

    # 读取错误信息
    with open("{}/error.txt".format(path), "r", encoding="utf-8") as errorFile:
        result["errorMessege"] = errorFile.read()
    
    return result

# 测试
if __name__ == "__main__":

    c_code = '''

#include <stdio.h>

int main() {
    printf("hello world\\n");
    return 0;
}

    '''

    cpp_code = '''

#include <iostream>
using namespace std;

int main() {
    cout << "hello world" << endl;
    return 0;
}

    '''

    python_code = '''

print("hello world")

    '''
    
    # print(judgeProblem(".", 0, c_code, "C"))
    # print(judgeProblem(".", 0, cpp_code, "C++"))
    # print(judgeProblem(".", 0, python_code, "Python3"))

