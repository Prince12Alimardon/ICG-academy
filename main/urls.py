from django.urls import path
from .views import *
urlpatterns = [
    path('telegram-users/', TelegramUsersApi.as_view()),
    path('courses/', CourseApi.as_view()),
    path('user-create/', UserApi.as_view()),
    path('about/', AboutApi.as_view())
]