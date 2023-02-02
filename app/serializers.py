from rest_framework import serializers
from .models import Client, Product, Mark


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['tg_id', 'full_name', 'prop_address', 'passport', 'mark', 'phone', 'products', 'update_date']


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = '__all__'


class NewMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ['mark']


class ClientNewSerializer(serializers.ModelSerializer):
    marks = NewMarkSerializer(read_only=True)
    class Meta:
        model = Client
        fields = ['full_name','phone', 'passport', 'prop_address', 'marks', ]
