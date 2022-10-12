from django.contrib import admin
from .models import *

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_brand', 'car_model', 'color', 'quantity', 'order_date')


    @admin.display(ordering='car_model__brand', description='brand')
    def get_brand(self, obj): ## Brand display in admin panel ##
        return obj.car_model.brand 

@admin.register(Colors)
class ColorsAdmin(admin.ModelAdmin):
    list_display = ('color',)

@admin.register(CarModels)
class CarModelsAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand')

@admin.register(CarBrands)
class CarBrandsAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)

