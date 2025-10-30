#!/usr/bin/env python
"""
Test script to verify email configuration is working properly.
Run this script to test your email setup before testing the appointment form.
"""

import os
import sys
import django
from decouple import config

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic.settings')
django.setup()

from django.core.mail import send_mail

def test_email_configuration():
    """Test if email configuration is working"""
    print("Testing email configuration...")
    
    # Check if required environment variables are set
    required_vars = ['EMAIL_HOST_USER', 'EMAIL_HOST_PASSWORD']
    missing_vars = []
    
    for var in required_vars:
        try:
            value = config(var)
            if not value:
                missing_vars.append(f"{var} (empty)")
            else:
                print(f"✓ {var}: {'*' * len(value)} (set)")
        except:
            missing_vars.append(var)
    
    if missing_vars:
        print(f"\n❌ Missing or empty environment variables: {', '.join(missing_vars)}")
        print("Please update your .env file with the following:")
        print("EMAIL_HOST_USER=your-email@gmail.com")
        print("EMAIL_HOST_PASSWORD=your-app-password")
        print("\nRefer to EMAIL_SETUP_GUIDE.md for detailed instructions.")
        return False
    
    # Try to send a test email
    try:
        print("\nAttempting to send test email...")
        send_mail(
            subject='Test Email from Django Portfolio',
            message='This is a test email to verify your email configuration is working correctly.',
            from_email=config('EMAIL_HOST_USER'),
            recipient_list=[config('EMAIL_HOST_USER')],  # Send to yourself
            fail_silently=False,
        )
        print("✓ Test email sent successfully!")
        print("Check your inbox for the test email.")
        return True
        
    except Exception as e:
        error_msg = str(e)
        print(f"\n❌ Failed to send test email: {error_msg}")
        
        # Provide specific troubleshooting advice
        if "authentication failed" in error_msg.lower() or "bad credentials" in error_msg.lower():
            print("\n🔧 Troubleshooting:")
            print("1. Make sure you're using an App Password, not your regular password")
            print("2. Verify 2-Step Verification is enabled in your Google account")
            print("3. Check that the email and password in .env are correct")
            
        elif "connection refused" in error_msg.lower():
            print("\n🔧 Troubleshooting:")
            print("1. Check your internet connection")
            print("2. Verify firewall/antivirus isn't blocking the connection")
            print("3. Try using a different network")
            
        else:
            print("\n🔧 Check your email configuration in the .env file")
            
        return False

if __name__ == '__main__':
    print("=" * 50)
    print("DJANGO EMAIL CONFIGURATION TEST")
    print("=" * 50)
    
    success = test_email_configuration()
    
    print("\n" + "=" * 50)
    if success:
        print("✅ Email configuration test PASSED!")
        print("Your appointment booking should work correctly.")
    else:
        print("❌ Email configuration test FAILED!")
        print("Please fix the issues above before testing the appointment form.")
    print("=" * 50)
