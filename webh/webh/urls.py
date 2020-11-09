"""webh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse,render,redirect
from test_verify import views as xiuviews
from login import views
from mainForStu import views as mainView
from mainForTea import views as teacherView
urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'Mobileauthentication/', xiuviews.Mobileauthentication.as_view(), name="Mobileauthentication"),
    path(r'Emailauthentication/', xiuviews.Emailauthentication.as_view(), name="Emailauthentication"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('teacher/', views.LoginForTeacher.as_view(), name="loginForTeacher"),
    path('main/', mainView.MainView.as_view(), name="main"),
    path('modify/', views.ModifyInformation.as_view(), name="modify"),
    path('getDataList/', teacherView.GetDataListView.as_view(), name="getDataList"),
    path('showQuestions/', teacherView.showQuestions.as_view(), name="showQuestions"),
    path('addDataList/', teacherView.addQuestions.as_view(), name="addQuestions"),
    path('deleteQuestion/', teacherView.deleteQuestion.as_view(), name="deleteQuestion"),
    path('alterQuestions/', teacherView.alterQuestions.as_view(), name="alterQuestions"),
    path('showTestData/', teacherView.showTestData.as_view(), name="showTestData"),
    path('addDataList/', teacherView.addTestData.as_view(), name="addTestData"),
    path('deleteQuestion/', teacherView.deleteTestData.as_view(), name="deleteTestData"),
    path('alterTestData/', teacherView.alterTestData.as_view(), name="alterTestData"),
    path('getState/', mainView.StateView.as_view(), name="getState"),
]
