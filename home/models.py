from django.db import models
from django.utils import timezone


class Channel(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    crawling_url = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    subscribers = models.IntegerField()
    genre = models.CharField(max_length=200)
    thumbnail = models.CharField(max_length=4000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class CommonCode(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    code_group = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name