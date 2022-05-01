from django.db import models


class ExtractionInfo(models.Model):
    date = models.DateField()
    is_processed = models.BooleanField(default=False)

class FlatInfo(models.Model):
    date = models.DateField()
    link = models.CharField(max_length=600)
    price = models.DecimalField(max_digits=19, decimal_places=10)
    address = models.CharField(max_length=600)
    sqft_m2 = models.DecimalField(max_digits=19, decimal_places=10)
    rooms = models.IntegerField()
    bathrooms = models.IntegerField()
    discount = models.DecimalField(max_digits=19, decimal_places=10)
    floor_elevator = models.IntegerField()
    realestate = models.CharField(max_length=600)
    realestate_id = models.BigIntegerField()
    is_new_construction = models.BooleanField()
    conservation_state = models.IntegerField(null=True)
    building_type = models.CharField(max_length=200)
    building_subtype = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    neighbourhood = models.CharField(max_length=200)
    neighbourhood_id = models.IntegerField()
    neighbourhood_meanprice = models.DecimalField(max_digits=19, decimal_places=10)
    neighbourhood_meanprice_difference = models.DecimalField(max_digits=19, decimal_places=10)
    price_m2 = models.DecimalField(max_digits=19, decimal_places=10)
    extract_info_id = models.ForeignKey(ExtractionInfo, on_delete=models.CASCADE, null=True)

class NeighbourhoodMeans(models.Model):
    date = models.DateField()
    price = models.DecimalField(max_digits=19, decimal_places=10)
    sqft_m2 = models.DecimalField(max_digits=19, decimal_places=10)
    rooms = models.DecimalField(max_digits=19, decimal_places=10)
    bathrooms = models.DecimalField(max_digits=19, decimal_places=10)
    discount = models.DecimalField(max_digits=19, decimal_places=10)
    neighbourhood = models.CharField(max_length=200)
    neighbourhood_id = models.IntegerField()
    neighbourhood_meanprice_difference = models.DecimalField(max_digits=19, decimal_places=10)
    price_m2 = models.DecimalField(max_digits=19, decimal_places=10)
    extract_info_id = models.ForeignKey(ExtractionInfo, on_delete=models.CASCADE, null=True)