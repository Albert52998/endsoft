from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import F

from .models import Soft, Category
# from .forms import SoftForm

from django.core.paginator import Paginator


def index(request):
    search_query = request.GET.get('search', '')

    if search_query:
        softs = Soft.objects.filter(title__icontains=search_query)
    else:
        softs = Soft.objects.all()

    paginator = Paginator(softs, 5)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    # if page.has_previous():
    #     prev_url = f'?page={page.previous_page_number()}'
    # else:
    #     prev_url = ''

    # if page.has_next():
    #     next_url = f'?page={page.next_page_number()}'
    # else:
    #     next_url = ''


    # form = SoftForm()

    categories = Category.objects.filter(parent_category=None)

    context = {
        'softs': softs, 
        'categories': categories, 
        'page_object': page, 
        'paginator': paginator, 
        'search_query': search_query
    }
    return render(request, 'main/index.html', context)


def soft_downloads_count(request, soft_id):
    '''Счетчик клика по ссылке Скачать'''
    soft = Soft.objects.get(pk=soft_id)
    soft.counter += 1
    soft.save()
    return redirect(soft.file.url)


def by_category(request, category_id):
    # search_query = request.GET.get('search', '')

    # if search_query:
    #     softs = Soft.objects.filter(title__icontains=search_query, soft=category_id)
    # else:
    softs = Soft.objects.filter(category=category_id)

    # paginator = Paginator(softs, 2)

    # page_number = request.GET.get('page', 1)
    # page = paginator.get_page(page_number)

    # is_paginated = page.has_other_pages()
    
    categories = Category.objects.filter(parent_category=None)
    current_category = Category.objects.get(pk=category_id)
    context = {'softs': softs, 'categories': categories, 'current_category': current_category}
    return render(request, 'main/by_category.html', context)


def by_soft(request, soft_id):
    softs = Soft.objects.all()
    categories = Category.objects.filter(parent_category=None)
    current_soft = Soft.objects.get(pk=soft_id)
    context = {'softs': softs, 'categories': categories, 'current_soft': current_soft}
    return render(request, 'main/by_soft.html', context)
