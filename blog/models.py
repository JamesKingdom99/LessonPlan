from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from markdown import markdown


# Create your models here.


class PostForms(models.Model):
    title = models.CharField(max_length = 140)
    name = models.ForeignKey(User, related_name='blogger',  on_delete=models.CASCADE)
    ls = models.TextField()
    question = models.TextField()
    presentation = models.TextField()
    background = models.TextField()
    perfTask = models.TextField()
    quiz = models.TextField()
    vocab = models.TextField()
    wiki = models.TextField()

    def __str__(self):
        return self.title

    def get_perfTask_as_markdown(self):
        return mark_safe(markdown(self.perfTask, safe_mode='escape'))

    def get_background_as_markdown(self):
        return mark_safe(markdown(self.background, safe_mode='escape'))
