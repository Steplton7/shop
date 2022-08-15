from django.urls import path
from django.views.decorators.cache import cache_page
from . import views


urlpatterns = [
    path('<slug:slug>/<slug:product_slug>/', views.ProductDetailView.as_view(), name="product_single"),
    path('<slug:slug>/', views.ProductListView.as_view(), name="product_list"),
    path('', cache_page(60*15)(views.HomeView.as_view()), name="home"),
    # path('', views.HomeView.as_view(), name="home"),
]
