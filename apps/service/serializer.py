from rest_framework import serializers
from .models import *


# 定义序列化
class ShowPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowPage
        fields = '__all__'



class FindPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindPage
        fields = '__all__'


class RemarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remark
        fields = '__all__'


class WealthBGSerializer(serializers.ModelSerializer):
    class Meta:
        model = WealthBGModel
        fields = '__all__'



class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'