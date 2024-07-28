from django.shortcuts import render, redirect

from apps.article.models import Article, Category, Comment, Tag, Account

from django.core.paginator import Paginator


def index(request):
    tag = request.GET.get('tag')
    cat = request.GET.get('cat')

    articles = Article.objects.all().order_by('-id')
    popular_articles = articles.order_by('?')[:3]
    categories = Category.objects.all().order_by('title')
    tags = Tag.objects.all().order_by('title')

    if tag:
        articles = articles.filter(tags__title__exact=tag)

    if cat:
        articles = articles.filter(category__slug__exact=cat)

    page_number = request.GET.get('page')
    paginator = Paginator(articles, 10)
    selected_page = paginator.get_page(page_number)
    selected_page.adjusted_elided_pages = paginator.get_elided_page_range(page_number)

    context = {
        "articles": selected_page,
        "popular_articles": popular_articles,
        "categories": categories,
        "tags": tags,
        }
    
    return render(request, 'index.html', context)

def single(request, slug):
    article = Article.objects.get(slug__exact=slug)
    
    article.views+=1
    article.save()

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
            message=comment,
            website=website,
        )

        return redirect('single', article.slug)

    context = {
        "article": article,
        "comments": comments,
        }
    
    return render(request, 'single.html', context)

def travel(request):
    tag = request.GET.get('tag')

    articles = Article.objects.filter(category__slug__exact="travel").order_by('-id')
    
    if tag:
        articles = articles.filter(tags__title__exact=tag)

    page_number = request.GET.get('page')
    paginator = Paginator(articles, 10)
    selected_page = paginator.get_page(page_number)
 
    context = {
        "articles": selected_page,
    }

    return render(request, 'travel.html', context)

def fashion(request):
    articles = Article.objects.filter(category__slug__exact="fashion").order_by('-id')

    page_number = request.GET.get('page')
    paginator = Paginator(articles, 10)
    selected_page = paginator.get_page(page_number)

    context = {
        "articles": selected_page,
    }

    return render(request, 'fashion.html', context)

def about(request):
    user = Account.objects.get(id=1)
    
    context ={
        "user": user,
    }

    return render(request, 'about.html', context)
