from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserLoginSerializers


class UsernameLogin(APIView):
    serializer_class = UserLoginSerializers

    def get(self, request, username):
        # 判断是不是重复的用户名
        try:
            count = User.objects.filter(username=username).count()
        except Exception as e:
            return Response({
                'code': 400,
                'errmsg': '访问数据库失败'
            })
        return Response({
            'code': 200,
            'count': count,
            'errmsg': 'ok'
        })


class MobileLogin(APIView):
    serializer_class = UserLoginSerializers

    def get(self, request, mobile):
        # 判断手机号是否已被使用

        try:
            count = User.objects.filter(mobile=mobile).count()
        except Exception as e:
            return Response({
                'code': 400,
                'errmsg': '查询数据库出错'
            })

        return Response({
            'code': 200,
            'count': count,
            'errmsg': 'ok'
        })
