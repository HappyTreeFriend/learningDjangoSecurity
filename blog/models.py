# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Post(models.Model):
    author = models.ForeignKey('auth.User')  # 外键：指向另一个模型的连接
    title = models.CharField(max_length=200)  # 字符数据，可定义多少个字符
    text = models.TextField()  # 没有长度限制的长文本
    published_date = models.DateTimeField(blank=True, null=True)  # 日期和时间
    created_date = models.DateTimeField(default=timezone.now)  # 日期和时间

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        '''TODO:def __str__ 这个步骤是什么意思?'''
        return self.title
