from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    # name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username'
    ]


class Tag(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Tag'

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=10000)
    tags = models.ManyToManyField(Tag, related_name='posts')
    editor = models.ForeignKey(User, related_name='posts', on_delete=models.SET_NULL, null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Post'

    def __str__(self):
        return self.title
