from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


class HomeView(ListView):
    model = Product
    pagination_by = 12
    template_name = "suits/home.html"

# def home(request):
#     return render(request, 'index.html')


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.filter(category__url=self.kwargs.get("slug")).select_related('category')


class ProductDetailView(DetailView):
    model = Product
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'
    slug_field = 'url'



