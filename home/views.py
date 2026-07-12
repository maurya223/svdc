from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from .models import Appointment, Contact, Feedback
from .forms import AppointmentForm, ContactForm, FeedbackForm

def index(request):
    if request.method == 'POST' and request.POST.get('form_type') == 'feedback':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your feedback!')
            return redirect('home')  # Redirect to home to show message
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FeedbackForm()
    return render(request, 'index.html', {'feedback_form': form})

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)  # Don't save yet
            try:
                # Send confirmation email
                subject = f'Appointment Confirmation - {appointment.name}'
                message = f"""
                Dear {appointment.name},

                Your appointment has been booked successfully.
                Details:
                - Date: {appointment.date}
                - Time: {appointment.time}
                - Service: {appointment.service}
                - Amount: {appointment.amount or 'To be determined'}

                We will contact you soon for confirmation.

                Best regards,
                Clinic Team
                """
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [appointment.email],
                    fail_silently=False,
                )
                # Send notification to admin
                admin_subject = f'New Appointment Booked - {appointment.name}'
                admin_message = f"""
                New appointment booked:

                Name: {appointment.name}
                Email: {appointment.email}
                Phone: {appointment.phone}
                Date: {appointment.date}
                Time: {appointment.time}
                Service: {appointment.service}
                Amount: {appointment.amount or 'To be determined'}
                Message: {appointment.message}

                Please review and confirm.
                """
                send_mail(
                    admin_subject,
                    admin_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                messages.success(request, 'Appointment booked successfully! Confirmation email sent.')
                # Save the appointment only if emails succeed
                appointment.save()
                return redirect('appointment_success')  # Or redirect to a success page
            except BadHeaderError:
                messages.error(request, 'Invalid header found in email.')
            except Exception as e:
                messages.error(request, f'Failed to send confirmation email: {str(e)}')
                # Do not save if email fails
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})



def contact(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if not all([name, email, phone, subject, message]):
            messages.error(request, "All fields are required.")
            return redirect("contact")

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        messages.success(request, "Your message has been sent successfully.")
        return redirect("contact")


    return render(request, "contact.html")


def feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if not all([name, email, message]):
            messages.error(request, "All fields are required.")
            return redirect("feedback")

       
     

        feedback.objects.create(
            name=name,
            email=email,
            message=message,
            
        )


        messages.success(request, "Thanks for your feedback!")
        return redirect("feedback")

    return render(request, "feedback.html")

def appointment_success(request):
    return render(request, 'appointment_success.html')  # Create this template if needed, or use a message

def contact_success(request):
    return render(request, 'contact_success.html')  # Or redirect to contact with message

def feedback_success(request):
    return render(request, 'feedback_success.html')  # Or redirect to feedback with message

