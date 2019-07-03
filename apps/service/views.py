from collections import OrderedDict

from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser, FormParser
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework import permissions
from common import *

'''
编写接口
'''
'''

URL Style	HTTP Method	Action	URL Name
{prefix}/	GET	list	{basename}-list
{prefix}/	POST	create	{basename}-list
{prefix}/{url_path}/	GET, or as specified by methods argument	@action(detail=False) decorated method	{basename}-{url_name}
{prefix}/{lookup}/	GET	retrieve	{basename}-detail
{prefix}/{lookup}/	PUT	update	{basename}-detail
{prefix}/{lookup}/	PATCH	partial_update	{basename}-detail
{prefix}/{lookup}/	DELETE	destroy	{basename}-detail
{prefix}/{lookup}/{url_path}/	GET, or as specified by methods argument	@action(detail=True) decorated method	{basename}-{url_name}
'''


# http:host:port/service/findpages/
class FindPageAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = FindPage.objects.all()
    serializer_class = FindPageSerializer
    def list(self,request,*args,**kwargs):
        return Response(FindPageSerializer(self.queryset,many=True).data)

class ShowPageAPIView(viewsets.ModelViewSet):
    queryset = ShowPage.objects.all()
    serializer_class = ShowPageSerializer

    # http:host:port/service/showpages/{username}/pageup/
    @action(methods=['post'], detail=True)
    def pageup(self, request, pk=None):

        ser = ShowPageSerializer(request.data)
        if ser.is_valid():
            ser.save()
            return Response({'status': 1})
        return Response({'status': 0})

    # http:host:port/service/showpages/{username}/userpageload/
    @action(methods=['get'], detail=True)
    def userpageload(self, request, pk=None):
        page = ShowPage.objects.get(username=pk)
        return Response(ShowPageSerializer(page, many=False))

    # http:host:port/service/showpages/{username}/pageload/
    @action(methods=['get'], detail=True)
    def pageload(self, request, pk=None):
        showpageall = ShowPage.objects.all()
        obj = StandardResultSetPagination()  # 分页
        showpage = obj.paginate_queryset(showpageall, request)
        showpage_ser = ShowPageSerializer(showpage, many=True)
        # 获取返回结果
        response = obj.get_paginated_response(showpage_ser.data)
        return response

    # http:host:port/service/showpages/{page_id}/pagechange/
    @action(methods=['post', 'put'], detail=True)
    def pagechange(self, request, pk=None):

        ret = ShowPage.objects.get(pk=pk)
        ser = ShowPageSerializer(instance=ret, data=request.data)

        if ser.is_valid():
            ser.save()
            return Response({'status': 1})
        else:
            return Response({'status': 0})


class ImageAPIView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    @action(methods=['get'],detail=True)
    def pageimages(self,request,pk=None):
        ret = Image.objects.fliter(showpage=pk)
        return Response(ImageSerializer(ret,many=True).data)
    
    def list(self,request,*args,**kwargs):
        ret = Image.objects.all()
        return Response(ImageSerializer(ret,many=True).data)
class RemarkAPIView(viewsets.ModelViewSet):
    queryset = Remark.objects.all()
    serializer_class = RemarkSerializer



class WealthBGAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = WealthBGModel.objects.all()
    serializer_class = WealthBGSerializer





