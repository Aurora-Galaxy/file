# Generated by Django 4.1 on 2023-10-21 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('config_id', models.AutoField(primary_key=True, serialize=False, verbose_name='配置表主键Id')),
                ('name', models.CharField(default='', max_length=100, verbose_name='配置名称')),
                ('key', models.CharField(default='', max_length=50, unique=True, verbose_name='配置键')),
                ('value', models.TextField(verbose_name='配置值')),
                ('create_time', models.IntegerField(default=0, verbose_name='创建时间')),
                ('update_time', models.IntegerField(default=0, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='联系人 id')),
                ('name', models.CharField(default='', max_length=50, verbose_name='联系人名称')),
                ('mobile', models.CharField(default='', max_length=13, verbose_name='联系电话')),
                ('email', models.CharField(default='', max_length=50, verbose_name='邮箱')),
                ('position', models.CharField(default='', max_length=100, verbose_name='联系人职位')),
                ('create_time', models.PositiveIntegerField(default=0, verbose_name='创建时间')),
                ('update_time', models.PositiveIntegerField(default=0, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('document_id', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='文档 id')),
                ('parent_id', models.PositiveIntegerField(default=0, verbose_name='文档父 id')),
                ('space_id', models.PositiveIntegerField(default=0, verbose_name='空间 id')),
                ('name', models.CharField(default='', max_length=150, verbose_name='文档名称')),
                ('type', models.SmallIntegerField(choices=[(1, 'Page'), (2, 'Directory')], default=1, verbose_name='文档类型')),
                ('path', models.CharField(default='0', max_length=30, verbose_name='存储根文档到父文档的 document_id 值, 格式 0,1,2,...')),
                ('sequence', models.PositiveIntegerField(default=0, verbose_name='排序号(越小越靠前)')),
                ('create_user_id', models.PositiveIntegerField(default=0, verbose_name='创建用户 id')),
                ('edit_user_id', models.PositiveIntegerField(default=0, verbose_name='最后修改用户 id')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.PositiveIntegerField(default=0, verbose_name='创建时间')),
                ('update_time', models.PositiveIntegerField(default=0, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('log_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='系统操作日志 id')),
                ('level', models.SmallIntegerField(choices=[(1, 'DEBUG'), (2, 'INFO'), (3, 'WARNING'), (4, 'ERROR'), (5, 'CRITICAL'), (6, 'DEFAULT')], default=6, verbose_name='日志级别')),
                ('path', models.CharField(default='', max_length=100, verbose_name='请求路径')),
                ('get', models.TextField(verbose_name='get参数')),
                ('post', models.TextField(verbose_name='post参数')),
                ('message', models.CharField(default='', max_length=255, verbose_name='信息')),
                ('ip', models.CharField(default='', max_length=100, verbose_name='ip地址')),
                ('user_agent', models.CharField(default='', max_length=200, verbose_name='用户代理')),
                ('referer', models.CharField(default='', max_length=100, verbose_name='referer')),
                ('user_id', models.PositiveIntegerField(default=0, verbose_name='用户id')),
                ('username', models.CharField(default='', max_length=100, verbose_name='用户名')),
                ('create_time', models.PositiveIntegerField(default=0, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='LogDocument',
            fields=[
                ('log_document_id', models.AutoField(primary_key=True, serialize=False, verbose_name='文档日志 id')),
                ('document_id', models.PositiveIntegerField(default=0, verbose_name='文档id')),
                ('space_id', models.PositiveIntegerField(default=0, verbose_name='空间id')),
                ('user_id', models.PositiveIntegerField(default=0, verbose_name='用户id')),
                ('action', models.SmallIntegerField(choices=[(1, '创建'), (2, '修改'), (3, '删除')], default=1, verbose_name='动作')),
                ('comment', models.CharField(default='', max_length=255, verbose_name='备注信息')),
                ('create_time', models.PositiveIntegerField(default=0, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='LoginAuth',
            fields=[
                ('login_auth_id', models.AutoField(primary_key=True, serialize=False, verbose_name='认证表主键ID')),
                ('name', models.CharField(max_length=30, verbose_name='登录认证名称')),
                ('username_prefix', models.CharField(max_length=30, verbose_name='用户名前缀')),
                ('url', models.CharField(max_length=200, verbose_name='认证接口 url')),
                ('ext_data', models.CharField(default='', max_length=500, verbose_name='额外数据: token=aaa&key=bbb')),
                ('is_used', models.BooleanField(default=False, verbose_name='是否被使用')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.IntegerField(verbose_name='创建时间')),
                ('update_time', models.IntegerField(verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='Privilege',
            fields=[
                ('privilege_id', models.AutoField(primary_key=True, serialize=False, verbose_name='权限id')),
                ('name', models.CharField(default='', max_length=30, verbose_name='权限名')),
                ('parent_id', models.PositiveIntegerField(default=0, verbose_name='上级')),
                ('type', models.CharField(choices=[('controller', '控制器'), ('menu', '菜单')], default='controller', max_length=10, verbose_name='权限类型')),
                ('controller', models.CharField(default='', max_length=100, verbose_name='控制器')),
                ('action', models.CharField(default='', max_length=100, verbose_name='动作')),
                ('icon', models.CharField(default='', max_length=100, verbose_name='图标（用于展示)')),
                ('target', models.CharField(default='', max_length=200, verbose_name='目标地址')),
                ('is_display', models.BooleanField(default=False, verbose_name='是否显示')),
                ('sequence', models.PositiveIntegerField(default=0, verbose_name='排序(越小越靠前)')),
                ('create_time', models.PositiveIntegerField(default=0, verbose_name='创建时间')),
                ('update_time', models.PositiveIntegerField(default=0, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='RolePrivilege',
            fields=[
                ('role_privilege_id', models.AutoField(primary_key=True, serialize=False, verbose_name='角色权限关系 id')),
                ('role_id', models.PositiveIntegerField(default=0, verbose_name='角色id')),
                ('privilege_id', models.PositiveIntegerField(default=0, verbose_name='权限id')),
                ('create_time', models.PositiveIntegerField(default=0, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='Space',
            fields=[
                ('space_id', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='空间 id')),
                ('name', models.CharField(default='', max_length=50, verbose_name='名称')),
                ('description', models.CharField(default='', max_length=100, verbose_name='描述')),
                ('tags', models.CharField(default='', max_length=255, verbose_name='标签')),
                ('visit_level', models.CharField(choices=[('private', '私有'), ('public', '公开')], default='public', max_length=10, verbose_name='访问级别')),
                ('is_share', models.BooleanField(default=True, verbose_name='文档是否允许分享')),
                ('is_export', models.BooleanField(default=True, verbose_name='文档是否允许导出')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.PositiveIntegerField(default=0, verbose_name='创建时间')),
                ('update_time', models.PositiveIntegerField(default=0, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='SpaceUser',
            fields=[
                ('space_user_id', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='用户空间关系 id')),
                ('user_id', models.PositiveIntegerField(default=0, verbose_name='用户 id')),
                ('space_id', models.PositiveIntegerField(default=0, verbose_name='空间 id')),
                ('privilege', models.SmallIntegerField(choices=[(0, '浏览者'), (1, '编辑者'), (2, '管理员')], default=0, verbose_name='空间成员操作权限')),
                ('create_time', models.PositiveIntegerField(default=0, verbose_name='创建时间')),
                ('update_time', models.PositiveIntegerField(default=0, verbose_name='修改时间')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, verbose_name='用户 id')),
                ('username', models.CharField(default='', max_length=100, verbose_name='用户名')),
                ('password', models.CharField(default='', max_length=32, verbose_name='密码')),
                ('given_name', models.CharField(default='', max_length=50, verbose_name='姓名')),
                ('mobile', models.CharField(default='', max_length=13, verbose_name='手机号')),
                ('phone', models.CharField(default='', max_length=13, verbose_name='电话')),
                ('email', models.EmailField(default='', max_length=50, verbose_name='邮箱')),
                ('department', models.CharField(default='', max_length=50, verbose_name='部门')),
                ('position', models.CharField(default='', max_length=50, verbose_name='职位')),
                ('location', models.CharField(default='', max_length=50, verbose_name='位置')),
                ('role_id', models.SmallIntegerField(default=0, verbose_name='角色 id')),
                ('is_forbidden', models.BooleanField(default=False, verbose_name='是否屏蔽')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.IntegerField(default=0, verbose_name='创建时间')),
                ('update_time', models.IntegerField(default=0, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False, verbose_name='角色 id')),
                ('name', models.CharField(default='', max_length=10, verbose_name='角色名称')),
                ('type', models.SmallIntegerField(default=0, verbose_name='角色类型')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.PositiveIntegerField(default=0, verbose_name='创建时间')),
                ('update_time', models.PositiveIntegerField(default=0, verbose_name='更新时间')),
            ],
        ),
    ]