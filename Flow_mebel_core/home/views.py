from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main_page(request):
    return render(request, 'home/main_page.html')

def about_page(request):
    return render(request, 'home/about_us_page.html')