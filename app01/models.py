from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django_comments.models import Comment


class Bbs(models.Model):
    category = models.ForeignKey('Category')
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256, blank=True,null=True)
    content = models.TextField()
    author = models.ForeignKey('BBS_user')
    view_count = models.IntegerField()
    ranking = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=32,unique=True)
    administrator = models.ForeignKey('BBS_user')

    def __unicode__(self):
        return self.name

class User_Comment(Comment):
    title = models.CharField(max_length=128)

class BBS_user(models.Model):
    user = models.OneToOneField(User)
    signature = models.CharField(max_length = 128, default='This guy is too lazy to leave anything.')
    #photo = models.ImageField()
    #models.ImageField(upload_to="upload_img/", default="upload_img/user_01.jpg")

    def __unicode__(self):
        return self.user.username
