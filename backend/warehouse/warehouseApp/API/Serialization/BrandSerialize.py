from rest_framework import serializers
from ...models import Brand


# Manual
class BrandSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(required=True,
                                 allow_null=False,
                                 allow_blank=False,
                                 max_length=25)

    def create(self, validated_data):
        return Brand.objects.save(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


# Modelo
class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']
