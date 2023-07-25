from django.contrib import admin
from django.urls import path, include
from . import views
from .views import problem_list, submission,submit_code
urlpatterns = [
    path('', views.home,name="home"),
    path('signup', views.signup,name="signup"),
    path('signin', views.signin,name="signin"),
    path('signout', views.signout,name="signout"),
    path('problems/', views.problem_list, name='problem_list'),
    path('submission/<int:problem_id>/', views.submission, name='submission'),
    path('submit_code/<int:problem_id>/', views.submit_code, name='submit_code'),  
]
