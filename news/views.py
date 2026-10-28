from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

def get_news(request):
    news = New.objects.all()
    context = {
        'news': news
    }
    return render(request, 'news/news.html', context)

def add_news_category(request):
    if request.method == 'POST':
        form = AddNewsCategory(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        form = AddNewsCategory()
    context = {
        'form': form
    }
    return render(request, 'news/add_news_category.html', context)

def add_news(request):
    if request.method == 'POST':
        form = AddNews(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        form = AddNews()
    context = {
        'form': form
    }
    return render(request, 'news/add_news.html', context)
