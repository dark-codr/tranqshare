from __future__ import absolute_import, unicode_literals

from django.core.mail import EmailMessage


def plain_email(to_email, subject, body):
    message = EmailMessage(subject=subject, body=body, to=[to_email])
    message.content_subtype = "html"
    message.send()

def support_email(to_email, subject, body, from_email):
    message = EmailMessage(subject=f"New Support Mail - {subject}", body=body, to=[to_email], bcc=["admin@tranqshare.com"], reply_to=[from_email])
    message.content_subtype = "html"
    message.send()


def pdf_attachment_email(to_email, subject, body, filepath, filename):
    message = EmailMessage(subject=f"New Quotation - {subject}", body=body, to=[to_email], bcc=["admin@tranqshare.com"], reply_to=["support@tranqshare.com"])
    file_data = open(filepath, "rb")
    message.attach(filename, file_data.read(), "application/pdf")
    message.content_subtype = "html"
    file_data.close()
    message.send()
