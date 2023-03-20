from django.shortcuts import render
from .models import Brand




def index(request):
    return render(request, 'layout.html')


createIt = False
def list(request):
    if createIt:
        Brand.objects.create(name="Adidas")
        Brand.objects.create(name="Nike")
        Brand.objects.create(name="Converse")
        Brand.objects.create(name="Vans")
    brand = Brand.objects.all();
    context = {
        'name': 'Eduardo',
        'brands': brand
    }
    return render(request, 'pages/list.html', context)

def create(request):
    return render(request, 'pages/create.html')