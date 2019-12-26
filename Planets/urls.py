from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('database_addition/',views.database_addition,name='database'),
    path('local_store/',views.local_store,name='store'),
]
