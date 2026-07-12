from django.contrib import admin
from .models import Contact, Appointment, Feedback

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'date')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('date',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'time', 'service', 'status', 'paid')
    search_fields = ('name', 'email', 'service')
    list_filter = ('date', 'service', 'status', 'paid')
    ordering = ('-date_created',)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_created', 'rating')
    search_fields = ('name', 'email')
    list_filter = ('date_created',)

