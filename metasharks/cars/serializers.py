from rest_framework import serializers
from .models import Orders, Colors, CarModels, CarBrands

class OrdersSerializer(serializers.ModelSerializer):
    """
    Serializing ID, COLOR, CAR_MODEL, CAR_BRAND, QUANTITY, ORDER_DATE
    for OrdersView
    """
    car_brand = serializers.IntegerField(source='car_model.brand_id', read_only=True)

    class Meta:
        model = Orders
        fields = '__all__'

class ColorsSerializer(serializers.ModelSerializer):
    """
    Serializing ID, COLOR, QUANTITY_ORDERED
    for ColorsView
    """
    quantity_ordered = serializers.SerializerMethodField()

    class Meta:
        model = Colors
        fields = '__all__'

    def get_quantity_ordered(self, obj): 
        count = obj.orders.count()
        return count

class CarModelsSerializer(serializers.ModelSerializer):
    """
    Serializing ID, MODEL, BRAND
    for CarModelsView
    """
    class Meta:
        model = CarModels
        fields = '__all__'

class CarBrandsSerializer(serializers.ModelSerializer):
    """
    Serializing ID, BRAND_NAME, QUANTITY_ORDERED 
    for CarBrandsView
    """
    quantity_ordered = serializers.SerializerMethodField()
    class Meta:
        model = CarBrands
        fields = '__all__'
    
    def get_quantity_ordered(self, obj): # Get orders quantity of the brand
        count = obj.car_models.all()
        quantity = 0
        for object in count:
            quantity += object.orders.count()
        return quantity

        