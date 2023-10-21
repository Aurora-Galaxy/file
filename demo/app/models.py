from django.db import models


# 用户信息
class User(models.Model):
    user_id = models.AutoField(primary_key=True, verbose_name='用户 id')
    username = models.CharField(max_length=100, default='', verbose_name='用户名')
    password = models.CharField(max_length=32, default='', verbose_name='密码')
    given_name = models.CharField(max_length=50, default='', verbose_name='姓名')
    mobile = models.CharField(max_length=13, default='', verbose_name='手机号')
    phone = models.CharField(max_length=13, default='', verbose_name='电话')
    email = models.EmailField(max_length=50, default='', verbose_name='邮箱')
    department = models.CharField(max_length=50, default='', verbose_name='部门')
    position = models.CharField(max_length=50, default='', verbose_name='职位')
    location = models.CharField(max_length=50, default='', verbose_name='位置')
    # im = models.CharField(max_length=50, default='', verbose_name='即时聊天工具')
    # last_ip = models.CharField(max_length=15, default='', verbose_name='最后登录ip')
    # last_time = models.IntegerField(default=0, verbose_name='最后登录时间')
    role_id = models.SmallIntegerField(default=0, verbose_name='角色 id')
    is_forbidden = models.BooleanField(default=False, verbose_name='是否屏蔽')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    create_time = models.IntegerField(default=0, verbose_name='创建时间')
    update_time = models.IntegerField(default=0, verbose_name='更新时间')


# 系统角色表
class UserRole(models.Model):
    role_id = models.AutoField(primary_key=True, verbose_name='角色 id')
    name = models.CharField(max_length=10, default='', verbose_name='角色名称')
    type = models.SmallIntegerField(default=0, verbose_name='角色类型')  # 0 自定义角色，1 系统角色 使用 SmallIntegerField 表示 tinyint(3)
    is_delete = models.BooleanField(default=False, verbose_name='是否删除') # 0 否 1 是
    create_time = models.PositiveIntegerField(default=0,verbose_name='创建时间')  # 使用 PositiveIntegerField 表示 int(10) unsigned
    update_time = models.PositiveIntegerField(default=0, verbose_name='更新时间')

# 系统权限表
class Privilege(models.Model):
    PRIVILEGE_TYPE_CHOICES = [
        ('controller', '控制器'),
        ('menu', '菜单'),
    ]
    privilege_id = models.AutoField(primary_key=True, verbose_name='权限id')
    name = models.CharField(max_length=30, default='', verbose_name='权限名')
    parent_id = models.PositiveIntegerField(default=0, verbose_name='上级')  # 使用 PositiveIntegerField 表示 int(10) unsigned
    type = models.CharField(max_length=10, choices=PRIVILEGE_TYPE_CHOICES, default='controller', verbose_name='权限类型') #指定控制器或者菜单
    controller = models.CharField(max_length=100, default='', verbose_name='控制器')
    action = models.CharField(max_length=100, default='', verbose_name='动作')
    icon = models.CharField(max_length=100, default='', verbose_name='图标（用于展示)') #0不显示 1显示
    target = models.CharField(max_length=200, default='', verbose_name='目标地址')
    is_display = models.BooleanField(default=False, verbose_name='是否显示')
    sequence = models.PositiveIntegerField(default=0, verbose_name='排序(越小越靠前)')
    create_time = models.PositiveIntegerField(default=0, verbose_name='创建时间')  # 使用 PositiveIntegerField 表示 int(10) unsigned
    update_time = models.PositiveIntegerField(default=0, verbose_name='更新时间')

# 系统角色权限对应关系表
class RolePrivilege(models.Model):
    role_privilege_id = models.AutoField(primary_key=True, verbose_name='角色权限关系 id')
    role_id = models.PositiveIntegerField(default=0, verbose_name='角色id')
    privilege_id = models.PositiveIntegerField(default=0, verbose_name='权限id')
    create_time = models.PositiveIntegerField(default=0, verbose_name='创建时间')

