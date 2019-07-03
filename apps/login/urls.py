from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('users',views.UserAPIView,base_name='userinfo')


app_name = 'login'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    # path('users/<str:name>/',views.UserAPIView.as_view(),name='users'),
    # path('users/',views.UserAPIView.as_view(),name='user'),
    path('',include(router.urls))
]
