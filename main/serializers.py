from rest_framework import serializers
from .models import TelegramUsers, User, UserCourse, Course


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('telegram_id', 'name', 'phone')


class TelegramUsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = TelegramUsers
        fields = ('telegram_id',)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('title', 'description', 'image_path')


class UserCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = ('course', 'user')



