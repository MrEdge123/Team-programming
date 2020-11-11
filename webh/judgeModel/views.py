import json
import os
import subprocess
import time
import random

from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.contrib.auth.decorators import login_required
from mainForStu.models import ProblemsContent, ProblemTestData, SubmitStatus

'''
SubmitCodeView(View): 提交代码视图

request请求:
GET方法:
无

POST方法:
前端传入:
1.sessionid
2.json, 内容:
    problemId: 题目编号
    language: 提交语言, 目前仅有: C, C++, Python3
    code: 提交代码

例子:
{
    "problemId": "1",
    "language": "Python3"
    "code": "print('hello world')"
}

后端返回内容json, 共5种:
1.{"code": "400", "msg": "提交语言错误"}
2.{"code": "400", "msg": "题目编号错误"}
3.{"code": "200", "msg": "评测成功"}
4.{"code": "400", "msg": "评测失败"}
5.{"code": "400", "msg": "用户未登录"}

'''

# 提交代码视图
class SubmitCodeView(View):

    def get(self, request):
        pass


    def post(self, request):
        result = request.session.get('username', 'null')

        if result == 'null':
            print(result)

        if 'username' in request.session:
            json_str = request.body
            json_data = json.loads(json_str)

            userName = request.session['username']
            # userName = 'mredge'
            problemId = json_data['problemId']
            code = json_data['code']
            language = json_data['language']

            print("problemId:" + problemId)
            print("language:" + language)

            if language != 'C' and language != 'C++' and language != 'Python3':
                ret = {"code": "400", "msg": "提交语言错误"}
            else:
                if len(ProblemsContent.objects.filter(problemId=problemId)) == 0:
                    ret = {"code": "400", "msg": "题目编号错误"}
                else:
                    ok = self.runCode(userName, problemId, code, language)
                    if ok:
                        ret = {"code": "200", "msg": "评测成功"}
                    else:
                        ret = {"code": "400", "msg": "评测失败"}
        else:
            ret = {"code": "400", "msg": "用户未登录"}
        
        return HttpResponse(json.dumps(ret, ensure_ascii=False))


    '''
    void runCode(userName, problemId, code, language)

    1.传入参数
    userName: 用户名, 类型为字符串, 用于数据库查询
    problemId: 题目编号, 类型为数字, 用于数据库查询
    code: 评测代码, 类型为字符串
    language: 评测语言, 类型为字符串, 暂时支持的语言有: "C", "C++", "Python3" (注意大小写)

    '''
    def runCode(self, userName, problemId, code, language):
        # 创建判题文件夹
        basePath = "./judgeSpace"

        submitTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        
        path_id = random.randint(1, 1000000)
        path = basePath + "/" + str(path_id)

        while os.path.exists(path):
            path_id = random.randint(1, 1000000)
            path = basePath + "/" + str(path_id)
        
        os.makedirs(path)

        # 添加判题状态
        try:
            status = SubmitStatus(  submitTime=submitTime, 
                                userName=userName,
                                problemId=problemId,
                                judgeResult="评测中",
                                usedMemory=-1,
                                usedTime=-1,
                                language=language,
                                code=code
                            )
            status.save()
        except:
            return False

        # 判题
        result = self.judgeProblem(path, problemId, code, language)

        meaning = {"AC":"通过", "WA":"答案错误", 
                    "TE":"运行超时", "ME":"空间超限",
                    "CE":"编译错误", "RE":"运行错误"
                    }

        # 修改判题状态
        status.judgeResult = meaning[result["result"]]
        status.usedMemory = result["memoryUsed"]
        status.usedTime = result["timeUsed"]
        status.save()

        # 删除判题文件夹
        delList = os.listdir(path)
        for fileName in delList:
            os.remove(path + "/" + fileName)
        
        os.rmdir(path)

        return True

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
    dict judgeProblem(path, problemId, code, language)

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
    def judgeProblem(self, path, problemId, code, language):
        # 判题核心位置(待修改)
        if not os.path.exists("./judgeModel/judgeCore.cpp"):
            print("判题核心路径错误!!, 应放在工作目录的judgeModel目录下")
            return
        
        subprocess.run("g++ ./judgeModel/judgeCore.cpp -o {}/core".format(path), shell=True)

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
        result = self.compileCode(path, language)
        if result["result"] == "CE": return result

        '''
        读取数据库, 然后单个数据评测

        数据: input.txt, answer.txt

        runJudge(path, language, timeLimit, memoryLimit, checkMode)

        timeLimit: 时间限制, 单位为毫秒(ms)
        memoryLimit: 空间限制, 单位为KB
        checkMode: 结果对比模式, 类型为字符串
        '''

        # 获得时间限制和空间限制
        problmeLimit = ProblemsContent.objects.get(problemId=problemId)
        timeLimit = problmeLimit.timeLimit
        memoryLimit = problmeLimit.memoryLimit

        # 获取题目评测数据
        dataList = ProblemTestData.objects.filter(problemId=problemId)
        
        for data in dataList:
            # 写入一组评测数据
            with open("{}/input.txt".format(path), "w", encoding="utf-8") as inputFile:
                inputFile.write(data.inputData)
            with open("{}/answer.txt".format(path), "w", encoding="utf-8") as answerFile:
                answerFile.write(data.outputData)
            
            # 评测一组数据
            tmp_result = self.runJudge(path, language, timeLimit, memoryLimit)
            if tmp_result["result"] != "AC":
                result = tmp_result
                break

            # 更新状态
            result["timeUsed"] = max(result["timeUsed"], tmp_result["timeUsed"])
            result["memoryUsed"] = max(result["memoryUsed"], tmp_result["memoryUsed"])

        return result


    '''
    dict complileCode(language)

    1.传入参数
    language: 评测语言, 类型为字符串

    2.返回参数
    字典, key有: "result", "timeUsed", "memoryUsed", "errorMessage"

    '''

    def compileCode(self, path, language):
        # 创建文件
        with open("{}/error.txt".format(path), "w", encoding="utf-8") as errorFile:
            pass

        # 运行core
        subprocess.run("{0}/core -mode {1} -lang {2} -path {3}".format(
            path, "cp", language, path), shell=True)

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

    def runJudge(self, path, language, timeLimit, memoryLimit, checkMode = "ignore-not"):
        # 创建文件
        with open("{}/error.txt".format(path), "w", encoding="utf-8") as errorFile:
            pass

        # 运行core
        subprocess.run("{0}/core -mode {1} -lang {2} -tl {3} -ml {4} -check {5} -path {6}".format(
                path, "run", language, timeLimit, memoryLimit, checkMode, path
            ), shell=True
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

