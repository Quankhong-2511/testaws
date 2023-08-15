from django.forms import ModelForm
from .models import Sinhvien

class ThemForm(ModelForm):
    class Meta:
        model = Sinhvien
        fields = ['ten_sv', 'ngay_sinh' ,'gioi_tinh','dia_chi', 'diem_tb','xep_hang', 'image']
        
class SuaForm(ModelForm):
    class Meta:
        model = Sinhvien
        fields = ['ten_sv', 'gioi_tinh','dia_chi', 'diem_tb', 'xep_hang']