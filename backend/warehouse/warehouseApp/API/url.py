from .Controllers import BrandController, ProductController, PositionController, TypeController
from django.urls import path, re_path

urlpatterns = [
    # Brand
    path('brand', BrandController.BrandList.as_view(), name='brand_list'),
    re_path('brand/detail/(?P<pk>[0-9a-f]{32})', BrandController.BrandDetails.as_view(), name='brand_detail'),

    # Type
    path('type', TypeController.ProductTypeList.as_view(), name='type_list'),
    re_path('type/detail/(?P<pk>[0-9a-f]{32})', TypeController.ProductTypeDetails.as_view(), name='type_detail'),

    # Position
    path('position', PositionController.PositionList.as_view(), name='position_list'),
    re_path('position/detail/(?P<pk>[0-9a-f]{32})', PositionController.PositionDetails.as_view(),
            name='position_detail'),

    # Product
    path('product', ProductController.product_list, name='product_list'),
    path('productApi', ProductController.ProductAPI.as_view(), name='product_api_list'),
    re_path('productApi/(?P<pk>[0-9a-f]{32})', ProductController.ProductAPID.as_view(),
            name='product_api_detail'),
]
