# Email Configuration Guide for Django Portfolio

## Step 1: Create/Update .env File

Create a `.env` file in your project root directory with the following content:

```
# Django Settings
SECRET_KEY=your-django-secret-key-here
DEBUG=True

# Email Configuration (GMAIL EXAMPLE)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password-here
```

## Step 2: Gmail App Password Setup

For Gmail, you need to generate an App Password (NOT your regular password):

1. Go to: https://myaccount.google.com/
2. Enable 2-Step Verification if not already enabled
3. Go to "Security" → "2-Step Verification" → "App Passwords"
4. Generate a new app password for "Mail"
5. Use this app password as `EMAIL_HOST_PASSWORD`

## Step 3: Alternative Email Providers

If using other providers, use these settings:

### Outlook/Hotmail:
```
EMAIL_HOST=smtp.office365.com
EMAIL_PORT=587
```

### Yahoo:
```
EMAIL_HOST=smtp.mail.yahoo.com
EMAIL_PORT=587
```

## Step 4: Railway Deployment

When deploying to Railway, set these environment variables in your Railway dashboard:

- `SECRET_KEY`
- `DEBUG` (set to `False` for production)
- `EMAIL_HOST`
- `EMAIL_PORT` 
- `EMAIL_USE_TLS`
- `EMAIL_HOST_USER`
- `EMAIL_HOST_PASSWORD`

## Step 5: Testing Email Functionality

Run the development server and test the appointment booking form:

```bash
python manage.py runserver
```

Visit: http://localhost:8000/appointment/

## Troubleshooting

### Common Issues:
1. **Bad Credentials**: Ensure you're using an App Password, not your regular password
2. **Connection Refused**: Check firewall/antivirus settings
3. **Authentication Failed**: Verify 2-Step Verification is enabled

### Development Fallback:
If email fails in development, the system will still book appointments but show a warning message.

## Security Notes

- Never commit your `.env` file to version control
- Use different email accounts for development and production
- Regularly rotate app passwords for security
