from django.shortcuts import render
from .models import Projects


def home_view(request, *args, **kwargs):
    projects = Projects.objects.all().order_by("-id")
    context = {'projects': projects}
    return render(request, 'base.html', context=context, status=200)
