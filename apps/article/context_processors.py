from .models import Article, Category, Tag


def data(request):
    articles = Article.objects.all().order_by('-id')
    categories = Category.objects.all().order_by('title')
    tags = Tag.objects.all().order_by('title')

    popular_articles = articles.order_by('?')
    
    return {
      "categories": categories,
      "popular_articles": popular_articles[:3],
      "tags": tags,
      "articles": articles,
    }
