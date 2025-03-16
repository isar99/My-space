from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='isar'),
    path('counter', views.counter, name='counter'),
    path('right', views.right, name='right' ),
    path('left', views.left, name='left' ),
    path('down', views.down, name='down' ),
    path('up', views.up, name='up' ),
]
