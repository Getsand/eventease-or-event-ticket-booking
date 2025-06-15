from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('export/', views.export_tickets_csv, name='export_csv'),
    path('analytics/', views.analytics_view, name='analytics'),
]
