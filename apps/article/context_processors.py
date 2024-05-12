from .models import Article, Category, Tag, Comment

def data(request):
    categories = Category.objects.all().order_by('title')
    tags = Tag.objects.all().order_by('title')

    return {
       "categories": categories,
       "tags": tags,

    }