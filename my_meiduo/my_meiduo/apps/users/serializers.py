from rest_framework import serializers
from users.models import User


class UserLoginSerializers(serializers.ModelSerializer):

    class Mate:
        model = User
        fields = '__all__'
        # 添加约束
        extra_kwargs = {
            'username':{
                'max_length':20,
                'min_length':5
            },
            'password':{
                'max_length':20,
                'min_length':6
            }
        }

    def create(self, validated_data):
        # 用户密码加密
        user = User.objects.create_user(**validated_data)

        return user