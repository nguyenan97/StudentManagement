from django.contrib import admin
from .models import Giangvien, Sinhvien, Ctkhung, Gvphutrach, Hockynam, Ketquahoctap, Khoahoc, Nganhhoc, Monhoc, Lopnienkhoa, Lophocphan, Tinhthanh
# Register your models here.


class MenuSV(admin.ModelAdmin):
    list_display = ['masv','ho','ten','ngaysinh','gioitinh','phone']
    list_filter = ['malop']
    search_fields = ['masv','ho','ten','gioitinh']
class MenuGV(admin.ModelAdmin):
    list_display = ['magv','ho','ten','phone']
    list_filter = ['magv']
    search_fields = ['magv','ho','ten','phone']
class MenuCtkhung(admin.ModelAdmin):
    list_display = ['manganh','mamon','hocky','batbuoc']
    list_filter = ['manganh']
    search_fields = ['manganh','mamon','hocky','batbuoc']

class MenuGVPhuTrach(admin.ModelAdmin):
    list_display = ['mamon','hockybatdau']
    list_filter = ['magv']
    search_fields = ['magv','mamon','hockybatdau']
class MenuHocKiNam(admin.ModelAdmin):
    list_display = ['namhoc','hocky']
    list_filter = ['mahk']
    search_fields = ['mahk','namhoc','hocky']
class MenuKQHT(admin.ModelAdmin):
    list_display = ['masv','mahp','diemtk']
    list_filter = ['masv']
    search_fields = ['masv','mahp','diemtk']
class MenuKhoaHoc(admin.ModelAdmin):
    list_display = ['namvaohoc','manganh']
    list_filter = ['makhoa']
    search_fields = ['makhoa','namvaohoc','manganh']
class MenuNganhHoc(admin.ModelAdmin):
    list_display = ['manganh','tennganh']
    list_filter = ['manganh']
    search_fields = ['manganh','tennganh']

class MenuMonHoc(admin.ModelAdmin):
    list_display = ['tenmon','sotinchi','monhoctruoc']
    list_filter = ['mamon']
    search_fields = ['mamon','tenmon','sotinchi','monhoctruoc']

class MenuLopNienKhoa(admin.ModelAdmin):
    list_display = ['tenlop','makhoa']
    list_filter = ['malop']
    search_fields = ['malop','tenlop','makhoa']

class MenuLopHP(admin.ModelAdmin):
    list_display = ['mahp','mamon','soluongdk']
    list_filter = ['magv']
    search_fields = ['mahp','mamon','soluongdk']
class MenuTinhThanh(admin.ModelAdmin):
    list_display = ['tentinh']
    list_filter = ['matinh']
    search_fields = ['matinh','tentinh']
admin.site.register(Giangvien,MenuGV)
admin.site.register(Sinhvien,MenuSV)
admin.site.register(Ctkhung,MenuCtkhung)
admin.site.register(Gvphutrach,MenuGVPhuTrach)
admin.site.register(Hockynam,MenuHocKiNam)
admin.site.register(Ketquahoctap,MenuKQHT)
admin.site.register(Khoahoc,MenuKhoaHoc)
admin.site.register(Nganhhoc,MenuNganhHoc)
admin.site.register(Monhoc,MenuMonHoc)
admin.site.register(Lopnienkhoa,MenuLopNienKhoa)
admin.site.register(Lophocphan,MenuLopHP)
admin.site.register(Tinhthanh,MenuTinhThanh)