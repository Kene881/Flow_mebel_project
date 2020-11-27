from django.shortcuts import render
from django.http import HttpResponse


def main_page(request):
    return render(request, 'home/home_page.html')

def about_page(request):
    return render(request, 'home/about_us_page.html')