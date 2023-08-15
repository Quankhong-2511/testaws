from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import TimSinhvien



router = DefaultRouter()
router.register('quanly', views.SinhvienViewSet)
router.register('users', views.UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/tim-sv/', TimSinhvien.as_view(), name='tim-sv'),
    
    path('dangnhap/', views.dangnhap, name='dangnhap'),
    path('dangxuat/', views.dangxuat, name='dangxuat'),
    
    path('', views.home, name='home'),
    path('detail/<str:pk>', views.detail, name='detail'),
    
    path('them/', views.them, name='them'),
    path('xoa/<str:pk>', views.xoa, name='xoa'),
    path('sua/<str:pk>', views.sua, name='sua'),

]
