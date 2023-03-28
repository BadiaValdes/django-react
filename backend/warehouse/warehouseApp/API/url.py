from .Controllers import BrandController, ProductController, PositionController, TypeController
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'productApiV', ProductController.ProductView, basename='productApiV')
router.register(r'productApiVM', ProductController.ProductModelViwe, basename='productApiVM')

urlpatterns = [
    # Brand
    path('brand', BrandController.BrandList.as_view(), name='brand_list'),
    re_path('brand/(?P<pk>[0-9a-f]{32})', BrandController.BrandDetails.as_view(), name='brand_detail'),

    # Type
    path('type', TypeController.ProductTypeList.as_view(), name='type_list'),
    re_path('type/(?P<pk>[0-9a-f]{32})', TypeController.ProductTypeDetails.as_view(), name='type_detail'),

    # Position
    path('position', PositionController.PositionList.as_view(), name='position_list'),
    re_path('position/(?P<pk>[0-9a-f]{32})', PositionController.PositionDetails.as_view(),
            name='position_detail'),

    # Product
    path('product', ProductController.product_list, name='product_list'),
    path('productApi', ProductController.ProductAPI.as_view(), name='product_api_list'),
    re_path('productApi/(?P<pk>[0-9a-f]{32})', ProductController.ProductAPID.as_view(),
            name='product_api_detail'),

    path('productGLC', ProductController.ProductGLC.as_view(), name='product_api_g'),
    re_path('productGRUD/(?P<pk>[0-9a-f]{32})', ProductController.ProductGURD.as_view(), name='product_api_gurd'),

    # GENERIC Product

    path('', include(router.urls))
]
