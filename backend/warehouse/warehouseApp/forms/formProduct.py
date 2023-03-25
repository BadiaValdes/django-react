from django import forms
from ..models import Product, Brand, ProductType, Position
from dal import autocomplete
from crispy_forms.helper import FormHelper


class ProductForm(forms.ModelForm):
    brand: forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        widget=autocomplete.ModelSelect2(url='dal_brand', attrs={
            'data-placeholder': 'Tipo de Producto'
        })
    )

    position: forms.ModelChoiceField(
        queryset=Position.objects.all(),
        widget=autocomplete.ModelSelect2(url='dal_position', attrs={
            'data-placeholder': 'Posicion'
        })
    )
    type: forms.ModelChoiceField(
        queryset=ProductType.objects.all(),
        widget=autocomplete.ModelSelect2(url='dal_productType', attrs={
            'data-placeholder': 'Tipo de Producto'
        })
    )

    class Meta:
        model = Product
        exclude = ('id',)
        # fields = ('name', 'photo', 'brand', 'position', 'type', 'quantity')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
