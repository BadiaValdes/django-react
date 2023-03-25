from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ..Serialization import ProductSerialize
from ...models import Product

@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerialize.ProductSerializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)