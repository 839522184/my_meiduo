from django.urls import re_path
from users import views

urlpatterns = [
    # 用户名重复注册
    re_path(r'^usernames/(?P<username>\w{5,20})/count/$', views.UsernameLogin.as_view()),
    # 手机号重复注册
    re_path(r'^mobiles/(?P<mobile>1[3-9]\d{9})/count/$', views.MobileLogin.as_view()),
]