#空间表
class Space(models.Model):
    VISIT_LEVEL_CHOICES = [
        ('private', '私有'),
        ('public', '公开'),
    ]
    space_id = models.PositiveIntegerField(primary_key=True, verbose_name='空间 id')
    name = models.CharField(max_length=50, default='', verbose_name='名称')
    description = models.CharField(max_length=100, default='', verbose_name='描述')
    tags = models.CharField(max_length=255, default='', verbose_name='标签')
    visit_level = models.CharField(max_length=10, choices=VISIT_LEVEL_CHOICES, default='public', verbose_name='访问级别')
    is_share = models.BooleanField(default=True, verbose_name='文档是否允许分享')  # 文档是否允许分享 0 否 1 是
    is_export = models.BooleanField(default=True, verbose_name='文档是否允许导出') # 文档是否允许导出 0 否 1 是
    is_delete = models.BooleanField(default=False, verbose_name='是否删除') # 是否删除 0 否 1 是
    create_time = models.PositiveIntegerField(default=0, verbose_name='创建时间')
    update_time = models.PositiveIntegerField(default=0, verbose_name='更新时间')


# 空间成员表
class SpaceUser(models.Model):
    PRIVILEGE_CHOICES = [
        (0, '浏览者'),
        (1, '编辑者'),
        (2, '管理员'),
    ]

    space_user_id = models.PositiveIntegerField(primary_key=True, verbose_name='用户空间关系 id')
    user_id = models.PositiveIntegerField(default=0, verbose_name='用户 id')
    space_id = models.PositiveIntegerField(default=0, verbose_name='空间 id')
    privilege = models.SmallIntegerField(choices=PRIVILEGE_CHOICES, default=0, verbose_name='空间成员操作权限')
    create_time = models.PositiveIntegerField(default=0, verbose_name='创建时间')
    update_time = models.PositiveIntegerField(default=0, verbose_name='修改时间')

# 文档表
class Document(models.Model):
    TYPE_CHOICES = [
        (1, 'Page'),
        (2, 'Directory'),
    ]
    document_id = models.PositiveIntegerField(primary_key=True, verbose_name='文档 id')
    parent_id = models.PositiveIntegerField(default=0, verbose_name='文档父 id')
    space_id = models.PositiveIntegerField(default=0, verbose_name='空间 id')
    name = models.CharField(max_length=150, default='', verbose_name='文档名称')
    type = models.SmallIntegerField(choices=TYPE_CHOICES, default=1, verbose_name='文档类型')
    path = models.CharField(max_length=30, default='0', verbose_name='存储根文档到父文档的 document_id 值, 格式 0,1,2,...')
    sequence = models.PositiveIntegerField(default=0, verbose_name='排序号(越小越靠前)')
    create_user_id = models.PositiveIntegerField(default=0, verbose_name='创建用户 id')
    edit_user_id = models.PositiveIntegerField(default=0, verbose_name='最后修改用户 id')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    create_time = models.PositiveIntegerField(default=0, verbose_name='创建时间')
    update_time = models.PositiveIntegerField(default=0, verbose_name='更新时间')



# 文档日志表
class LogDocument(models.Model):
    ACTION_CHOICES = [
        (1, '创建'),
        (2, '修改'),
        (3, '删除'),
    ]

    log_document_id = models.AutoField(primary_key=True, verbose_name='文档日志 id')
    document_id = models.PositiveIntegerField(default=0, verbose_name='文档id')
    space_id = models.PositiveIntegerField(default=0, verbose_name='空间id')
    user_id = models.PositiveIntegerField(default=0, verbose_name='用户id')
    action = models.SmallIntegerField(choices=ACTION_CHOICES, default=1, verbose_name='动作') # 1 创建 2 修改 3 删除
    comment = models.CharField(max_length=255, default='', verbose_name='备注信息')
    create_time = models.PositiveIntegerField(default=0, verbose_name='创建时间')

