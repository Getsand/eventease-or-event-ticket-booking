import requests
import os
from django.core.mail import send_mail  # optional fallback
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Booking, Ticket
from django.core.mail import send_mail



def send_resend_email(to_email, subject, content):
    api_key = os.getenv("RESEND_API_KEY")
    response = requests.post(
        "https://api.resend.com/emails",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "from": "EventEase <onboarding@resend.dev>",
            "to": [to_email],
            "subject": subject,
            "html": content,
        },
    )
    return response.json()


@login_required
def book_ticket(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    try:
        booking = Booking.objects.create(user=request.user, event=event)
        Ticket.objects.create(user=request.user, event=event)

        # Send email via ReSend
        send_resend_email(
            to_email=request.user.email,
            subject="Your Ticket is Confirmed!",
            content=f"<strong>{request.user.username}</strong>, your ticket for <b>{event.name}</b> is booked."
        )

        messages.success(request, 'Ticket booked and email sent!')
    except Exception as e:
        messages.error(request, str(e))
    return redirect('eventapp:event_list')

@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'eventapp/event_list.html', {'events': events})
