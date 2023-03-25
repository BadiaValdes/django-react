from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from ..Serialization import ProductSerialize
from ...models import Product
from rest_framework import status


@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerialize.ProductSerializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


class ProductAPI(APIView):
    def get(self, request, format=None):
        product_list_value = Product.objects.all()
        serializer = ProductSerialize.ProductSerializer(product_list_value, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serialize = ProductSerialize.ProductSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductAPID(APIView):
    def put(self, request, pk, format=None):
        serialize = ProductSerialize.ProductSerializer(data=request.data)
        # ...
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        product_list_value = Product.objects.get(id=pk)
        serializer = ProductSerialize.ProductSerializer(product_list_value, many=False)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Product.objects.get(id=pk).delete()
        return Response('deleted', status=status.HTTP_200_OK)