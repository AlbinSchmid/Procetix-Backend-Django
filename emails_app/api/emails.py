from django_rq import job
from rq import Retry
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


@job('default', retry=Retry(max=3, interval=[10, 30, 60]))
def send_contact_email(name, email, phone, message):
    """
    Function to send a contact email.

    Args:
        name (str): Name of the person submitting the contact form.
        email (str): Email address of the person.
        phone (str): Phone number of the person.
        message (str): Message content from the contact form.
    """
    subject = f"Contact Form Submission from {name}"
    from_email = 'noreply@procetix.com'
    to = ['contact@albin-schmid.com']

    html_content = render_to_string('emails/contact.html', {
        'name': name,
        'email': email,
        'phone': phone,
        'message': message
    })

    text_content = 'Neue Kontaktanfrage'

    email = EmailMultiAlternatives(subject, text_content, from_email, to)
    email.attach_alternative(html_content, "text/html")
    email.send()
