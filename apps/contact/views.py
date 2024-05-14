from django.shortcuts import render, redirect
from .models import Contact
from .forms import Contact


def get_in_touch(request):
    form = Contact(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("contact")
    
    return render(request, "contact.html", {"form": form})
