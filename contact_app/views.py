from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages


# Create your views here.
def contact(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        company_name = request.POST['company_name']
        phone = request.POST['phone']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
    

        contact = Contact(
            full_name=full_name,
            company_name=company_name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        contact.save()
        messages.success(request, "Thanks for reaching out!")
        return redirect('contact')
