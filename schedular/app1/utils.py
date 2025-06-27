from django.core.mail import send_mail
from datetime import datetime

def send_daily_report():
    subject = 'Daily Report'
    message = f"Hello Admin,\n\nThis is your daily report.\nTime: {datetime.now()}"
    from_email = 'pavanram63055@gmail.com'
    recipient_list = ['ramagiripavan242@gmail.com']
    fail_silently=False
    
    send_mail(subject, message, from_email, recipient_list)
    return "Email sent successfully"
