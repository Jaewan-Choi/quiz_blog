from django.shortcuts import render, redirect
from . models import Article


def home(request):
    return render(request, 'category.html')


def go_new(request):
    return render(request, 'new.html')


def write(request):
    title = request.POST.get('title', '')
    content = request.POST.get('content', '')
    category = request.POST.get('category', '')

    new_write = Article.objects.create(title=title, content=content, category=category)
    new_write.save()
    
    return redirect('/')