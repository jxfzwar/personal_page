# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Register your models here.
from django.contrib import admin
from django.db import models
from django import forms
from .models import Article, Column


class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(
            attrs={'rows': 20,
                   'cols': 110
                   })},
    }
    list_display = ('title', 'publish_year','articleurl')

class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'intro')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Column, ColumnAdmin)
