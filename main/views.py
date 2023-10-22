from django.shortcuts import render
from rest_framework import views, response, status
from .models import User, TelegramUsers, Course, UserCourse, About
from .serializers import UserSerializer, CourseSerializer


class TelegramUsersApi(views.APIView):

    def post(self, request, *args, **kwargs):
        TelegramUsers.objects.create(telegram_id=self.request.data.get('telegram_id'))
        return response.Response(status=status.HTTP_201_CREATED)


class UserApi(views.APIView):

    def post(self, request, *args, **kwargs):
        # User.objects.create(telegram_id=self.request.data.get('telegram_id'), name=self.request.data.get('name'),
        #                     phone=self.request.data.get('phone'))
        serializer = UserSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)

    # def get(self, request, *args, **kwargs):
    #     User.objects.filter('telegram')


class CourseApi(views.APIView):
    def get(self, request, *args, **kwargs):
        qs = Course.objects.all()
        serializer = CourseSerializer(qs, many=True)
        return response.Response(serializer.data)

    def post(self, request, *args, **kwargs):
        obj = Course.objects.filter(title__exact=self.request.query_params.get('title')).first()
        return response.Response({'description': obj.description, 'image_path': obj.image_path})


class AboutApi(views.APIView):
    def get(self, request, *args, **kwargs):
        qs = About.objects.first()
        return response.Response({'image': qs.image.path, 'phone': qs.phone, 'description': qs.description})

