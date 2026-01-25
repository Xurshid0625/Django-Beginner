from django.shortcuts import render, redirect
from .models import Category, Post, Comment, Rating

from .utils import check_read_articles


def home_page(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    last_comments = Comment.objects.all().order_by("-id")[:10]

    data = {"categories": categories, "posts": posts, "last_comments": last_comments}
    return render(request=request, template_name="index.html", context=data)


def detail(request, post_id):
    category = Category.objects.all()
    post = Post.objects.get(id=post_id)

    if post.id in check_read_articles(request):
        pass
    else:
        check_read_articles(request).append(post.id)
        post.views += 1
        post.save()

    if request.method == "POST":
        name = request.POST.get("name")
        comment = request.POST.get("comment")

        if all([name, comment]):
            Comment.objects.create(author=name, comment=comment, post=post)

    return render(
        request, "detail.html", context={"post": post, "categories": category}
    )


def set_rating(request, value, post_id):
    post = Post.objects.get(id=post_id)
    value = int(value)

    if all([post, value]):
        Rating.objects.create(post=post, value=value)
    return redirect("/")


def category_list(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(category=category)
    last_comments = Comment.objects.all().order_by("-id")[:10]

    return render(
        request,
        "category.html",
        context={"posts": posts, "category": category, "last_comments": last_comments},
    )


def search(request):
    last_comments = Comment.objects.all().order_by("-id")[:10]
    query = request.GET.get("query")
    posts = Post.objects.filter(title__icontains=query)
    return render(
        request,
        "index.html",
        context={"posts": posts, "last_comments": last_comments},
    )
