from rest_framework import generics
from ..Serialization import TypeSerialize
from ...models import ProductType


class ProductTypeList(generics.ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = TypeSerialize.ProductTypeSerializer


class ProductTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductType.objects.all()
    serializer_class = TypeSerialize.ProductTypeSerializer
