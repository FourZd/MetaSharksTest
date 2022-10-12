from rest_framework import viewsets
from .models import Orders, Colors, CarModels, CarBrands
from .serializers import OrdersSerializer, ColorsSerializer, CarModelsSerializer, CarBrandsSerializer


class OrdersView(viewsets.ModelViewSet):
    """All-in-one CRUD view for orders"""
    serializer_class = OrdersSerializer

    def get_queryset(self):

        try: # Checking for a filter
            self.kwargs['brand_id']
            brand_id = self.kwargs['brand_id']
            queryset = Orders.objects.filter(car_model__brand_id=brand_id).order_by('quantity') # Sorted by quantity
            return queryset # Returning brand-filtered queryset

        except Exception: # No filter 
            queryset = Orders.objects.all().order_by('quantity') # Sorted by quantity
            return queryset # Returning all brands

class ColorsView(viewsets.ModelViewSet):
    """All-in-one CRUD view for colors"""
    queryset = Colors.objects.all()
    serializer_class = ColorsSerializer

class CarModelsView(viewsets.ModelViewSet):
    """All-in-one CRUD view for car models"""
    queryset = CarModels.objects.all()
    serializer_class = CarModelsSerializer

class CarBrandsView(viewsets.ModelViewSet):
    """All-in-one CRUD view for car brands"""
    queryset = CarBrands.objects.all()
    serializer_class = CarBrandsSerializer
