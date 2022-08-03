from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from .models import ContactLink, ContactModel
from .forms import ContactForms


class ContactView(View):
    def get(self, request):
        contacts = ContactLink.objects.all()
        form = ContactForms()
        return render(request, 'contact/contact.html', {"contacts": contacts, "form": form})


class CreateContact(CreateView):
#    model = ContactModel#.objects.all()
    form_class = ContactForms
#    template_name = 'contact/contact.html'
    success_url = '/'
