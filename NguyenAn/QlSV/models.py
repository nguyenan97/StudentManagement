# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Ctkhung(models.Model):
    manganh = models.ForeignKey('Nganhhoc', models.DO_NOTHING, db_column='MaNganh', primary_key=True)  # Field name made lowercase.
    mamon = models.ForeignKey('Monhoc', models.DO_NOTHING, db_column='MaMon')  # Field name made lowercase.
    hocky = models.CharField(db_column='HocKy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    batbuoc = models.CharField(db_column='BatBuoc', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ctkhung'
        unique_together = (('manganh', 'mamon'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Giangvien(models.Model):
    magv = models.IntegerField(db_column='MaGV', primary_key=True)  # Field name made lowercase.
    ho = models.CharField(db_column='Ho', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ten = models.CharField(db_column='Ten', max_length=10, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pass_field = models.CharField(db_column='pass', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.


    class Meta:
        managed = False
        db_table = 'giangvien'



class Gvphutrach(models.Model):
    magv = models.ForeignKey(Giangvien, models.DO_NOTHING, db_column='MaGV', primary_key=True, unique=True)  # Field name made lowercase.
    mamon = models.ForeignKey('Monhoc', models.DO_NOTHING, db_column='MaMon')  # Field name made lowercase.
    hockybatdau = models.ForeignKey('Hockynam', models.DO_NOTHING, db_column='HocKyBatDau', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gvphutrach'
        unique_together = (('magv', 'mamon'),)


class HistoryStore(models.Model):
    timemark = models.DateTimeField()
    table_name = models.TextField(primary_key=True)
    pk_date_src = models.TextField()
    pk_date_dest = models.TextField()
    record_state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'history_store'
        unique_together = (('table_name', 'pk_date_dest'),)


class Hockynam(models.Model):
    mahk = models.IntegerField(db_column='MaHK', primary_key=True)  # Field name made lowercase.
    namhoc = models.CharField(db_column='NamHoc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hocky = models.CharField(db_column='HocKy', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hockynam'


class Ketquahoctap(models.Model):
    masv = models.ForeignKey('Sinhvien', models.DO_NOTHING, db_column='MaSV', primary_key=True, unique=True)  # Field name made lowercase.
    mahp = models.ForeignKey('Lophocphan', models.DO_NOTHING, db_column='MaHP')  # Field name made lowercase.
    diemtk = models.FloatField(db_column='DiemTK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ketquahoctap'
        unique_together = (('masv', 'mahp'),)


class Khoahoc(models.Model):
    makhoa = models.IntegerField(db_column='MaKhoa', primary_key=True)  # Field name made lowercase.
    namvaohoc = models.CharField(db_column='NamVaoHoc', max_length=5, blank=True, null=True)  # Field name made lowercase.
    manganh = models.ForeignKey('Nganhhoc', models.DO_NOTHING, db_column='MaNganh', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'khoahoc'


class Lophocphan(models.Model):
    mahp = models.IntegerField(db_column='MaHP', primary_key=True)  # Field name made lowercase.
    mamon = models.ForeignKey('Monhoc', models.DO_NOTHING, db_column='MaMon', blank=True, null=True)  # Field name made lowercase.
    mahk = models.ForeignKey(Hockynam, models.DO_NOTHING, db_column='MaHK', blank=True, null=True)  # Field name made lowercase.
    magv = models.ForeignKey(Giangvien, models.DO_NOTHING, db_column='MaGV', blank=True, null=True)  # Field name made lowercase.
    soluongdk = models.IntegerField(db_column='SoLuongDK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lophocphan'


class Lopnienkhoa(models.Model):
    malop = models.IntegerField(db_column='MaLop', primary_key=True)  # Field name made lowercase.
    tenlop = models.CharField(db_column='TenLop', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    makhoa = models.ForeignKey(Khoahoc, models.DO_NOTHING, db_column='MaKhoa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lopnienkhoa'


class Monhoc(models.Model):
    mamon = models.IntegerField(db_column='MaMon', primary_key=True)  # Field name made lowercase.
    tenmon = models.CharField(db_column='TenMon', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    sotinchi = models.PositiveIntegerField(db_column='SoTinChi', blank=True, null=True)  # Field name made lowercase.
    monhoctruoc = models.ForeignKey('self', models.DO_NOTHING, db_column='MonHocTruoc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'monhoc'


class Nganhhoc(models.Model):
    manganh = models.IntegerField(db_column='MaNganh', primary_key=True)  # Field name made lowercase.
    tennganh = models.CharField(db_column='TenNganh', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nganhhoc'


class Sinhvien(models.Model):
    masv = models.IntegerField(db_column='MaSV', primary_key=True, unique=True)  # Field name made lowercase.
    ho = models.CharField(db_column='Ho', max_length=50)  # Field name made lowercase.
    ten = models.CharField(db_column='Ten', max_length=50)  # Field name made lowercase.
    ngaysinh = models.DateField(db_column='NgaySinh', blank=True, null=True)  # Field name made lowercase.
    gioitinh = models.CharField(db_column='GioiTinh', max_length=50, blank=True, null=True)  # Field name made lowercase.
    noisinh = models.ForeignKey('Tinhthanh', models.DO_NOTHING, db_column='NoiSinh', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=10, blank=True, null=True)  # Field name made lowercase.
    malop = models.ForeignKey(Lopnienkhoa, models.DO_NOTHING, db_column='MaLop', blank=True, null=True)  # Field name made lowercase.
    pass_field = models.CharField(db_column='pass', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'sinhvien'


class Tinhthanh(models.Model):
    matinh = models.IntegerField(db_column='MaTinh', primary_key=True)  # Field name made lowercase.
    tentinh = models.CharField(db_column='TenTinh', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tinhthanh'
