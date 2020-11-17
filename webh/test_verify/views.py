from django.shortcuts import HttpResponse,render,redirect
# Create your views here.
from django.urls.base import *
import json
from test_verify import models
from django.views.generic import View
from test_verify import tests
from login.models import User

from functools import wraps

# def login_required(func):
#     @wraps(func)
#     def inner(request,*args,**kwargs):
#         print(request.COOKIES)
#         is_login = request.get_signed_cookie('is_login',salt='zjw',default='')
#         if is_login !='':
#             return redirect('/login/?url={}'.format(request.path_info))
#         ret=func(request,*args,**kwargs)
#         return ret
#     return inner
#
#
# @login_required
class Mobileauthentication(View):

    def post(self,request):

        getemail =request.POST.get('user')
        # print(getemail)
        if User.objects.filter(userphone=getemail):

            getcode=tests.Mobileauthentication(getemail)
            # print(getcode)
            if getcode[0]==0:
                ret = {"captcha": '0', "msg":"短信发送出错，请检查联网情况", "data":[]}
                return HttpResponse(json.dumps(ret, ensure_ascii=False))
            else:
                data=[{"captcha":getcode[0],"time":getcode[1]}]
                ret = {"captcha": '0', "msg":"该手机未注册过用户", "data":data}
                return HttpResponse(json.dumps(ret, ensure_ascii=False))
        else:
            ret = {"code":400, "msg":"该手机未注册过用户","data":[]}
            return HttpResponse(json.dumps(ret, ensure_ascii=False))
        ret = {"code":400, "msg":"系统出错","data":[]}
        return HttpResponse(json.dumps(ret, ensure_ascii=False))
# @login_required
class Emailauthentication(View):

    def post(self, request):

        getemail =request.POST.get('user')
        # print(getemail)
        if User.objects.filter(email=getemail):
            getcode=tests.Emailauthentication(getemail)
            # print(type(getcode))
            # print(getcode["code"])
            # print(getcode["time"])
            if(getcode[0]==0):
                ret = {"captcha": '0', "msg": "邮件发送出错，请检查联网情况", "data": []}
                return HttpResponse(json.dumps(ret, ensure_ascii=False))

            else:
                data = [{"captcha": getcode[0], "time": getcode[1]}]
                ret = {"captcha": '0', "msg": "该手机未注册过用户", "data": data}
                return HttpResponse(json.dumps(ret, ensure_ascii=False))
        else:
            ret = {"code": 400, "msg": "该邮箱未注册过用户", "data": []}
            return HttpResponse(json.dumps(ret, ensure_ascii=False))
        ret = {"code": 400, "msg": "系统出错", "data": []}
        return HttpResponse(json.dumps(ret, ensure_ascii=False))
# def tq(request):
#     all_que=models.teacherquestion.objects.all()
#     return render(request,'zhanshi.html',{'all_que':all_que})
# def tq_add(request):
#     if request.method=='POST':
#         que = request.POST.get('geque')
#         det = request.POST.get('gedet')
#         aut = request.POST.get('geaut')
#         models.teacherquestion.objects.create(question=que,detail=det,author=aut)
#     return render(request,'zhanshi.html')
# def tq_del(request):
#     if request.method=='POST':
#         id = request.POST.get('geid')
#         models.teacherquestion.objects.get(pk=id).delete()
#     return render(request,'zhanshi.html')
# def tq_xiu(request):
#     pk=request.GET.get('pk')
#     xiu_obj=models.teacherquestion.objects.get(pk=pk)
#
#     if request.method=='POST':
#         xiuname=request.POST.get('xiuname')
#         xiu_obj.author=xiuname
#         xiu_obj.save()
#         return render(request, 'zhanshi.html')
# def login_zjw(request):
#     if request.method =='POST':
#         print('ok')
#         user =request.POST.get('user')
#         pwd =request.POST.get('pwd')
#         if models.User_zjw.objects.filter(username=user,password=pwd):
#             url=request.GET.get('url')
#             if url:
#                 return_url = url
#             else:
#                 return_url ='/index/'
#             ret =redirect(return_url)
#             ret.set_signed_cookie("is_login",'1',salt='zjw')
#
#             return ret
#             # return redirect('http://acm.hdu.edu.cn/status.php')
#     return render(request,'login_zjw.html')