from django.urls import path
from . import views


urlpatterns = [
    path('<slug:slug>/<slug:product_slug>/', views.ProductDetailView.as_view(), name="product_single"),
    path('<slug:slug>/', views.ProductListView.as_view(), name="product_list"),
    path('', views.HomeView.as_view(), name="home"),
]
