from django.shortcuts import render

# Create your views here.


def index_website(request):
    return render(request, 'index_website.html')
