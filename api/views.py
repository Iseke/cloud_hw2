from django.shortcuts import render
from .utils import main

def base_view(request):
    images = main()

    context = {
        'images': images
    }
    return render(request, 'index.html', context=context)
