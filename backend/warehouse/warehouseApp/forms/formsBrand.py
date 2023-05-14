from django import forms
from ..models import Brand
# Creamos la clase para almacenar los datos del formulario
# Hacemos que extienda de forms.ModelForm
class BrandForm(forms.ModelForm):
    # Añadimos la clase meta para trabajar con los atributos de ModelForm
    class Meta:
        model = Brand # Seleccionamos el modelo al que se le estará creando el formulario
        fields = ('name',) # Seleccionamos los campos,
        # fields = '__all__' # Usamos este si queremos añadir todos los campos

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)