from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('findpages',views.FindPageAPIView,base_name='findpage')
router.register('showpages',views.ShowPageAPIView,base_name='showpage')
router.register('bg',views.WealthBGAPIView,base_name='wealthbg')
# router.register('peom',views.WealthBGAPIView,base_name='wealthpeom')
router.register('remarks',views.RemarkAPIView,base_name='remark')
router.register('images',views.ImageAPIView,base_name='image')

app_name = 'service'
urlpatterns = [
    # path('getshowpages/', views.ShowPageAPIVIew.as_view(), name='getshowpages'),
    # path('getshowpages/<int:pk>/', views.ShowPageAPIVIew.as_view(), name='getshowpage'),
    # path('getimages/', views.ImageAPIView.as_view(), name='getimage'),
    # path('getwealthbg/', views.WealthBGAPIView.as_view(), name='getwealthbg'),
    # path('getwealthpeom', views.WealthPeomAPIView.as_view(), name='getwealthpeom')
    path('',include(router.urls))
]
