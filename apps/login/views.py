from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm

from rest_framework.parsers import JSONParser, FormParser, FileUploadParser
from .models import *
from .serializer import *
from rest_framework.response import Response


# Create your views here.


class LoginView(View):

    def get(self, request):
        return render(request, 'login/login.html', {'form': LoginForm()})

    def post(self, request):
        data = request.POST
        form = LoginForm(data, initial=data)
        form.is_valid()
        form.password = ''
        print(data)
        return render(request, 'login/login.html', {'form': form})


class RegisterView(View):

    def get(self, request):
        return render(request, 'login/login.html', {'form': RegisterForm()})

    def post(self, request):
        data = request.POST
        form = RegisterForm(data, initial=data)
        form.is_valid()
        form.password = ''
        print(data)
        print(type(request.FILES.get('icon')))
        return render(request, 'login/login.html', {'form': form})


# class UserAPIView(APIView):
#     parser_classes = [JSONParser, FormParser, FileUploadParser]
#     # permission_classes = (IsAuthenticated,)
#
#     #http://host:port/users?password=/
#     def get(self, request,name):
#         print(request.GET)
#
#         ret = User.objects.get(username = name)
#
#         ser = UserSerializer(ret, many=False)
#         return Response(ser.data)
#
#
#
#     def post(self, request):
#         print(request.POST)
#
#         ser = UserSerializer(data=request.data)
#
#         if ser.is_valid():
#             ser.save()
#
#         return Response({"status":1})
#
#     # def put(self, request, pk):
#     #
#     #     ret = User.objects.get(pk=pk)
#     #     ser = UserSerializer(instance=ret,data=request.data)
#     #     back_msg = {'status': 0, 'msg': '更改失败'}
#     #     if ser.is_valid():
#     #         ser.save()
#     #         back_msg['status'] = 1
#     #         back_msg['msg'] = '数据更新成功'
#     #
#     #     return Response(back_msg)
#

class UserAPIView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # http://host:port/users/{username}/oneuser/
    @action(methods=['get'], detail=True)
    def oneuser(self, request, pk=None):
        try:
            ret = User.objects.get(username=pk)
            ser = UserSerializer(ret, many=False)
            print(ser)
            return Response(ser.data)
        except:
            return Response({'status': 0})

    # http://host:port/users/{username}/login/
    @action(methods=['post'], detail=True)
    def login(self, request,pk=None):
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            ret = User.objects.get(username=username)

            if ret.password == password:

                return Response(UserSerializer(ret,many=False).data)
            else:
                return Response({'status': 0})
        except:
            return Response({'status': 0})

    # http://host:port/users/register/
    @action(methods=['post'], detail=False)
    def register(self, request):

        # print(request.POST)
        # print(type(request.POST))
        kwargs = dict(request.POST)
        for k, v in kwargs.items():
            kwargs[k] = v[0]
        # print(request.FILES)
        kwargs['icon'] = request.FILES.get('icon')
        # print(kwargs)
        ret = User.objects.create(**kwargs)
        # return Response(UserSerializer(ret).data)
        return Response({'status':1})

    # http://host:port/users/{username}/changeinfo/
    @action(methods=['post','put'], detail=True)
    def changeinfo(self, request,pk=None):

        try:
            ret = User.objects.get(username=pk)
            ser = UserSerializer(instance=ret,data=request.data)
            if ser.is_valid():
                ser.save()
                return Response({'status':1})
            else:
                return Response({'status':0})
        except:
            return Response({'status':0})
