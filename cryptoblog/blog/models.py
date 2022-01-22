from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


def name_file(instance, filename):
    return '/'.join(['images', str(instance.id), filename])


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(
        'Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(max_length=150)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to=name_file, blank=True, null=True)
    categories = models.ManyToManyField(Category)
    activate = models.BooleanField()

    def __str__(self):
        return self.title


class ImagePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=name_file, blank=True, null=True)

    def __str__(self):
        return self.post.title
