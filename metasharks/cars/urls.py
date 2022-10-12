from django.urls import path, include
from cars.models import Orders
from .views import OrdersView, ColorsView, CarBrandsView, CarModelsView
from rest_framework import routers

############ Simple router for all views ###############
router = routers.SimpleRouter()

router.register(r'orders', OrdersView, basename='orders')
router.register(r'colors', ColorsView)
router.register(r'brands', CarBrandsView)
router.register(r'models', CarModelsView)
########################################################

urlpatterns = [
    path('', include(router.urls)),
    path('orders/brand/<int:brand_id>/', OrdersView.as_view({'get': 'list'})) # Filter by brand
]