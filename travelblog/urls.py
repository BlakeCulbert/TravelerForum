from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='travel-blog-home'),
    path('about/', views.about, name='travel-blog-about'),
    path('regions/', views.continents, name='travel-blog-regions'),
    path('regions/africa/', views.africa, name='travel-blog-africa'),
    path('regions/asia/', views.asia, name='travel-blog-asia'),
    path('regions/oceania/', views.oceania, name='travel-blog-oceania'),
    path('regions/centralamerica/', views.centralamerica, name='travel-blog-centralamerica'),
    path('regions/europe/', views.europe, name='travel-blog-europe'),
    path('regions/middleeast/', views.middleeast, name='travel-blog-middleeast'),
    path('regions/northamerica/', views.northamerica, name='travel-blog-northamerica'),
    path('regions/southamerica/', views.southamerica, name='travel-blog-southamerica'),
]