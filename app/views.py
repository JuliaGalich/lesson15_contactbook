from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import Contacts_form

# Create your views here.
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})

def addnew(request):
    if request.method == 'POST':
        form = Contacts_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('contact_list')
    else:
        form = Contacts_form()
        return render(request, 'contact_form.html', {'form': form})

def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = Contacts_form(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = Contacts_form(instance=contact)
    return render(request, 'contact_form.html', {'form': form})

def delete_contact(request):
    contact_id = request.POST.get('contact_id')
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return redirect('contacts_list')