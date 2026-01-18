from django.shortcuts import render, HttpResponse


def home_page(request):
    return HttpResponse("hello world!")
