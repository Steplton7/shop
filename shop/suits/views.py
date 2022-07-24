from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.filter(category__url=self.kwargs.get("slug"))


def home(request):
    return render(request, 'base.html')