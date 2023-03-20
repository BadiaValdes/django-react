from django.shortcuts import render
from .models import Brand
from django.views import generic
def index(request):
    return render(request, 'layout.html')


createIt = False
# Listar las marcas mediante un metodo
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

    # En este caso el nombre de la plantilla comienza con la carpeta donde está ubicada
    return render(request, 'pages/list.html', context)

# Listar las marcas utilizando las vistas genericas
class listGeneric(generic.ListView):
    template_name = 'pages/list.html' # nombre de la plantilla que va a utilizar.
    context_object_name = 'brands' # el nombre con el que se accederá al objeto principal en la plantilla
    model = Brand # modelo que se va a utilizar para mostrar los datos

    # Las vistas genéricas poseen una serie de métodos que podemos sobreescribir
    def get_context_data(self, *, object_list=None, **kwargs): # Este método nos permite modificar los valores del contexto
        context = super().get_context_data(**kwargs) # Creamos la variable contexto y le asignamos todos los datos que ya existían en la clase padre (brand.objects.all)
        context['name']='Bruno' # añado un valor nuevo al contexto
        return context # retorno el contexto
def create(request):
    return render(request, 'pages/create.html')