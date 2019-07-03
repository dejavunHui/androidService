from .models import *
from extra_apps import xadmin


class ShowPageAdmin(object):
    style_fields = {"content": "ueditor"}
    list_display = ['title']


class RemarkAdmin(object):
    style_fields = {"content": "ueditor"}
    list_display = ['autor']


class ImageAdmin(object):

    list_display = ['id']


class FindPageAdmin(object):

    style_fields = {"content": "ueditor"}
    list_display = ['title']

class UserAdmin(object):

    list_display = ['username']


xadmin.site.register(ShowPage, ShowPageAdmin)
xadmin.site.register(Remark, RemarkAdmin)
xadmin.site.register(Image,ImageAdmin)
xadmin.site.register(FindPage,FindPageAdmin)
xadmin.site.register(WealthBGModel)


xadmin.site.register(User,UserAdmin)
# xadmin.site.register(ShowPageImage)
# xadmin.site.register(RemarkImage)
