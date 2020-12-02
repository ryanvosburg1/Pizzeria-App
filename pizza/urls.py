from django.urls import path
from . import views
#import views module from urls module

app_name = 'pizza'

urlpatterns = [
    path('', views.index, name='index'),
    path('pizza',views.pizza,name='pizza'),
    path('pizza/<int:pizza_id>/',views.p,name='pizza'),
    path('new_comment/<int:pizza_id>/',views.new_comment,name='new_comment'),
]





