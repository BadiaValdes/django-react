from .auxView import brand, position, producType, dal, product
from django.urls import path, re_path

urlpatterns = [
    # Index
    path('', brand.index, name='index'),

    # Brand
    path('brand/fun/list', brand.list, name='brand_list_fun'),
    path('brand/', brand.listGeneric.as_view(), name='brand_list'),  # URL para vista creada mediante vista generica.
    path('brand/fun/create/', brand.create, name='brand_create_fun'),  # URL para crear mediante funcion.
    path('brand/create/', brand.createView.as_view(), name='brand_create'),  # URL para crear generico
    re_path('brand/fun/update/(?P<pk>[0-9a-f]{32})', brand.update, name='update_function'),
    # URL para actualizar mediante función
    # Se utilizó re_path debido a que path por defecto no valida UUID
    re_path('brand/update/(?P<pk>[0-9a-f]{32})', brand.updateBrand.as_view(), name='brand_update'),
    # URL para actualizar mediante función
    re_path('brand/fun/delete/(?P<pk>[0-9a-f]{32})', brand.delete, name='brand_delete_fun'),
    # URL para actualizar mediante función
    re_path('brand/delete/(?P<pk>[0-9a-f]{32})', brand.brandDelete.as_view(), name='brand_delete'),
    # URL para actualizar mediante función
    re_path('brand/fun/details/(?P<pk>[0-9a-f]{32})', brand.detail, name='brand_detail_fun'),
    # URL para actualizar mediante función
    re_path('brand/details/(?P<pk>[0-9a-f]{32})', brand.brandDetails.as_view(), name='brand_details'),
    # URL para actualizar mediante función

    # Position
    path('position/', position.listGeneric.as_view(), name='position_list'),
    path('position/create', position.createView.as_view(), name='position_create'),
    re_path('position/update/(?P<pk>[0-9a-f]{32})', position.updatePosition.as_view(), name='position_update'),
    re_path('position/delete/(?P<pk>[0-9a-f]{32})', position.deletePosition.as_view(), name='position_delete'),
    re_path('position/(?P<pk>[0-9a-f]{32})', position.detailsPosition.as_view(), name='position_details'),

    # Type
    path('type/', producType.listGeneric.as_view(), name='productType_list'),
    path('type/create', producType.createView.as_view(), name='productType_create'),
    re_path('type/update/(?P<pk>[0-9a-f]{32})', producType.updateView.as_view(), name='productType_update'),
    re_path('type/delete/(?P<pk>[0-9a-f]{32})', producType.deleteView.as_view(), name='productType_delete'),
    re_path('type/(?P<pk>[0-9a-f]{32})', producType.detailsView.as_view(), name='productType_details'),

    # Product
    path('product/', product.ListGeneric.as_view(), name='product_list'),
    path('product/create', product.CreateView.as_view(), name='product_create'),
    re_path('product/update/(?P<pk>[0-9a-f]{32})', product.UpdateView.as_view(), name='product_update'),
    re_path('product/delete/(?P<pk>[0-9a-f]{32})', product.DeleteView.as_view(), name='product_delete'),
    re_path('product/details/(?P<pk>[0-9a-f]{32})', product.DetailsView.as_view(), name='product_details'),


    # DAL
    path('dal/brand', dal.ABrand.as_view(create_field='brand'), name='dal_brand'),
    path('dal/position', dal.APosition.as_view(create_field='position'), name='dal_position'),
    path('dal/productType', dal.AProductType.as_view(), name='dal_productType')
]
