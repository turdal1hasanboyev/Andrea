from django.shortcuts import render, redirect

from .models import Article, Comment, Account

from django.core.paginator import Paginator


def index(request):
    tag = request.GET.get('tag')
    cat = request.GET.get('cat')
    page_number = request.GET.get('page')

    articles = Article.objects.all().order_by('-id')

    popular_articles = articles.order_by('?')
    
    if tag:
        articles = articles.filter(tags__title__exact=tag)

    if cat:
        articles = articles.filter(category__slug__exact=cat)

    paginator = Paginator(articles, 10)
    selected_page = paginator.get_page(page_number)
    selected_page.adjusted_elided_pages = paginator.get_elided_page_range(page_number)

    context = {
        "articles": selected_page,
        "popular_articles": popular_articles[:3],
        }
    
    return render(request, 'index.html', context)

def single(request, slug):
    article = Article.objects.get(slug__exact=slug)
    
    article.views+=1
    
    article.save()

    comments = Comment.objects.filter(article_id=article.id)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        comment = request.POST.get("comment")
        web_site = request.POST.get("website")

        Comment.objects.create(
            article_id=article.id,
            user_id=request.user.id,
            name=name,
            email=email,
            message=comment,
            web_site=web_site,
        )

        return redirect('single', article.slug)

    context = {
        "article": article,
        "comments": comments,
        }
    
    return render(request, 'single.html', context)

def travel(request):
    tag = request.GET.get('tag')
    page_number = request.GET.get('page')

    articles = Article.objects.filter(category__slug__exact="travel").order_by('-id')
    
    if tag:
        articles = articles.filter(tags__title__exact=tag)

    paginator = Paginator(articles, 10)
    selected_page = paginator.get_page(page_number)

    return render(request, 'travel.html', {"articles": selected_page})

def fashion(request):
    page_number = request.GET.get('page')

    articles = Article.objects.filter(category__slug__exact="fashion").order_by('-id')

    paginator = Paginator(articles, 10)
    selected_page = paginator.get_page(page_number)

    return render(request, 'fashion.html', {"articles": selected_page})

def about(request):
    user = Account.objects.get(id=1)

    return render(request, 'about.html', {"user": user})
