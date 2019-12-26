from django.db import models
class Planet(models.Model):
    planet_name=models.CharField(max_length=200,null=True)
    rotation_period=models.CharField(max_length=100,null=True)
    orbital_period=models.CharField(max_length=100,null=True)
    gravity=models.CharField(max_length=100,null=True)
    films=models.CharField(max_length=1000,null=True)
    images=models.ImageField(default='https://image.cnbcfm.com/api/v1/image/106256503-1574274174070yoda.jpg?v=1574274186&w=740&h=416',blank=True)
