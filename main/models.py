from django.db import models


class User(models.Model):
    telegram_id = models.CharField(max_length=221, unique=True)
    name = models.CharField(max_length=221)
    phone = models.CharField(max_length=221)

    def __str__(self):
        return self.telegram_id


class TelegramUsers(models.Model):
    telegram_id = models.CharField(max_length=221)

    def __str__(self):
        return self.telegram_id


class Course(models.Model):
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='images')
    description = models.TextField()

    def __str__(self):
        return self.title

    @property
    def image_path(self):
        return self.image.path


class UserCourse(models.Model):
    course = models.ForeignKey(Course, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.course}"


class About(models.Model):
    image = models.ImageField(upload_to='images')
    phone = models.CharField(max_length=255)
    description = models.TextField()

    @property
    def image_path(self):
        return self.image.path
