from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_list, name="MY List"),
    path('<id>', views.list_detail, name="My List Detail")
]
