from django.shortcuts import render
from .models import Article, Comment, HashTag

# Create your views here.
def index(request):
    article_list = Article.objects.all()
    hashtag_list = HashTag.objects.all()

    # category_list = set([])
    # for article in article_list:
    #     category_list.add(article.get_category_display())
    # print(category_list)
    category_list = set([
        article.get_category_display()
        for article in article_list
    ])

    ctx = {
        "article_list" : article_list,
        "hashtag_list" : hashtag_list,
        "category_list" : category_list,
    }
    return render(request, "index.html", ctx)

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    hashtag_list = HashTag.objects.all()
    ctx = {
        "article" : article,
        "hashtag_list" : hashtag_list,
    }
    return render(request, "detail.html", ctx)

# def about(request):
#     pass
