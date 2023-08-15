from .models import Sinhvien, User, Xephang
from .forms import ThemForm, SuaForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.views import View
from rest_framework import viewsets, permissions, generics
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SinhvienSerializer, UserSerializer


class TimSinhvien(APIView):
    def get(self, request):
        query_params = request.query_params
        ten_sv = query_params.get('ten_sv', '')
        
        sinhviens = Sinhvien.objects.filter(ten_sv__icontains=ten_sv)
        serializer = SinhvienSerializer(sinhviens, many=True)
        
        return Response(serializer.data)


class UserViewSet(viewsets.ViewSet, 
                  generics.ListAPIView,
                  generics.CreateAPIView,
                  generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]

    
class SinhvienViewSet(viewsets.ModelViewSet):
    queryset = Sinhvien.objects.filter(gioi_tinh='Nam')
    serializer_class = SinhvienSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
    def get_permissions(self):
        if self.action == 'list':
           return [permissions.AllowAny()]
    
        return [permissions.IsAuthenticated()]
    

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    danhsach = Sinhvien.objects.filter(
        Q(xep_hang__icontains=q) |
        Q(ten_sv__icontains=q) |
        Q(gioi_tinh__icontains=q) 
        )
    
    quanly_count = Sinhvien.objects.count()
    
    
    context = {'danhsach': danhsach,
               'quanly_count': quanly_count,
               }
    return render(request, 'home.html', context)
    

def detail(request, pk):
    chitiet = Sinhvien.objects.get(id=pk)
    context = {'chitiet': chitiet}
    return render(request, 'detail.html', context)


def them(request):
    form = ThemForm()
    if request.method == 'POST':
        form = ThemForm(request.POST)        
        
        Sinhvien.objects.create(
            ten_sv=request.POST.get('ten_sv'),
            ngay_sinh=request.POST.get('ngay_sinh'),
            gioi_tinh=request.POST.get('gioi_tinh'),
            dia_chi=request.POST.get('dia_chi'),
            diem_tb=request.POST.get('diem_tb'),
            xep_hang=request.POST.get('xep_hang'),
        )
        return redirect('home')

    context = {'form': form}
    return render(request, 'them.html', context)


def sua(request, pk):
    sua = Sinhvien.objects.get(id=pk)
    form = SuaForm(instance=sua)
    if request.method == 'POST':
        form = SuaForm(request.POST)
        
        Sinhvien.objects.filter(id=pk).update(
            ten_sv = request.POST.get('ten_sv'),
            gioi_tinh = request.POST.get('gioi_tinh'),
            dia_chi=request.POST.get('dia_chi'),
            diem_tb=request.POST.get('diem_tb'),
            xep_hang=request.POST.get('xep_hang'),
        )
        
        return redirect('home')
    
    context = {'form': form}
    return render(request,'sua.html' , context)


def xoa(request, pk):
    xoa = Sinhvien.objects.get(id=pk)
    
    if request.method == 'POST':
        xoa.delete()
        return redirect('home')
    return render(request, 'xoa.html', {'xoa': xoa})


def dangnhap(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            return render(request, 'Nguoi dung khong ton tai')

        user == authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        
        
    context = {}
    return render(request, 'dangnhap.html', context)


def dangxuat(request):
    logout(request)
    return redirect('home')
