from django.contrib import admin
from .models import User, TelegramUsers, Course, UserCourse, About


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('telegram_id', 'name', 'phone')


@admin.register(TelegramUsers)
class TelegramUsersAdmin(admin.ModelAdmin):
    list_display = ('telegram_id',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description')


#
# @admin.register(UserCourse)
# class UserCourseAdmin(admin.ModelAdmin):
#     list_display = ('course', 'user')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('phone', 'image', 'description')
