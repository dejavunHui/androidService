from django.db import models
from rest_framework.pagination import LimitOffsetPagination

from ..login.models import User
from extra_apps.DjangoUeditor.models import UEditorField


# Create your models here.

class Page(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40, blank=False, null=False, verbose_name='标题')
    content = UEditorField(verbose_name='内容', imagePath='goods/images/', width=1000, height=300,
                           filePath='goods/files/', default='')
    time = models.DateTimeField(auto_now=True, verbose_name='产生时间')

    class Meta:
        abstract = True


class ShowPage(Page):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'showpage'
        verbose_name = '晒一晒文章'
        ordering = ['-time']


class Remark(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE,null=False)
    to = models.CharField(max_length=20,verbose_name="评论对象",null=True,blank=True)
    page = models.ForeignKey(ShowPage, on_delete=models.CASCADE,null=False)
    content = UEditorField(verbose_name='内容', imagePath='app/images/', width=1000, height=300,
                           filePath='app/files/', default='')
    time_l = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')

    class Meta:
        db_table = 'remark'
        verbose_name = '评论'
        ordering = ['page','time_l']


class FindPage(Page):
    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>

        return 'user_page/{0}/{1}'.format(instance.title, filename)

    look = models.IntegerField(null=True)
    headImage = models.ImageField(upload_to=user_directory_path)
    class Meta:
        db_table = 'findpage'
        verbose_name = '发现文章'
        ordering = ['time']


class Image(models.Model):

    # 图片上传位置
    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>

        return 'user_page/{0}/{1}'.format('showpage', filename)

    id = models.AutoField(primary_key=True)
    showpage = models.ForeignKey(ShowPage, on_delete=models.CASCADE, blank=True, null=True)
    remark = models.ForeignKey(Remark, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to=user_directory_path)
    # name = models.CharField(max_length=10, blank=True, null=True, default=None)

    class Meta:
        db_table = 'image'
        verbose_name = '图片'


class WealthBGModel(models.Model):

    def user_upload(instance, filename):
        return 'wealth/{0}/{1}'.format(instance.name, filename)

    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to=user_upload, verbose_name='天气背景图')
    wealth = models.IntegerField(verbose_name='天气状况')
    class Meta:
        verbose_name = '天气背景'


# 分页显示
class StandardResultSetPagination(LimitOffsetPagination):
    # 默认每页显示的条数
    default_limit = 20
    # url 中传入的显示数据条数的参数
    limit_query_param = 'limit'
    # url中传入的数据位置的参数
    offset_query_param = 'offset'
    # 最大每页显示条数
    max_limit = 50
