from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.add_cart, name='index'),
    path('about', views.about, name='about')
]