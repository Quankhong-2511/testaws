from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')
    

class Diem(models.Model):
    ten_sv = models.CharField(max_length=100, null=False)
    diem_tb = models.FloatField(max_length=10)


class Xephang(models.Model):
    xep_hang = models.CharField(max_length=10, null=True)
   
    def __str__(self):
        return self.xep_hang
   
   
class Sinhvien(models.Model):
    ten_sv = models.CharField(max_length=100, null=False)
    ngay_sinh = models.DateField(null=True)
    gioi_tinh = models.CharField(max_length=10, null=True)
    dia_chi = models.CharField(max_length=100, null=True)
    diem_tb = models.FloatField(max_length=10, null=True)
    xep_hang = models.CharField(max_length=10, null=True)
    image = models.ImageField(upload_to='qlsv/%Y/%m', default=None)
    
    def __str__(self):
        return self.ten_sv