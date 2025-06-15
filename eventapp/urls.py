from django.urls import path
from . import views

app_name = 'eventapp'

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('book/<int:event_id>/', views.book_ticket, name='book_ticket'),
]
