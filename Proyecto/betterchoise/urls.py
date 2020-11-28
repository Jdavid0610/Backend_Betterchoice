from django.urls import path

from betterchoise import views

urlpatterns = [
    path('',views.index, name='index'),
    path('mensaje',views.searchClass.salu2, name='salu2'),
    path('ASearch',views.searchClass.Amazon_search, name='Amazon_search'),
]
