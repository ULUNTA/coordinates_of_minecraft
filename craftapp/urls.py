from django.urls import path
# .は同じ階層にあるという意味。
from . import views


app_name = 'craftapp'

#それぞれのpath一つ一つがviews.pyの関数にリンクしている。
urlpatterns = [
    path('', views.index, name='index'),
    path('new_coordinate/', views.new_coordinate, name='new_coordinate'),
    path('<int:coordinate_id>', views.coordinate_detail, name='coordinate_detail'),
    path('delete_coordinate/<int:coordinate_id>', views.delete_coordinate, name='delete_coordinate'),
    path('edit_coordinate/<int:coordinate_id>', views.edit_coordinate, name='edit_coordinate'),
    path('new_player/', views.new_player, name='new_player'),
    path('new_world/', views.new_world, name='new_world'),
    #path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    #ここからQiita記事抜粋
    path('create_account/', views.create_account, name='create_account'),
    path('account_login/', views.account_login, name='account_login'),
    #path('logout/', views.logout, name='logout'),

]