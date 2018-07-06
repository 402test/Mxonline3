# encoding: utf-8
__author__ = 'test_huang'
__date__ = '2018/7/5 20:35'
import xadmin

from .models import EmailVerifyRecord
from .models import Banner
# 创建admin的管理类,这里不再是继承admin，而是继承object
class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']
# 创建banner的管理类
class BannerAdmin(object):
    list_display = ['title', 'image', 'url','index', 'add_time']
    search_fields = ['title', 'image', 'url','index']
    list_filter = ['title', 'image', 'url','index', 'add_time']

xadmin.site.register(Banner, BannerAdmin)

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)