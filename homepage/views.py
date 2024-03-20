import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from . import models


@login_required
def homepage(request):
    tickets = models.Ticket.objects.all()
    # tickets_with_reviews = [{'ticket': ticket, 'reviews': [{}]}]
    return render(request, 'homepage.html', context={'tickets': tickets})
    #return render(request, "homepage.html")


@login_required
def ticket_upload(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            # set the uploader to the user before saving the model
            ticket.user = request.user
            # now we can save
            ticket.save()
            return redirect('homepage')
    return render(request, 'ticket_upload.html', context={'form': form})


@login_required
def ticket_update(request,id):
    ticket = models.Ticket.objects.get(id=id)
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES, instance=ticket)     
        if form.is_valid():
            # Deleting old uploaded image.
            if ticket.image:
                image_path = ticket.image.path
                if os.path.exists(image_path):
                    os.remove(image_path)
            form.save()
            return redirect('homepage')
    else:
        form = forms.TicketForm(instance=ticket)
    return render(request, 'ticket_update.html', {'form': form, 'ticket': ticket})

@login_required
def ticket_delete(request,id):
    ticket = models.Ticket.objects.get(id=id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('homepage')
    return render(request,'ticket_delete.html', {'ticket': ticket})


@login_required
def review_upload(request, id):
    ticket = models.Ticket.objects.get(id=id)
    form = forms.ReviewForm(initial={'ticket':ticket})
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES, initial={'ticket':ticket})
        if form.is_valid():
            review = form.save(commit=False)
            # Set the uploader to the user before saving the model
            review.user = request.user
            review.ticket = ticket
            # Now we can save
            review.save()
            return redirect('homepage')
    return render(request, 'review_upload.html', context={'form': form, 'ticket': ticket})
