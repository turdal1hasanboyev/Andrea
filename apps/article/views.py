from django.shortcuts import render, redirect
from .models import Article, Category, Comment

def index(request):
    articles = Article.objects.all().order_by('-id')


    context = {
        "articles": articles,
        }
    
    return render(request, 'index.html', context)
