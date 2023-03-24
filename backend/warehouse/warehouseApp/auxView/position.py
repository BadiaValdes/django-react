from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from ..models import Position
from django.views import generic
from ..forms import formPosition


# Create
class createView(generic.CreateView):
    model = Position
    form_class = formPosition.PositionForm
    template_name = 'pages/position/create.html'
    success_url = reverse_lazy('position_list')


# list
class listGeneric(generic.ListView):
    template_name = 'pages/position/list.html'
    context_object_name = 'objects'
    model = Position

    def get_context_data(self, *, object_list=None,
                         **kwargs):
        context = super().get_context_data(
            **kwargs)
        return context


# update
class updatePosition(generic.UpdateView):
    model = Position
    form_class = formPosition.PositionForm
    context_object_name = 'position'
    template_name = 'pages/position/update.html'
    success_url = reverse_lazy('Position_list')


# delete
class deletePosition(generic.DeleteView):
    model = Position
    success_url = reverse_lazy('Position_list')
    template_name = 'pages/position/delete.html'


# Details
class detailsPosition(generic.DetailView):
    model = Position
    template_name = 'pages/position/details.html'
