from django.shortcuts import render
from .models import Article, Category, Tag, Comment


def index(request):

    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'index.html',context)

