from django.shortcuts import render, redirect
from .models import Contact
from .forms import Contacts_form

# Create your views here.
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html', {'contacts': contacts})

def addnew(request):
    if request.method == 'POST':
        form = Contacts_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = Contacts_form()
        return render(request, 'contact_form.html', {'form': form})

