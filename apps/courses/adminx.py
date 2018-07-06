# encoding: utf-8
__author__ = 'test_huang'
__date__ = '2018/7/6 16:00'
from .models import Course, Lesson, Video, CourseResource
import xadmin
from xadmin import views
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True
# Register your models here.
class CourseAdmin(object):
    list_display = [
        'name',
        'desc',
        'detail',
        'degree',
        'learn_times',
        'students']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = [
        'name',
        'desc',
        'detail',
        'degree',
        'learn_times',
        'students']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']

    # __name代表使用外键中name字段
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']

class GlobalSettings(object):
    site_title = "黄成威流弊"
    site_footer = "over"
    # 收起菜单
    menu_style = "accordion"


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    # __name代表使用外键中name字段
    list_filter = ['course__name', 'name', 'download', 'add_time']



# 将管理器与model进行注册关联
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)


def __str__(self):
    return '《{0}》课程的章节 >> {1}'.format(self.course, self.name)