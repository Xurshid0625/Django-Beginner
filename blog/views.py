from django.shortcuts import render, HttpResponse
from .models import Category, Tag, Post


def home_page(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    print(posts)
    data = {"categories": categories, "posts": posts}
    return render(request=request, template_name="index.html", context=data)


def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "detail.html", context={"post": post})
