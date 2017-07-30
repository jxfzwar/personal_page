# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Article

def aindex(request):
    return render(request, 'aindex.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    latest_article_list = Article.objects.query_by_time()
    context = {'latest_article_list': latest_article_list}
    return render(request, 'blog.html',context)

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def services(request):
    return render(request, 'services.html')

