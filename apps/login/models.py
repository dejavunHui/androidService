from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers
# Create your models here.


class User(models.Model):

    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'user_{0}/icon/{1}'.format(instance.username, filename)


    # id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20,verbose_name="用户名",primary_key=True)
    email = models.EmailField(null=False,verbose_name="邮箱")
    password = models.CharField(max_length=20,verbose_name='密码')
    age = models.IntegerField(verbose_name='年龄')
    gender = models.CharField(max_length=2,choices=(('M','男'),('F','女')))
    icon = models.ImageField(upload_to=user_directory_path,blank=True)
    registertime = models.DateField(auto_now=True)



    class Meta:
        db_table = 'users'
        verbose_name = '用户表'
        app_label='login'


