from django.db import models
from django.conf import settings
from django.utils import timezone

#ワールドだけ選択式にしておく。
class World(models.Model):
    world = models.CharField(max_length=30)

    def __str__(self):
        return self.world

#座標をメモするためのmodel
class Coordinate(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    world = models.ForeignKey(World, on_delete=models.PROTECT)
    player = models.CharField(max_length=30) 
    #座標の名称をplaceに記録する 
    place = models.CharField(max_length=30)
    x_coordinate = models.IntegerField(default=0)
    y_coordinate = models.IntegerField(default=0)
    z_coordinate = models.IntegerField(default=0)

    def __str__(self):
        return self.place


    

