from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'layout.html')


def list(request):
    return render(request, 'pages/list.html')


def create(request):
    return render(request, 'pages/create.html')
