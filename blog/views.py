from django.shortcuts import render, redirect
from .models import Category, Post, Comment, Rating

from .utils import check_read_articles


def home_page(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    print(posts)
    data = {"categories": categories, "posts": posts}
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
