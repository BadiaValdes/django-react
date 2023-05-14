from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from ..Serialization import ProductSerialize
from ...models import Product
from rest_framework import status, viewsets, generics


# Metodo
@csrf_exempt
def product_list(request):
    if request.method == 'GET':  # Preguntamos si la peticion es de tipo GET
        product = Product.objects.all()  # Obtenemos todos los productos de la base de datos
        serializer = ProductSerialize.ProductSerializer(product, many=True)  # Serializamos los productos
        return JsonResponse(serializer.data,
                            safe=False)  # Retornamos el valor cen un Json Response, esto significa que django tratara la respuesta como un json


# API View
class ProductAPI(APIView):
    def get(self, request, format=None):  # Declaramos un metodo para manejar las peticiones get
        product_list_value = Product.objects.all()  # Obtenemos todos los productos
        serializer = ProductSerialize.ProductSerializer(product_list_value,
                                                        many=True)  # lo serializamos, el many=True permite serializar varios objetos
        return Response(serializer.data)  # Devolvemos los datos

    def post(self, request, format=None):
        serialize = ProductSerialize.ProductSerializer(
            data=request.data)  # Serializamos los datos que nos pasen por parametro
        if serialize.is_valid():  # Preguntamos si son datos validos
            serialize.save()  # En caso que lo sean los guardamos
            return Response(serialize.data, status=status.HTTP_201_CREATED)  # Devolvemos los datos y un estado HTTP 201
        return Response(serialize.errors,
                        status=status.HTTP_400_BAD_REQUEST)  # En caso que no sean validos, devolvemos un error y el estado 400


# APIView
class ProductAPID(APIView):
    def put(self, request, pk, format=None):  # Creamos un metodo para manejar las peticiones de modificacion o PUT
        serialize = ProductSerialize.ProductSerializer(data=request.data)  # Mismo procedimiento del post
        # ...
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk,
            format=None):  # Obtenemos los datos de un solo producto. Tenemos que pasar como parametro el valor de la url PK
        product_list_value = Product.objects.get(
            id=pk)  # Buscamos en bd la url, podriamos haber utilizado get_object_or_404
        serializer = ProductSerialize.ProductSerializer(product_list_value, many=False)  # Lo serializamos
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)  # Devolvemos el valor

    def delete(self, request, pk, format=None):
        Product.objects.get(id=pk).delete()  # Obtenemos el valor y lo eliminamos
        return Response('deleted', status=status.HTTP_200_OK)  # Devolvemos un mensaje y el estado 200


# ViewSet
class ProductView(viewsets.ViewSet):
    def list(self, request):  # Similar al get de APIView
        query = Product.objects.all()
        serialize = ProductSerialize.ProductSerializer(query, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)

    def create(self, request, ):  # Similar al post de APIView
        serialize = ProductSerialize.ProductSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):  # Similar al get de APIView
        query = Product.objects.get(id=pk)
        serialize = ProductSerialize.ProductSerializer(query, many=False)
        return Response(serialize.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):  # Similar al Delete de APIView
        query = get_object_or_404(id=pk)
        query.delete()
        return Response('Deleted', status=status.HTTP_200_OK)

    def update(self, request, pk=None):  # Similar al put de APIView
        serialize = ProductSerialize.ProductSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_200_OK)
        return Response(serialize.errors, status=status.HTTP_201_CREATED)


# Model View Set
class ProductModelViwe(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerialize.ProductSerializer


# Generic View
class ProductGLC(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialize.ProductSerializer


class ProductGURD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialize.ProductSerializer
