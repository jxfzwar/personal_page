# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Article,Column

def aindex(request):
    return render(request, 'aindex.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    #latest_article_list = Article.objects.query_by_time()
    article_column = Column.objects.all()
    #context = {'latest_article_list': latest_article_list,'article_column':article_column}

    keyword = request.POST.get('searchWords')
    allArticle = Article.objects.query_by_time()
    SearchResult = []
    if keyword == None:
        SearchResult = allArticle
    else:
        for x in allArticle:
            if keyword in x.title:
                SearchResult.append(x)
            elif keyword in x.abstract:
                SearchResult.append(x)
            elif keyword in x.author:
                SearchResult.append(x)
            elif keyword in str(x.publish_year):
                SearchResult.append(x)
            else:
                for y in x.column.all():
                    if keyword in y.name:
                        SearchResult.append(x)

    if len(SearchResult) == 0:
        SearchStatus = "Error"
    else:
        SearchStatus = "Success"
    ResultAmount = len(SearchResult)

    return render(request, 'blog.html', {"keyword": keyword,
                                                "SearchResult": SearchResult,
                                                "SearchStatus": SearchStatus,
                                                "ResultAmount": ResultAmount,
                                         "article_column":article_column})

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def services(request):
    return render(request, 'services.html')



