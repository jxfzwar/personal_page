# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.db import models
from django import forms
from .models import Article, Column


class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(
            attrs={'rows': 41,
                   'cols': 100
                   })},
    }
    list_display = ('title', 'pub_date')

class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'intro')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Column, ColumnAdmin)
