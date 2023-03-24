from .auxView import brand
from django.urls import path, re_path

urlpatterns = [
    path('brand/fun/list', brand.list, name='brand_list_fun'),
    path('brand/list/', brand.listGeneric.as_view(), name='brand_list'), # URL para vista creada mediante vista generica.
    path('brand/fun/create/', brand.create, name='brand_create_fun'), # URL para crear mediante funcion.
    path('brand/create/', brand.createView.as_view(), name='brand_create'), # URL para crear generico
    re_path('brand/fun/update/(?P<pk>[0-9a-f]{32})', brand.update, name='update_function'), # URL para actualizar mediante función
    # Se utilizó re_path debido a que path por defecto no valida UUID
    re_path('brand/update/(?P<pk>[0-9a-f]{32})', brand.updateBrand.as_view(), name='brand_update'), # URL para actualizar mediante función
    re_path('brand/fun/delete/(?P<pk>[0-9a-f]{32})', brand.delete, name='brand_delete_fun'), # URL para actualizar mediante función
    re_path('brand/delete/(?P<pk>[0-9a-f]{32})', brand.brandDelete.as_view(), name='brand_delete'), # URL para actualizar mediante función
]
