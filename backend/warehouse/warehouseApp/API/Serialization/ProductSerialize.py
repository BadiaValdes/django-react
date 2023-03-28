from rest_framework import serializers
from ...models import Product, Brand, Position, ProductType
from . import BrandSerialize, PositionSerialize, TypeSerialize


class ProductSerializer(serializers.ModelSerializer):
    # Se comentaron todos debido a que en el front no se podian enviar los datos de las llaves foraneas
    # brand = BrandSerialize.BrandModelSerializer(many=False) # Serializamos el objeto por completo
    # position = PositionSerialize.PositionSerializer(many=False) # Serializamos el objeto por completo
    # type = TypeSerialize.ProductTypeSerializer(many=False) # Serializamos el objeto por completo
    # brand = serializers.StringRelatedField(many=False) # Solo serializamos el valor que devuelve el método __str__
    # position = serializers.StringRelatedField(many=False) # Solo serializamos el valor que devuelve el método __str__
    # type = serializers.StringRelatedField(many=False) # Solo serializamos el valor que devuelve el método __str__
    # Se una many false porque la relación es de Uno a muchos, es decir, un producto solo puede tener un tipo

    photo = serializers.ImageField(required=False)
    class Meta:
        model = Product # Especificamos el modelo a utilizar
        fields = ['id', 'name', 'quantity', 'position', 'type', 'brand', 'photo'] # Definimos todos los campos, si falta alguno, no se tendrá en cuenta


class ProductRSerializer(serializers.ModelSerializer):
    # brand = BrandSerialize.BrandModelSerializer(many=False) # Serializamos el objeto por completo
    # position = PositionSerialize.PositionSerializer(many=False) # Serializamos el objeto por completo
    # type = TypeSerialize.ProductTypeSerializer(many=False) # Serializamos el objeto por completo
    # brand = serializers.StringRelatedField(many=False) # Solo serializamos el valor que devuelve el método __str__
    # position = serializers.StringRelatedField(many=False) # Solo serializamos el valor que devuelve el método __str__
    # type = serializers.StringRelatedField(many=False) # Solo serializamos el valor que devuelve el método __str__
    # Se una many false porque la relación es de Uno a muchos, es decir, un producto solo puede tener un tipo

    class Meta:
        model = Product # Especificamos el modelo a utilizar
        fields = ['id', 'name', 'quantity', 'position', 'type', 'brand'] # Definimos todos los campos, si falta alguno, no se tendrá en cuenta

