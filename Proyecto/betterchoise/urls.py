from django.urls import path

from betterchoise import views

urlpatterns = [
    path('',views.index, name='index'),
    path('mensaje',views.salu2, name='salu2')
]
