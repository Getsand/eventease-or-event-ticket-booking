from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count
from eventapp.models import Ticket, Event
import csv

# Admin-only: Export all tickets as CSV
@staff_member_required
def export_tickets_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tickets.csv"'
    writer = csv.writer(response)
    writer.writerow(['User', 'Event', 'Booking Time'])

    tickets = Ticket.objects.select_related('user', 'event').all()
    for ticket in tickets:
        writer.writerow([ticket.user.username, ticket.event.name, ticket.booked_at])

    return response

# Organizer & Staff: Show event-wise booking stats
@login_required
def analytics_view(request):
    events = Event.objects.annotate(num_tickets=Count('ticket'))
    labels = [event.name for event in events]
    data = [event.num_tickets for event in events]
    return render(request, 'dashboard/analytics.html', {
        'labels': labels,
        'data': data
    })