# 系统操作日志表
class Log(models.Model):
    LEVEL_CHOICES = [
        (1, 'DEBUG'),
        (2, 'INFO'),
        (3, 'WARNING'),
        (4, 'ERROR'),
        (5, 'CRITICAL'),
        (6, 'DEFAULT'),
    ]

    log_id = models.BigAutoField(primary_key=True, verbose_name='系统操作日志 id')
    level = models.SmallIntegerField(choices=LEVEL_CHOICES, default=6, verbose_name='日志级别')
    path = models.CharField(max_length=100, default='', verbose_name='请求路径')
    get = models.TextField(verbose_name='get参数')
    post = models.TextField(verbose_name='post参数')
    message = models.CharField(max_length=255, default='', verbose_name='信息')
    ip = models.CharField(max_length=100, default='', verbose_name='ip地址')
    user_agent = models.CharField(max_length=200, default='', verbose_name='用户代理')
    referer = models.CharField(max_length=100, default='', verbose_name='referer')
    user_id = models.PositiveIntegerField(default=0, verbose_name='用户id')
    username = models.CharField(max_length=100, default='', verbose_name='用户名')
    create_time = models.PositiveIntegerField(default=0, verbose_name='创建时间')

# 统一认证表
class LoginAuth(models.Model):
    login_auth_id = models.AutoField(primary_key=True, verbose_name='认证表主键ID')
    name = models.CharField(max_length=30, verbose_name='登录认证名称')
    username_prefix = models.CharField(max_length=30, verbose_name='用户名前缀')
    url = models.CharField(max_length=200, verbose_name='认证接口 url')
    ext_data = models.CharField(max_length=500, default='', verbose_name='额外数据: token=aaa&key=bbb')
    is_used = models.BooleanField(default=False, verbose_name='是否被使用')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    create_time = models.IntegerField(verbose_name='创建时间')
    update_time = models.IntegerField(verbose_name='更新时间')

# 全局配置表
class Config(models.Model):
    config_id = models.AutoField(primary_key=True, verbose_name='配置表主键Id')
    name = models.CharField(max_length=100, default='', verbose_name='配置名称')
    key = models.CharField(max_length=50, unique=True, default='', verbose_name='配置键')
    value = models.TextField(verbose_name='配置值')
    create_time = models.IntegerField(default=0, verbose_name='创建时间')
    update_time = models.IntegerField(default=0, verbose_name='更新时间')


# 联系人表
class Contact(models.Model):
    contact_id = models.PositiveIntegerField(primary_key=True, verbose_name='联系人 id')
    name = models.CharField(max_length=50, default='', verbose_name='联系人名称')
    mobile = models.CharField(max_length=13, default='', verbose_name='联系电话')
    email = models.CharField(max_length=50, default='', verbose_name='邮箱')
    position = models.CharField(max_length=100, default='', verbose_name='联系人职位')
    create_time = models.PositiveIntegerField(default=0, verbose_name='创建时间')
    update_time = models.PositiveIntegerField(default=0, verbose_name='更新时间')


# # 文件
# class File(models.Model):
#     id = models.AutoField(primary_key=True)
#     file_name = models.CharField(max_length=255)  # 文件名称
#     # file_content = models.CharField(max_length=255)
#     user_id = models.IntegerField(max_length=10)  # 文档作者
#     file_url = models.CharField(max_length=255)  # 文件保存路径，初步打算使用github
#     file_group_id = models.IntegerField(max_length=10)  # 文件所属组
#
#
# # 文集
# class FileSet(models.Model):
#     id = models.AutoField(primary_key=True)
#     file_set_auth = models.IntegerField(max_length=10)  # 设置文集权限
#     file_set_name = models.CharField(max_length=255)  # 文集名称
