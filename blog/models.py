from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
