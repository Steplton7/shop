from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "price"]
    save_as = True
    save_on_top = True


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Type)
admin.site.register(models.Comment)
