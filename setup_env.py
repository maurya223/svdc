#!/usr/bin/env python
"""
Interactive script to help set up the .env file for email configuration.
This script will guide you through the process of setting up your email credentials.
"""

import os
import sys

def create_env_file():
    """Create or update the .env file with email configuration"""
    
    print("=" * 60)
    print("DJANGO EMAIL CONFIGURATION SETUP")
    print("=" * 60)
    print("This script will help you set up your email configuration.")
    print("Your .env file will be created/updated with the provided values.")
    print()
    
    # Check if .env already exists
    env_exists = os.path.exists('.env')
    if env_exists:
        print("⚠️  .env file already exists. This will append to it.")
        print("   If you want to start fresh, delete the .env file first.")
        print()
    
    # Get email configuration
    print("Please provide your email configuration:")
    print()
    
    email_host = input("Email Host (e.g., smtp.gmail.com): ").strip() or 'smtp.gmail.com'
    email_port = input("Email Port (e.g., 587): ").strip() or '587'
    email_use_tls = input("Use TLS? (y/n, default: y): ").strip().lower() or 'y'
    email_user = input("Email Address: ").strip()
    email_password = input("App Password (not your regular password): ").strip()
    
    # Get Django settings
    print()
    print("Django Settings:")
    secret_key = input("Secret Key (leave blank to generate): ").strip()
    debug_mode = input("Debug Mode? (y/n, default: y for development): ").strip().lower() or 'y'
    
    # Prepare content
    content = []
    
    if not env_exists:
        content.append("# Django Email Configuration")
        content.append("# This file contains sensitive information - DO NOT commit to version control")
        content.append("")
    
    content.append(f"EMAIL_HOST={email_host}")
    content.append(f"EMAIL_PORT={email_port}")
    content.append(f"EMAIL_USE_TLS={'True' if email_use_tls in ['y', 'yes', 'true'] else 'False'}")
    content.append(f"EMAIL_HOST_USER={email_user}")
    content.append(f"EMAIL_HOST_PASSWORD={email_password}")
    
    if secret_key:
        content.append(f"SECRET_KEY={secret_key}")
    else:
        content.append("# SECRET_KEY=your-secret-key-here (generate one: https://djecrety.ir/)")
    
    content.append(f"DEBUG={'True' if debug_mode in ['y', 'yes', 'true'] else 'False'}")
    
    # Write to file
    try:
        with open('.env', 'a' if env_exists else 'w') as f:
            f.write('\n'.join(content) + '\n')
        
        print()
        print("✅ .env file created/updated successfully!")
        print()
        print("Next steps:")
        print("1. Run: python test_email.py (to test your email configuration)")
        print("2. Run: python manage.py runserver")
        print("3. Visit: http://localhost:8000/appointment/ to test booking")
        print()
        print("📖 Refer to EMAIL_SETUP_GUIDE.md for detailed instructions")
        
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")
        return False
    
    return True

if __name__ == '__main__':
    try:
        create_env_file()
    except KeyboardInterrupt:
        print("\n\nSetup cancelled.")
        sys.exit(1)
