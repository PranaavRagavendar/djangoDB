from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('status',views.status,name='status'),
    path('attendance',views.attendance,name='attendance'),
    path('login',views.login,name='login'),
    path('user',views.user,name='user'),   
]
