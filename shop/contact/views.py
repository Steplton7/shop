from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from .models import ContactLink, About  # ContactModel
from .forms import ContactForms


class ContactView(View):
    def get(self, request):
        contacts = ContactLink.objects.all()
        form = ContactForms()
        return render(request, 'contact/contact.html', {"contacts": contacts, "form": form})


class CreateContact(CreateView):
    # model = ContactModel#.objects.all()
    # template_name = 'contact/contact.html'
    form_class = ContactForms
    success_url = '/'


class AboutView(View):
    def get(self, request):
        about = About.objects.last()
        return render(request, 'contact/about.html', {"about": about})

