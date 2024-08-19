from django.shortcuts import render, redirect

from .forms import ContactForm


def get_in_touch(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save()
        
        return redirect("contact")
    
    return render(request, "contact.html", {"form": form})
