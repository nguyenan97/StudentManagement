from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import loader
from django.http import Http404
from django.template.context_processors import csrf

from QlSV.models import *
from QlSV.templates import *
# Create your views here.
import MySQLdb
#Trang chủ
def index(request):
    return render(request, 'QlSV/home.html')
#giới thiệu
def gioiThieu(request):
    obj1 = Giangvien.objects.all()
    context1 = {'listTeacher': obj1}
    return render(request, "QlSV/gioiThieu.html", context1)
#Chi tiết giảng viên
def teacherDetail(request, maGV):
    try:
        teacher = Giangvien.objects.get(pk=maGV)
    except Giangvien.DoesNotExist:
        raise Http404("Giảng viên không tồn tại")

    return render(request,'QlSV/teacherDetail.html',{'teacherDetail':teacher})
#Sinh viên
def sv(request):
    obj = Sinhvien.objects.all()
    context = {'list':obj}
    return render(request,"QlSV/sinhVien.html")
#login xem chi tiết sinh viên
def login(request):
    listStudent = Sinhvien.objects.all()

    mssv = int(request.POST.get('txtLogin'))
    passwd = request.POST.get('txtPass')
    for x in listStudent:
        if x.masv == mssv and x.pass_field == passwd:
            diem = Ketquahoctap.objects.get(pk=int(mssv))

            return render(request,'QlSV/sinhVien.html', {'sv1': x, 'diem':diem})
    return render(request,'QlSV/sinhVien.html')
#Giảng Viên
def giangVien(request):
    obj = Giangvien.objects.all()
    content = {'list1':obj}
    return render(request, 'QlSV/GiangVien.html',content)

#login xem lịch dạy
def loginGV(request):
    list = Giangvien.objects.all()

    msgv = int(request.POST.get('txtLogin'))
    passwd = (request.POST.get('txtPass'))
    for x in list:
        if x.magv == msgv and x.pass_field == passwd:
            lop = Gvphutrach.objects.get(pk=int(msgv))
            return render(request,'QlSV/GiangVien.html', {'gv1': x,'lop':lop})
    return render(request,'QlSV/GiangVien.html')


#error 404
def error(request):
    return render(request,'QlSV/error.html')
#Chi tiết sinh viên
def detail(request, maSV):
    try:
        student = Sinhvien.objects.get(pk=maSV)
    except Sinhvien.DoesNotExist:
        raise Http404("Sinh viên không tồn tại")

    return render(request,'QlSV/detail.html',{'studentDetail':student})


#def listStudent(request):

#    db = MySQLdb.connect(user='root', db='qlsv',  passwd='12345', host='')
 #   cursor = db.cursor()

  #  cursor.execute('SELECT * FROM qlsv.sinhvien s join qlsv.ketquahoctap k')

   # name = [row[1] for row in cursor.fetchall()]
   # db.close()
    #return render(request, 'QlSV/abc.html', {'abc': name})
