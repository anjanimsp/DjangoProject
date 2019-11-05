
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='ShopHome'),
    path('contact/',views.contact,name='Contact Us'),
    path('about/',views.about,name='About Us'),
    path('tracker/',views.tracker,name='TrackingStatus'),
    path('search/',views.search,name='Search'),
    path('products/<int:myid>',views.prodView,name='ProductView'),
    path('checkout/',views.checkout,name='Checkout'),
    
]
