# 模块接口设计

[toc]

## 导入问题：import_problem

### 内容

- 函数：`generate_problem()`
- 函数：`add_test_data()`
- 题目描述：`problem/problem_id/description.txt`
- 输入数据：`problem/problem_id/*.in`
- 输出数据：`problem/problem_id/*.out`

### 函数层次关系

```python
generate_problem()
add_test_data()
```

### generate_problem()

原型：

```python
problem_id generate_problem(description)
```
`problem_id`：`number`类型，题目编号
`description`：`string`类型，题目描述

作用：

生成一个新的题目，把题目描述写到`description.txt`里面，最后返回题目`id`

### add_test_data()

原型：

```python
void add_test_data(input_data, output_data, problem_id)
```
`input_data`：`string`类型，输入数据
`output_data`：`string`类型，输出数据
`problem_id`：`number`类型，题目编号

作用：

添加题目`problem_id`的输入数据到`*.in`，输出数据到`*.out`

---

## 判题：judge_problem

### 内容

- 函数：`judge_problem()`
- 函数：`generate_program()`
- 函数：`run_program()`
- 函数：`compare_output()`
- 程序：`program/code.py`
- 输出：`program/output.out`

### 函数层次关系

```python
judge_problem()
    generate_program()

    for each test data
        run_program()
        compare_output()
```

### judge_problem()

原型：

```python
result judge_problem(code, problem_id)
```
`result`：`bool`类型，返回判题结果
`code`：`string`类型，提交的代码
`problem_id`：`number`类型，题目编号

作用：

判断对于题目`problem_id`，代码`code`是否正确

### generate_program()

原型：

```python
void generate_program(code)
```
`code`：`string`类型，提交的代码

作用：

把提交的代码放到`program/code.py`

### run_program()

原型：

```python
void run_program(input_path)
```
`input_path`：`string`类型，输入文件的路径

作用：

运行`program/code.py`，重定向输入为`input_path`，输出为`program/output.out`

### compare_output()

原型：

```python
bool compare_output(out1_path, out2_path)
```
`out1_path`：`string`类型，输出文件1的路径
`out2_path`：`string`类型，输出文件2的路径

---

## 主程序：main

### 内容

- 函数：`main()`
- 模块：`import_problem`
- 模块：`judge_problem`
- 函数：`generate_problem()`
- 函数：`add_test_data()`
- 函数：`judge_problem()`

### 函数层次关系

```python
main()
    generate_problem()
    add_test_data()
    judge_problem()
```

