from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('loginview', views.loginview, name='loginview'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('manage', views.manage, name='manage'),
    path('datab', views.datab, name='datab'),
    path('register', views.register, name='register'),
    path('results', views.results, name='results'),
    
]