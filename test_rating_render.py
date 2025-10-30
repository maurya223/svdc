#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic.settings')
django.setup()

from home.forms import FeedbackForm

def test_rating_render():
    print("Testing Rating Field Rendering...")

    form = FeedbackForm()
    print("Rating field widget:", form.fields['rating'].widget)
    print("Rating field choices:", form.fields['rating'].choices)

    # Render the rating field
    rating_html = str(form['rating'])
    print("Rating field HTML:")
    print(rating_html)

    # Test form with rating data
    form_with_data = FeedbackForm(data={'name': 'Test', 'email': 'test@test.com', 'message': 'Test', 'rating': 3})
    print("\nForm with rating=3 is valid:", form_with_data.is_valid())
    if not form_with_data.is_valid():
        print("Errors:", form_with_data.errors)

if __name__ == '__main__':
    test_rating_render()
