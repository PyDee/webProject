# -*- coding: utf-8 -*-
""" 
@Time : 2020/11/16 14:51
@Author : PyDee
@File : adminx.py
@description : users app的models注册
"""

import xadmin
from .models import EmailVerifyRecord, Banner


class EmailVerifyRecordAdmin(object):
    # 显示的列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['code', 'email', 'send_type']
    # 过滤
    list_filter = ['code', 'email', 'send_type', 'send_time']
    pass


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


from xadmin import views


# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


# 全局修改，固定写法
class GlobalSettings(object):
    # 修改title
    site_title = 'NBA后台管理界面'
    # 修改footer
    site_footer = '科比的公司'
    # 收起菜单
    menu_style = 'accordion'


# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView, GlobalSettings)

# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
