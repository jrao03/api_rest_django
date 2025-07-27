from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    price = serializers.DecimalField(decimal_places=2, max_digits=5, min_value=0)
    department = serializers.CharField(max_length=20)
    quantity = serializers.IntegerField(min_value=0, max_value=999)

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.department = validated_data.get('department', instance.department)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance
    
