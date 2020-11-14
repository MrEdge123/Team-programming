import json

from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#学生界面获取总题目
from django.views import View
import random
from mainForStu.models import ProblemsContent, ProblemTestData


class GetDataListView(View):

    def get(self, request):
        # print("------get--------")

        #判断用户是否登录
        # result = request.session.get('username', 'null')
        # if result == 'null':
        #     print(result)
        if 'username' in request.session:
            # print("------test--------")
            # print(request.session['username'])
            ret = {"code": "200", "msg": "用户登录"}

            #存储数据
            # examples_data = []
            data = []

            # test = ProblemsContent.objects.values("problemId", "problemTitle")[0:1]
            # test.filter()
            # problemsList = ProblemsContent.objects.filter()
            dataList = ProblemTestData.objects.filter()
            # print(dataList)
            for i in range(len(dataList)):
                # print(dataList[i])
                #将model转化为字典
                problem_dict = model_to_dict(dataList[i])
                # print(problem_dict)
                data.append(problem_dict)
            ret = {"code": "200", "msg": "成功获取", "data": data}
            return HttpResponse(json.dumps(ret, ensure_ascii=False))

        ret = {"code": "400", "msg": "用户未登录"}
        return HttpResponse(json.dumps(ret, ensure_ascii=False))

class showQuestions(View):
    def get(self, request):
        # print("------get--------")
        return render(request, "register.html", {})
    def post(self,request):
        all_que = ProblemsContent.objects.all()
        all_quea = ProblemTestData.objects.all()
        return render(request, 'zhanshi.html', {'all_que': all_que,'all_quea': all_quea,})

class addQuestions(View):
    def get(self, request):
        # print("------get--------")
        return render(request, "register.html", {})
    def post(self,request):
        problemId = request.POST.get('problemId')
        problemTitle = request.POST.get('problemTitle')
        memoryLimit = request.POST.get('memoryLimit')
        timeLimit = request.POST.get('timeLimit')
        problemDescription = request.POST.get('problemDescription')
        inputDescription = request.POST.get('inputDescription')
        outputDescription = request.POST.get('outputDescription')
        try:
            ProblemsContent.objects.create(problemId=problemId, problemTitle=problemTitle, memoryLimit=memoryLimit,
                                           timeLimit=timeLimit,problemDescription=problemDescription,
                                           inputDescription=inputDescription,outputDescription=outputDescription)
            ret = {"code": 200, "msg": "添加题目成功"}
            return HttpResponse(json.dumps(ret, ensure_ascii=False))
        except:
            ret = {"code": 400, "msg": "插入错误"}
            return HttpResponse(json.dumps(ret, ensure_ascii=False))

class deleteQuestion(View):
    def get(self, request):
        # print("------get--------")
        return render(request, "register.html", {})
    def post(self,request):
        try:
            problemId= request.POST.get('problemId')
            ProblemsContent.objects.get(problemId=problemId).delete()
            ret = {"code": 200, "msg": "删除成功"}
            return HttpResponse(json.dumps(ret, ensure_ascii=False))
        except:
            ret = {"code": 400, "msg": "删除错误"}
            return HttpResponse(json.dumps(ret, ensure_ascii=False))
class alterQuestions(View):
    def get(self, request):
        # print("------get--------")
        return render(request, "register.html", {})
    def post(self,request):
        try:
            problemId = request.POST.get('problemId')
            xiu_obj = ProblemsContent.objects.get(problemIdk=problemId)
            problemTitle = request.POST.get('problemTitle')
            memoryLimit = request.POST.get('memoryLimit')
            timeLimit = request.POST.get('timeLimit')
            problemDescription = request.POST.get('problemDescription')
            inputDescription = request.POST.get('inputDescription')
            outputDescription = request.POST.get('outputDescription')


            xiu_obj.problemId = problemId
            xiu_obj.problemTitle = problemTitle
            xiu_obj.memoryLimit = memoryLimit
            xiu_obj.timeLimit = timeLimit
            xiu_obj.problemDescription = problemDescription
            xiu_obj.inputDescription  = inputDescription
            xiu_obj.outputDescription = outputDescription

            xiu_obj.save()
            ret = {"code": 200, "msg": "修改成功"}
            return HttpResponse(json.dumps(ret, ensure_ascii=False))
        except:
            ret = {"code": 400, "msg": "修改错误"}
            return HttpResponse(json.dumps(ret, ensure_ascii=False))



class showTestData(View):
    def get(self, request):
        # print("------get--------")
        return render(request, "register.html", {})

    def post(self, request):

        all_quea = ProblemTestData.objects.all()
        return render(request, 'zhanshi.html', {'all_quea': all_quea, })

class addTestData(View):
    def get(self, request):
        # print("------get--------")
        return render(request, "register.html", {})

    def post(self, request):
        try:
            problemId = request.POST.get('problemId')
            number = request.POST.get('number')
            inputData = request.POST.get('inputData')
            outputData = request.POST.get('outputData')
            isExample = request.POST.get('isExample')
            explanation = request.POST.get('explanation')

            if ProblemTestData.objects.filter(problemId=problemId):
                ProblemsContent.objects.create(problemId=problemId, number=number, inputData=inputData,
                                               outputData=outputData, isExample=isExample,
                                               explanation=explanation)
            ret = {"code": 200, "msg": "添加成功"}
            return HttpResponse(json.dumps(ret, ensure_ascii=False))
        except:
            ret = {"code": 400, "msg": "添加错误"}
            return HttpResponse(json.dumps(ret, ensure_ascii=False))
class deleteTestData(View):
    def get(self, request):
        # print("------get--------")
        return render(request, "register.html", {})

    def post(self, request):
        problemId = request.POST.get('problemId')
        isExample = request.POST.get('isExample')
        if ProblemTestData.objects.filter(problemId=problemId,isExample=isExample):
            if (len(ProblemTestData.objects.all(isExample=isExample))>1):
                ProblemsContent.objects.get(problemId=problemId).delete()
                ret = {"code": 200, "msg": "删除成功"}
                return HttpResponse(json.dumps(ret, ensure_ascii=False))
            ret = {"code": 400, "msg": "无法删除必须含有两种例子"}
            return HttpResponse(json.dumps(ret, ensure_ascii=False))
        ret = {"code": 400, "msg": "删除错误"}
        return HttpResponse(json.dumps(ret, ensure_ascii=False))
class alterTestData(View):
    def get(self, request):
        # print("------get--------")
        return render(request, "register.html", {})

    def post(self, request):
        try:
            problemId = request.POST.get('problemId')
            xiu_obj = ProblemTestData.objects.get(problemId=problemId)

            number = request.POST.get('number')
            inputData = request.POST.get('inputData')
            outputData = request.POST.get('outputData')

            explanation = request.POST.get('explanation')



            xiu_obj.problemId = problemId
            xiu_obj.inputData = inputData
            xiu_obj.number = number
            xiu_obj.outputData = outputData
            xiu_obj.explanation = explanation


            xiu_obj.save()
            ret = {"code": 200, "msg": "修改成功"}
            return HttpResponse(json.dumps(ret, ensure_ascii=False))

        except:
            ret = {"code": 400, "msg": "修改错误"}
            return HttpResponse(json.dumps(ret, ensure_ascii=False))

    # def post(self, request):
    #     print("------post--------")
    #     ret = {"code": False, "error": "用户名或密码错误"}
    #     return HttpResponse(json.dumps(ret, ensure_ascii=False))
    #     # return render(request, "test.html", {})
