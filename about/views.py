from django.shortcuts import render
from django.http import HttpResponse
from .models import AboutPage

# Create your views here.

def index(request):
    about_pages = AboutPage.objects.filter(is_active=True).first()
    context = {
        'about_page': about_pages
    }
    return render(request, 'about/index.html', context)
