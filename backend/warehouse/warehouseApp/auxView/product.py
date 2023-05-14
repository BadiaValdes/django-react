from ..models import Product
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from ..forms import formProduct

base_dir_url = 'pages/product/'

class Base():
    model=Product

class BaseCU(Base):
    success_url = reverse_lazy('product_list')
    form_class = formProduct.ProductForm


# Create
class CreateView(BaseCU, generic.CreateView):
    template_name = base_dir_url + 'create.html'

    # def form_valid(self, form):
    #     print(form)
    #
    # def form_invalid(self, form):
    #     print("INVALID FORM DATA")



# list
class ListGeneric(Base, generic.ListView):
    template_name = base_dir_url + 'list.html'
    context_object_name = 'objects'

    def get_context_data(self, *, object_list=None,
                         **kwargs):
        context = super().get_context_data(
            **kwargs)

        return context


# update
class UpdateView(BaseCU, generic.UpdateView):
    template_name = base_dir_url + 'update.html'
    context_object_name = 'object'


# delete
class DeleteView(Base, generic.DeleteView):
    template_name = base_dir_url + 'delete.html'
    success_url = reverse_lazy('product_list')


# Details
class DetailsView(Base, generic.DetailView):
    template_name = base_dir_url + 'details.html'
