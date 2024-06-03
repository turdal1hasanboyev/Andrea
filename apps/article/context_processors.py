from .models import Article, Category, Tag


def data(request):
    articles = Article.objects.all().order_by('-id')
    popular_articles = articles.order_by('?')[:3]
    categories = Category.objects.all().order_by('title')
    tags = Tag.objects.all().order_by('title')

    return {
      "categories": categories,
      "popular_articles": popular_articles,
      "tags": tags,
      "articles": articles,
    }
