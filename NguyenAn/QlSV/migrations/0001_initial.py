# Generated by Django 2.0.4 on 2018-04-24 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Giangvien',
            fields=[
                ('magv', models.IntegerField(db_column='MaGV', primary_key=True, serialize=False)),
                ('ho', models.CharField(blank=True, db_column='Ho', max_length=50, null=True)),
                ('ten', models.CharField(blank=True, db_column='Ten', max_length=10, null=True)),
                ('phone', models.CharField(blank=True, db_column='Phone', max_length=10, null=True)),
                ('pass_field', models.CharField(blank=True, db_column='pass', max_length=50, null=True)),
                ('imgage', models.ImageField(null=True, upload_to='')),
            ],
            options={
                'db_table': 'giangvien',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HistoryStore',
            fields=[
                ('timemark', models.DateTimeField()),
                ('table_name', models.TextField(primary_key=True, serialize=False)),
                ('pk_date_src', models.TextField()),
                ('pk_date_dest', models.TextField()),
                ('record_state', models.IntegerField()),
            ],
            options={
                'db_table': 'history_store',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hockynam',
            fields=[
                ('mahk', models.IntegerField(db_column='MaHK', primary_key=True, serialize=False)),
                ('namhoc', models.CharField(blank=True, db_column='NamHoc', max_length=50, null=True)),
                ('hocky', models.CharField(blank=True, db_column='HocKy', max_length=1, null=True)),
            ],
            options={
                'db_table': 'hockynam',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Khoahoc',
            fields=[
                ('makhoa', models.IntegerField(db_column='MaKhoa', primary_key=True, serialize=False)),
                ('namvaohoc', models.CharField(blank=True, db_column='NamVaoHoc', max_length=5, null=True)),
            ],
            options={
                'db_table': 'khoahoc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lophocphan',
            fields=[
                ('mahp', models.IntegerField(db_column='MaHP', primary_key=True, serialize=False)),
                ('soluongdk', models.IntegerField(blank=True, db_column='SoLuongDK', null=True)),
            ],
            options={
                'db_table': 'lophocphan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lopnienkhoa',
            fields=[
                ('malop', models.IntegerField(db_column='MaLop', primary_key=True, serialize=False)),
                ('tenlop', models.CharField(blank=True, db_column='TenLop', max_length=50, null=True, unique=True)),
            ],
            options={
                'db_table': 'lopnienkhoa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Monhoc',
            fields=[
                ('mamon', models.IntegerField(db_column='MaMon', primary_key=True, serialize=False)),
                ('tenmon', models.CharField(blank=True, db_column='TenMon', max_length=50, null=True, unique=True)),
                ('sotinchi', models.PositiveIntegerField(blank=True, db_column='SoTinChi', null=True)),
            ],
            options={
                'db_table': 'monhoc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nganhhoc',
            fields=[
                ('manganh', models.IntegerField(db_column='MaNganh', primary_key=True, serialize=False)),
                ('tennganh', models.CharField(blank=True, db_column='TenNganh', max_length=50, null=True, unique=True)),
            ],
            options={
                'db_table': 'nganhhoc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sinhvien',
            fields=[
                ('masv', models.IntegerField(db_column='MaSV', primary_key=True, serialize=False, unique=True)),
                ('ho', models.CharField(db_column='Ho', max_length=50)),
                ('ten', models.CharField(db_column='Ten', max_length=50)),
                ('ngaysinh', models.DateField(blank=True, db_column='NgaySinh', null=True)),
                ('gioitinh', models.CharField(blank=True, db_column='GioiTinh', max_length=50, null=True)),
                ('phone', models.CharField(blank=True, db_column='Phone', max_length=10, null=True)),
                ('pass_field', models.CharField(blank=True, db_column='pass', max_length=50, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
            options={
                'db_table': 'sinhvien',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tinhthanh',
            fields=[
                ('matinh', models.IntegerField(db_column='MaTinh', primary_key=True, serialize=False)),
                ('tentinh', models.CharField(blank=True, db_column='TenTinh', max_length=50, null=True, unique=True)),
            ],
            options={
                'db_table': 'tinhthanh',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ctkhung',
            fields=[
                ('manganh', models.ForeignKey(db_column='MaNganh', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='QlSV.Nganhhoc', unique=True)),
                ('hocky', models.CharField(blank=True, db_column='HocKy', max_length=10, null=True)),
                ('batbuoc', models.CharField(blank=True, db_column='BatBuoc', max_length=50, null=True)),
            ],
            options={
                'db_table': 'ctkhung',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gvphutrach',
            fields=[
                ('magv', models.ForeignKey(db_column='MaGV', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='QlSV.Giangvien', unique=True)),
            ],
            options={
                'db_table': 'gvphutrach',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ketquahoctap',
            fields=[
                ('masv', models.ForeignKey(db_column='MaSV', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='QlSV.Sinhvien', unique=True)),
                ('diemtk', models.FloatField(blank=True, db_column='DiemTK', null=True)),
            ],
            options={
                'db_table': 'ketquahoctap',
                'managed': False,
            },
        ),
    ]
