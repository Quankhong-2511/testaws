from django.contrib import admin
from django.contrib.auth.models import Permission
from django.utils.html import mark_safe
from .models import Sinhvien, Xephang, Diem, User


class SinhvienAdmin(admin.ModelAdmin):
    list_display = ['ten_sv', 'ngay_sinh', 'gioi_tinh', 'dia_chi', 'diem_tb', 'xep_hang']
    search_fields = ['ten_sv']
    list_filter =  ['gioi_tinh', 'xep_hang']
    readonly_fields = ['avatar']

    def avatar(self, Sinhvien):
        return mark_safe("<img src='/static/{img_url}' alt='{alt}' />".format(img_url=Sinhvien.image.name, alt=Sinhvien.ten_sv))

class QuanlyAppAdminSite(admin.AdminSite):
    site_header = 'HỆ THỐNG QUẢN LÝ SINH VIÊN'
    
#admin_site = QuanlyAppAdminSite('quanly')


admin.site.register(Sinhvien, SinhvienAdmin)
admin.site.register(Xephang)
admin.site.register(Diem)
admin.site.register(User)
admin.site.register(Permission)



#admin_site.register(Sinhvien, SinhvienAdmin)
#admin_site.register(Xephang)
#admin_site.register(Diem)
