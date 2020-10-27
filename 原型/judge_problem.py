import os


'''
初始化文件夹：

'''

if os.path.exists("program") == False:
    os.mkdir("program")

'''
模块：
judge_problem(code, problem_id):
    对题目problem_id的代码code进行评测

'''

#把代码导入到对应位置
def generate_program(code):
    program_file = open(
        "program/" +
        "code.py",
        "w", encoding="utf-8"
        )

    program_file.write(code)
    program_file.close()

#运行程序
def run_program(input_path):
    os.system(
        "python program/code.py" +
        " < " + input_path +
        " > " + "program/output.out"
    )

#对比输出结果
def compare_output(out1_path, out2_path):
    out1_file = open(
        out1_path,
        "r", encoding="utf-8"
    )

    out2_file = open(
        out2_path,
        "r", encoding="utf-8"
    )

    #逐行进行对比
    while True:
        out1 = out1_file.readline()
        out2 = out2_file.readline()

        if out1 == "" and out2 == "":
            break

        if out1 == "" or out2 == "":
            out1_file.close()
            out2_file.close()
            return False

        out1 = out1.rstrip()
        out2 = out2.rstrip()

        if out1 != out2:
            out1_file.close()
            out2_file.close()
            return False

    out1_file.close()
    out2_file.close()
    return True

#判题
def judge_problem(code, problem_id):
    generate_program(code)

    test_data = os.listdir("problem/" + str(problem_id))

    #读取每个数据
    for input_name in test_data:
        if input_name[-3:] == ".in":
            output_name = input_name[:-3] + ".out"

            run_program(
                "problem/" + 
                str(problem_id) + "/" + 
                input_name
            )

            if compare_output(
                "problem/" +
                str(problem_id) + "/" +
                output_name, 
                "program/output.out"
                ) == False:

                return False
    
    return True


'''
单元测试：

'''

if __name__ == "__main__":
    code = (
        "s = input().split()\n" +
        "print(int(s[0]) + int(s[1]))\n" 
    )

    print(judge_problem(code, 1))