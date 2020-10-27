import os

#题目的数量
problem_cnt = 0

#题目对应的数据数量
problem_test_cnt = {}

'''
初始化文件夹与配置：
从problem/problem.config中读取配置到
    problem_cnt
    problem_test_cnt

'''

if os.path.exists("problem") == False:
    os.mkdir("problem")

if os.path.exists("problem/problem.config") == False:
    config_file = open(
        "problem/problem.config",
        "w", encoding="utf-8"
    )

    config_file.write(
        "problem_cnt: 0\n" +
        "problem_test_cnt:\n"
    )

    config_file.close()
else:
    config_file = open(
        "problem/problem.config",
        "r", encoding="utf-8"
    )

    problem_cnt = int(config_file.readline().split(':')[1].strip())
    config_file.readline()

    while True:
        line = config_file.readline()
        if line == "": break

        problem_id, test_cnt = line.split(':')
        problem_id = int(problem_id.strip())
        test_cnt = int(test_cnt.strip())

        problem_test_cnt[problem_id] = test_cnt
    
    config_file.close()


'''
模块：
generate_problem(description):
    通过题目描述初始化题目

add_test_data(input_data, output_data, problem_id):
    对题目problem_id加入一组数据

'''

#更新配置文件
def update_config():
    config_file = open(
        "problem/problem.config",
        "w", encoding="utf-8"
    )

    config_file.write(
        "problem_cnt: " + str(problem_cnt) + "\n" +
        "problem_test_cnt:\n"
    )

    for key in problem_test_cnt:
        config_file.write(
            str(key) + ":" +
            str(problem_test_cnt[key]) + "\n"
        )

    config_file.close()

#生成题目
def generate_problem(description):
    global problem_cnt
    global problem_test_cnt

    problem_cnt += 1
    problem_id = problem_cnt
    problem_test_cnt[problem_id] = 0

    os.mkdir("problem/" + str(problem_id))

    file = open(
        "problem/" + 
        str(problem_id) + "/"
        "description.txt", 
        "w", encoding="utf-8")

    file.write(description)
    file.close()

    update_config()

    return problem_id

#导入数据
def add_test_data(input_data, output_data, problem_id):
    global problem_test_cnt
    
    problem_test_cnt[problem_id] += 1
    test_id = problem_test_cnt[problem_id]

    input_file = open(
        "problem/" + 
        str(problem_id) + "/" +
        str(test_id) +
        ".in", 
        "w", encoding="utf-8"
        )

    output_file = open(
        "problem/" + 
        str(problem_id) + "/" +
        str(test_id) +
        ".out", 
        "w", encoding="utf-8"
        )

    input_file.write(input_data)
    output_file.write(output_data)
    
    input_file.close()
    output_file.close()

    update_config()


'''
单元测试：

'''

if __name__ == "__main__":
    id1 = generate_problem("计算a+b")
    id2 = generate_problem("计算a*b")

    input_data = ["2 3\n", "1 2\n"]
    output_data = ["5\n", "3\n"]

    for i in range(len(input_data)):
        add_test_data(input_data[i], output_data[i], id1)
