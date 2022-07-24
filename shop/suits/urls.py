from django.urls import path
from . import views


urlpatterns = [
    path('<slug:slug>/', views.ProductListView.as_view(), name="shop_page"),
    path('', views.home),
]
