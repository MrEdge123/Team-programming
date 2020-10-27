from import_problem import *
from judge_problem import *


def main():
    #前端输入题目描述
    problem_description = (
        "计算a+b\n" +
        "输入：两个整数，a和b\n" +
        "输出：a+b的结果\n"
    )

    #生成新题目
    problem_id = generate_problem(problem_description)

    #前端输入数据
    input_data = ["2 3\n", "1 2\n"]
    output_data = ["5\n", "3\n"]

    #导入数据到题目
    for i in range(len(input_data)):
        add_test_data(
            input_data[i], 
            output_data[i], 
            problem_id
        )
    
    #前端输入代码
    code = (
        "s = input().split()\n" +
        "print(int(s[0]) + int(s[1]))\n" 
    )

    #判断对错
    ok = judge_problem(code, problem_id)

    if ok:
        print("Accepted!!")
    else:
        print("Wrong Answer!!")


if __name__ == "__main__":
    main()
