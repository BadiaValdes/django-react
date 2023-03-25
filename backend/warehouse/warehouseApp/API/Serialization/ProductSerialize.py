from rest_framework import serializers
from ...models import Product
from . import BrandSerialize, PositionSerialize, TypeSerialize


class ProductSerializer(serializers.ModelSerializer):
    # brand = BrandSerialize.BrandModelSerializer(many=False)
    # position = PositionSerialize.PositionSerializer(many=False)
    # type = TypeSerialize.ProductTypeSerializer(many=False)
    brand = serializers.StringRelatedField(many=False)
    position = serializers.StringRelatedField(many=False)
    type = serializers.StringRelatedField(many=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'quantity', 'position', 'type', 'brand', 'photo']
