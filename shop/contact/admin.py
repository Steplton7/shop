from django.contrib import admin
from .models import ContactModel, ContactLink, About, ImageAbout

# Register your models here.


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "create_at"]
    list_display_links = ("name",)


admin.site.register(ContactLink)
admin.site.register(About)
admin.site.register(ImageAbout)
