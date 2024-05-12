from django.shortcuts import render, redirect
from .models import Article, Category, Comment, Tag
from django.core.paginator import Paginator


def index(request):
    tag = request.GET.get('tag')

    articles = Article.objects.all().order_by('-id')
    popular_articles = articles.order_by('?')[:3]

    if tag:
        articles = articles.filter(tags__title__exact=tag)

    page_number = request.GET.get('page')
    paginator = Paginator(articles, 10)
    selected_page = paginator.get_page(page_number)
    selected_page.adjusted_elided_pages = paginator.get_elided_page_range(page_number)
  


    context = {
        "articles": selected_page,
        "popular_articles": popular_articles,
        }
    
    return render(request, 'index.html',context)


def single(request, slug):
    article = Article.objects.get(slug__exact=slug)

    articles = Article.objects.filter(category_id=article.category_id)[:3]

    comments = Comment.objects.filter(article_id=article.id)

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")
        
        name = request.POST.get("name")
        email = request.POST.get("email")
        comment = request.POST.get("comment")
        website = request.POST.get("website")


        Comment.objects.create(
            article_id=article.id,
            user=request.user,
            name=name,
            email=email,
            comment=comment,
            website=website
        )

        return redirect('single', article.slug)

    context = {
        "article": article,
        "articles": articles,
        "comments": comments,
        }
    
    return render(request, 'single.html',context)
