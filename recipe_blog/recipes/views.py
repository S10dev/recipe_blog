from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Recipe


def index(request):
    recipe_list = Recipe.objects.order_by('-pk').all()
    paginator = Paginator(recipe_list, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request, 'index.html',
        {'page': page, 'paginator': paginator}
        )
