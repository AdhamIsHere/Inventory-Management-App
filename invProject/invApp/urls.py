from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name='home'),
    path('create/',views.create_product_view,name='create_product'),
    path('list/',views.product_list_view,name='product_list'),
    path('update/<int:pid>/',views.update_product_view,name='update_product'),
    path('delete/<int:pid>/',views.delete_product_view,name='delete_product'),
]