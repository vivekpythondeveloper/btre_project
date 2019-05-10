from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from . import models

# Create your views here.


def contact(request):
    if request.method == 'POST':
        listing_id    = request.POST['listing_id']
        listing       = request.POST['listing']
        name          = request.POST['name']
        email         = request.POST['email']
        phone         = request.POST['phone']
        message       = request.POST['message']
        user_id       = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = models.Contact.objects.filter(listing_id = listing_id, user_id=user_id)

            if has_contacted:
                messages.error(request, 'you have already submitted enquery for this')
                return redirect('/listings/'+listing_id)

        contact = models.Contact(listing = listing, listing_id=listing_id,
                        name=name, email=email, phone=phone,message=message,
                        user_id=user_id)
        contact.save()

        #send mail
        send_mail(
            'Property Enquiry',
            'You have enquery for '+ listing + '. Sign into admin panel for more info.',
            'vivek.singh@skilrock.com',
            [realtor_email,'vivekkumar57@gmail.com'],
            fail_silently=False
        )

        messages.success(request, 'Your request has been submitted successfuly, a realtor wil get back to you soon')
    return redirect('/listings/'+listing_id)
