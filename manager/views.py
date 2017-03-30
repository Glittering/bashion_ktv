from django.shortcuts import render

# Create your views here.


def index_manager(request):
    return render(request, 'index_manager.html')
