from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from ..models import ProductType
from django.views import generic
from ..forms import formType


# Se crearon clases bases para agrupar los atributos comunes de cada una de las clases genéricas
class base():
    model = ProductType


class baseCU(base):
    success_url = reverse_lazy('productType_list')
    form_class = formType.ProductTypeForm


# Create
class createView(baseCU, generic.CreateView):
    template_name = 'pages/type/create.html'


# list
class listGeneric(base, generic.ListView):
    template_name = 'pages/type/list.html'
    context_object_name = 'objects'

    def get_context_data(self, *, object_list=None,
                         **kwargs):
        context = super().get_context_data(
            **kwargs)
        return context


# update
class updateView(baseCU, generic.UpdateView):
    template_name = 'pages/type/update.html'
    context_object_name = 'productType'


# delete
class deleteView(base, generic.DeleteView):
    template_name = 'pages/type/delete.html'


# Details
class detailsView(base, generic.DetailView):
    template_name = 'pages/type/details.html'
