import json
import datetime

from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.contrib.auth.decorators import login_required
from mainForStu.models import ProblemsContent, ProblemTestData,SubmitStatus

#学生界面获取总题目
class MainView(View):

    def get(self, request):
        # print("------get--------")

        #判断用户是否登录
        result = request.session.get('username', 'null')
        if result == 'null':
            # print(result)
            pass

        if 'username' in request.session:
            # print("------test--------")
            # print(request.session['username'])
            ret = {"code": "200", "msg": "用户登录"}

            #存储数据
            examples_data = []
            data = []

            # test = ProblemsContent.objects.values("problemId", "problemTitle")[0:1]
            # test.filter()
            # problemsList = ProblemsContent.objects.filter()
            problemsList = ProblemsContent.objects.values("problemId", "problemTitle")
            # print(problemsList)
            for i in range(len(problemsList)):
                # print(problemsList[i])
                #将model转化为字典
                # problem_dict = model_to_dict(problemsList[i])
                # print(problem_dict)
                data.append(problemsList[i])
            ret = {"code": "200", "msg": "用户登录", "data": data}
            return HttpResponse(json.dumps(ret, ensure_ascii=False))

        ret = {"code": "400", "msg": "用户未登录"}
        return HttpResponse(json.dumps(ret, ensure_ascii=False))


    def post(self, request):
        # print("------post--------")
        ret = {"code": False, "error": "用户名或密码错误"}
        return HttpResponse(json.dumps(ret, ensure_ascii=False))
        # return render(request, "test.html", {})


class DetailsView(View):

    def get(self, request):
        # print("------get--------")

        # 判断用户是否登录
        if 'username' in request.session:
            # print("------test--------")
            # print(request.session['username'])
            ret = {"code": "200", "msg": "用户登录"}

            examples_data = []
            pno = request.GET.get("problemId", "")


            problem = ProblemsContent.objects.filter(problemId=pno) 
            if len(problem) == 0:
                
                ret = {"code": "400", "msg": "problemId错误"} 
                return HttpResponse(json.dumps(ret, ensure_ascii=False)) 
           
            problem_dict = model_to_dict(problem[0])

            # 如果题目存在例子则获取例子
            examples = ProblemTestData.objects.filter(problemId=pno, isExample=1)
            if len(examples) != 0:
                for j in range(len(examples)):
                    example_dict = model_to_dict(examples[j])
                    # print(example_dict)
                    examples_data.append(example_dict)
                # 将获取的数据存到相应的题目字典里
                problem_dict['examples'] = examples_data

            ret = {"code": "200", "msg": "用户登录", "data": problem_dict}
            return HttpResponse(json.dumps(ret, ensure_ascii=False))

        ret = {"code": "400", "msg": "用户未登录"}
        return HttpResponse(json.dumps(ret, ensure_ascii=False))

    def post(self, request):
        pass


class StateView(View):

    def get(self, request):
        # print("------get--------")

        # 判断用户是否登录
        result = request.session.get('username', 'null')
        if result == 'null':
            # print(result)
            pass

        if 'username' in request.session:
            # print("------test--------")
            # print(request.session['username'])
            ret = {"code": "200", "msg": "用户登录"}

            # 存储数据
            data = []

            stateList = SubmitStatus.objects.values("userName","judgeResult","problemId","usedMemory",
                                                    "usedTime","language", "submitTime").order_by("-submitTime")
            # print(stateList)
            for i in range(len(stateList)):
                # print(stateList[i])
                # 将model转化为字典
                # problem_dict = model_to_dict(problemsList[i])
                # print(problem_dict)
                data.append(stateList[i])
            ret = {"code": "200", "msg": "用户登录", "data": data}
            return HttpResponse(json.dumps(ret, ensure_ascii=False, cls=DateEncoder))

        ret = {"code": "400", "msg": "用户未登录"}
        return HttpResponse(json.dumps(ret, ensure_ascii=False))

    def post(self, request):
        pass

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')

        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")

        else:
            return json.JSONEncoder.default(self, obj)
            
