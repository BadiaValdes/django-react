from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from ..models import Brand
from django.views import generic
from ..forms import formsBrand

# INDEX
def index(request):
    return render(request, 'index.html')

# Basada en método
def list(request):
    brand = Brand.objects.all()  # Nos permite obtener todos los datos de un objeto en la base de datos
    # Variable encargada de almacenar los datos a utilizar en la plantilla.
    context = {
        'name': 'Eduardo',
        'brands': brand
    }
    # En este caso el nombre de la plantilla comienza con la carpeta donde está ubicada
    return render(request, 'pages/brand/list.html', context)


# Listar las marcas utilizando las vistas genericas
class listGeneric(generic.ListView):
    template_name = 'pages/brand/list.html'  # nombre de la plantilla que va a utilizar.
    context_object_name = 'brands'  # el nombre con el que se accederá al objeto principal en la plantilla
    model = Brand  # modelo que se va a utilizar para mostrar los datos

    # Las vistas genéricas poseen una serie de métodos que podemos sobreescribir
    def get_context_data(self, *, object_list=None,
                         **kwargs):  # Este método nos permite modificar los valores del contexto
        context = super().get_context_data(
            **kwargs)  # Creamos la variable contexto y le asignamos todos los datos que ya existían en la clase padre (brand.objects.all)
        context['name'] = 'Bruno'  # añado un valor nuevo al contexto
        return context  # retorno el contexto


# Crear basada en clase
class createView(generic.CreateView):
    model = Brand
    form_class = formsBrand.BrandForm
    template_name = 'pages/brand/create.html'
    success_url = reverse_lazy('brand_list')


# Crear basada en funcion
def create(request):
    if request.method == 'GET':
        return render(request, 'pages/brand/create.html')
    else:
        brand = Brand.objects.create(name=request.POST['name'])
        return redirect('/brand/list')


# Modificar
def update(request, pk):
    print(request.method)
    if request.method == 'GET':
        brand = get_object_or_404(Brand, id=pk)
        return render(request, 'pages/brand/update.html', {'brand': brand, 'pk': pk})
    else:
        brand = get_object_or_404(Brand, id=pk)
        brand.name = request.POST['name']
        brand.save()
        return redirect(reverse_lazy('brand_list'))


class updateBrand(generic.UpdateView):
    model = Brand
    form_class = formsBrand.BrandForm
    template_name = 'pages/brand/update.html'
    success_url = reverse_lazy('brand_list')


# Delete
def delete(request, pk):
    if request.method == 'GET':
        brand = get_object_or_404(Brand, id=pk)
        brand.delete()
        return redirect(reverse_lazy('brand_list'))


class brandDelete(generic.DeleteView):
    model = Brand
    success_url = reverse_lazy('brand_list')
    template_name = 'pages/brand/delete.html'


# Details
def detail(request, pk):
    if request.method == 'GET':
        brand = get_object_or_404(Brand, id=pk)
        print(brand.name)
        return render(request, 'pages/brand/details.html', {'brand': brand})

class brandDetails(generic.DetailView):
    model = Brand
    template_name = 'pages/brand/details.html'