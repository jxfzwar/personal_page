# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Column(models.Model):
    name = models.CharField('column_name', max_length=256)
    intro = models.TextField('introduction', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'column'
        verbose_name_plural = 'column'
        ordering = ['name']


class ArticleManager(models.Manager):
    def query_by_column(self, column_id):
        query = self.get_queryset().filter(column_id=column_id)

    def query_by_time(self):
        query = self.get_queryset().order_by('-publish_year')
        return query

    def query_by_keyword(self, keyword):
        query = self.get_queryset().filter(title__contains=keyword)
        return query

@python_2_unicode_compatible
class Article(models.Model):
    column = models.ManyToManyField(Column, blank=True, null=True, verbose_name = 'belong to')
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    abstract = models.TextField('abstract')
    publishment = models.CharField(max_length=256)
    upload_date = models.DateTimeField(auto_now_add=True, editable=True)
    #pdf = models.FileField()
    articleurl = models.CharField(max_length=256)
    publish_year = models.IntegerField()
    def __str__(self):
        return "{0}, {1}".format(self.title, self.articleurl)
    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'article'

    objects = ArticleManager()
