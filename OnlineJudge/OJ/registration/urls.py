from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('signup', views.signup,name="signup"),
    path('signin', views.signin,name="signin"),
    path('signout', views.signout,name="signout"),
    path('problem_list',views.problem_list, name='problem_list'),
    
]
