from django.db import models
import datetime

class Colors(models.Model):
    """
    Stores color. Reverse-related to Orders model
    """
    color = models.CharField(max_length=50, verbose_name='Color')

    def __str__(self): 
        return self.color

    class Meta:
        verbose_name = 'Color' 
        verbose_name_plural = 'Colors'


class CarBrands(models.Model):
    """
    Stores brand_name. Reverse-related to CarModels model
    """
    brand_name = models.CharField(max_length=50, verbose_name='Brand')
    
    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = 'Car brand'
        verbose_name_plural = 'Car brands'

class CarModels(models.Model):
    """
    Stores model. Related to CarBrands and reverse-related to Orders model
    """
    model = models.CharField(max_length=50)
    brand = models.ForeignKey(
        CarBrands, verbose_name='Car brand', related_name='car_models',
        on_delete=models.CASCADE)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Car model'
        verbose_name_plural = 'Car models'


class Orders(models.Model):
    """
    Stores order_date, quantity. Related to Colors, CarModels
    """
    color = models.ForeignKey(
        Colors, verbose_name = 'Car color', related_name='orders',
        on_delete=models.CASCADE
    )
    car_model = models.ForeignKey(
        CarModels, verbose_name = 'Car model', related_name='orders',
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(verbose_name='Quantity')
    order_date = models.DateField(default=datetime.date.today, verbose_name='Order date')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    