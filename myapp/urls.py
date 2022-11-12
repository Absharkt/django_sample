from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='hlo'),
    path('land',views.land,name='land'),
]
