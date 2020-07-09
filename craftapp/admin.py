from django.contrib import admin
#model.pyのclassを読み込む
from .models import Coordinate, World

class CoordinateAdmin(admin.ModelAdmin):
    #管理画面に表示する内容を定義する。
    list_display = ('id', 'place', 'world', 'player', 'created_date')
    #管理画面にリンク付きで表示する内容を定義する。
    list_display_links = ('id', 'place')

#管理画面に各モデルを追加する。
admin.site.register(Coordinate, CoordinateAdmin)
admin.site.register(World)


