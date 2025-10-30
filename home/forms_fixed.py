from django import forms
from .models import Appointment, Contact, Feedback
from django.core.exceptions import ValidationError
from datetime import date

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'date', 'time', 'service', 'amount', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number',
                'pattern': '[0-9]{10}',
                'title': 'Please enter a valid 10-digit phone number'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'min': str(date.today()),
                'required': True
            }),
            'time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',
                'required': True
            }),
            'service': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Final Amount',
                'min': '0',
                'step': '0.01'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Any additional details or special requirements...',
                'rows': 4
            }),
        }
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'date': 'Preferred Date',
            'time': 'Preferred Time',
            'service': 'Service Type',
            'amount': 'Final Amount',
            'message': 'Additional Notes'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Use the service choices from the model to ensure consistency
        from .models import Appointment
        self.fields['service'].choices = [('', 'Select a service')] + list(Appointment.SERVICES)

        # Make amount field optional
        self.fields['amount'].required = False
        self.fields['phone'].required = False
        self.fields['message'].required = False

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.isdigit():
            raise ValidationError('Phone number should contain only digits.')
        if phone and len(phone) != 10:
            raise ValidationError('Phone number should be 10 digits.')
        return phone

    def clean_date(self):
        selected_date = self.cleaned_data.get('date')
        if selected_date and selected_date < date.today():
            raise ValidationError('Appointment date cannot be in the past.')
        return selected_date

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if date and time:
            # Check for existing appointments at the same date/time
            existing = Appointment.objects.filter(
                date=date,
                time=time,
                status__in=['Pending', 'Confirmed']
            ).exists()

            if existing:
                raise ValidationError(
                    'This time slot is already booked. Please choose another time.'
                )

        return cleaned_data


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Phone Number'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your Message',
                'rows': 5,
                'required': True
            }),
        }
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'subject': 'Subject',
            'message': 'Message'
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.isdigit():
            raise ValidationError('Phone number should contain only digits.')
        if phone and len(phone) != 10:
            raise ValidationError('Phone number should be 10 digits.')
        return phone


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your Feedback',
                'rows': 5,
                'required': True
            }),
            'rating': forms.RadioSelect(attrs={
                'class': 'rating-radio',
                'required': True
            }),
        }
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'message': 'Feedback Message',
            'rating': 'Rating (1-5)'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'].choices = [(i, f'{i} Star{"s" if i > 1 else ""}') for i in range(1, 6)]

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating and (rating < 1 or rating > 5):
            raise ValidationError('Rating must be between 1 and 5.')
        return rating
