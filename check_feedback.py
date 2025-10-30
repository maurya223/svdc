#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic.settings')
django.setup()

from home.models import Feedback

def check_feedback():
    print("Checking Feedback Model and Data...")
    print(f"Feedback model fields: {[f.name for f in Feedback._meta.fields]}")
    print(f"Total feedback objects: {Feedback.objects.count()}")

    feedbacks = Feedback.objects.all()
    if feedbacks:
        print("\nFeedback entries:")
        for f in feedbacks:
            print(f"ID: {f.id}")
            print(f"Name: {f.name}")
            print(f"Email: {f.email}")
            print(f"Rating: {f.rating}")
            print(f"Message: {f.message}")
            print(f"Date Created: {f.date_created}")
            print("-" * 50)
    else:
        print("No feedback entries found.")

if __name__ == '__main__':
    check_feedback()
