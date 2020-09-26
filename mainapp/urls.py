from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.loginUser, name="loginuser"),
    path('signup/', views.RegUser, name="reguser"),
    url(r'^external', views.external),
    url(r'^chatbot', views.chatbot),
    path('signup/complete', views.completeaccount, name="completeaccount"),
    path('users/edit/', views.UpdateUser, name="updateuser"),
    path('user/dashboard/', views.dash, name="dashboard"),
    path('logout/', views.logout_view, name="logout"),
    path('user/account/', views.account, name="account"),
    path('user/notification/', views.notif, name="notification"),
    path('user/reports/', views.viewreport, name='report'),
    path('user/email/', views.mail, name='mail'),
    path('user/reports/<int:pk>', views.viewreportdetail, name='reportdetail'),
]
