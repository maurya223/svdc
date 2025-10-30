#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic.settings')
django.setup()

from home.forms import FeedbackForm
from home.models import Feedback

def test_feedback_form():
    print("Testing Feedback Form...")

    # Test valid data
    valid_data = {
        'name': 'Test User',
        'email': 'test@example.com',
        'message': 'Great service!',
        'rating': 5
    }
    form = FeedbackForm(data=valid_data)
    print(f"Form is valid: {form.is_valid()}")
    if not form.is_valid():
        print(f"Form errors: {form.errors}")
    else:
        obj = form.save()
        print(f"Saved feedback: {obj.name}, Rating: {obj.rating}")

    # Test invalid data (missing required fields)
    invalid_data = {
        'name': '',
        'email': 'invalid-email',
        'message': '',
        'rating': ''
    }
    form_invalid = FeedbackForm(data=invalid_data)
    print(f"Invalid form is valid: {form_invalid.is_valid()}")
    print(f"Invalid form errors: {form_invalid.errors}")

    # Check model fields
    print(f"Feedback model fields: {[f.name for f in Feedback._meta.fields]}")
    print(f"Current feedback count: {Feedback.objects.count()}")

if __name__ == '__main__':
    test_feedback_form()