# # 创建showpage
# def createShowPage(request):
#     back_msg = {'status': 0, 'msg': '验证失败'}
#     ser = ShowPageSerializer(data=request.data)
#     if ser.is_valid():
#         ser.save()
#         back_msg['status'] = 1
#         back_msg['msg'] = '存储成功'
#     return Response(back_msg)
#
#
# class ShowPageAPIVIew(APIView):
#     parser_classes = [JSONParser, FormParser]
#     # permission_classes = (permissions.IsAuthenticated,)
#
#     def get(self, request):
#         pk = request.GET.get('pk')
#         if pk:
#             ret = ShowPage.objects.get(pk=pk)
#             ser = ShowPageSerializer(ret,many=False)
#             return Response(ser.data)
#         showpageall = ShowPage.objects.all()
#         obj = StandardResultSetPagination()  # 分页
#         showpage = obj.paginate_queryset(showpageall, request)
#         showpage_ser = ShowPageSerializer(showpage, many=True)
#         # 获取返回结果
#         response = obj.get_paginated_response(showpage_ser.data)
#         print(showpage_ser.data)
#         return response
#
#
# def post(self, request):
#     return createShowPage(request=request)
#
#
# def put(self, request, pk):
#     showpage = ShowPage.objects.filter(pk=pk).first()
#     showpage_ser = ShowPageSerializer(instance=showpage, data=request.data)
#     msg_back = {'status': 0, 'data': None, 'msg': '更改失败'}
#     if showpage_ser.is_valid():
#         showpage_ser.save()
#         msg_back['status'] = 1
#         msg_back['data'] = showpage_ser.data
#         msg_back['msg'] = '更改成功'
#     return Response(msg_back)
#
#
# def delete(self, request, pk):
#     ShowPage.objects.filter(pk=pk).delete()
#     return Response({'status': 1, 'msg': '删除完成'})
#
#
# # http://host:port/getimages?type=1&pk=0/
# class ImageAPIView(APIView):
#     parser_classes = [JSONParser, FormParser]
#
#     def getImage(self, request):
#         print(request.GET)
#         type = request.GET.get('type')
#         pk = request.GET.get('pk')
#         obj = None
#         ret = None
#         ser = None
#         if not type or not pk:
#             return HttpResponse("没有查询条件")
#         if type == SHOWPAGE:
#             obj = ShowPage.objects.get(pk=pk)
#             ret = obj.image_set.all()
#             ser = ImageSerializer(ret, many=True)
#
#         elif type == FINDPAGE:
#             obj = FindPage.objects.get(pk=pk)
#             ret = obj.image_set.all().first()
#             ser = ImageSerializer(ret, many=False)
#
#         elif type == USERPAGE:
#             obj = User.objects.get(pk=pk)
#             ret = obj.image_set.all().first()
#             ser = ImageSerializer(ret, many=False)
#
#         return Response(ser.data)
#
#     def get(self, request):
#         return self.getImage(request)
#
#
# # http://host:port/getwealthbg?wealth=1&jijie=0/
# class WealthBGAPIView(APIView):
#     parser_classes = [JSONParser, FormParser]
#
#     def getWealthBG(self, request):
#         wealth = request.GET.get('wealth')
#         jijie = request.GET.get('jijie')
#         if not wealth:
#             return HttpResponse("缺少查询条件")
#         ret = WealthBGModel.objects.filter(wealth=wealth, jijie=jijie)
#         ser = WealthBGSerializer(ret, many=True)
#         return Response(ser.data)
#
#     def get(self, request):
#         return self.getWealthBG(request)
#
#
# # http://host:port/getwealthpeom?wealth=1&jijie=0&theme=1/
# class WealthPeomAPIView(APIView):
#     parser_classes = [JSONParser, FormParser]
#
#     def getWealthPeom(self, request):
#         wealth = request.GET.get('wealth')
#         theme = request.GET.get('theme')
#         jijie = request.GET.get('jijie')
#         if not wealth:
#             return HttpResponse('缺少查询条件')
#         ret = WealthPeomModel.objects.filter(wealth=wealth, theme=theme, jijie=jijie)
#         ser = WealthPeomSerializer(ret, many=True)
#         return Response(ser.data)
#
#     def get(self, request):
#         return self.getWealthPeom(request)
#
#
# class FindPageAPIView(APIView):
#     parser_classes = [JSONParser, FormParser]
#
#     def get(self, request):
#         ret = FindPage.objects.all()
#         obj = StandardResultSetPagination()
#         ret_ = obj.paginate_queryset(ret, request)
#         ser = FindPageSerializer(ret_, many=True)
#         response = obj.get_paginated_response(ser.data)
#         return response
#
