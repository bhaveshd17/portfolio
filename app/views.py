from django.shortcuts import redirect, render
from .models import Projects
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def home_view(request, *args, **kwargs):
    projects = Projects.objects.all().order_by("-id")
    context = {'projects': projects}
    return render(request, 'base.html', context=context, status=200)

def send_msg_email(request, *args, **kwargs):
    status = 200
    try:
        email_subject="Message From Bhavesh's Portfolio"
        email_body=render_to_string("mails/bhaveshmail.html",{
            "name": request.POST.get("name"),
            "msg": request.POST.get("msg")
        })

        email=EmailMessage(subject=email_subject,body=email_body,
        from_email=settings.EMAIL_HOST_USER,
        to=[request.POST.get("email")],
        cc=["bhaveshdhake8@gmail.com"]
        )
        
        email.fail_silently = False
        email.content_subtype = 'html'
        email.send()
    except:
        status = 505
    return redirect('/', status=status)
