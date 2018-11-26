from django.conf import settings
from django.http import Http404
from django.shortcuts import redirect, render

from .models import Link


def redirect_(request, key):
    try:
        link = Link.find_by_key(key.lower())

    except Link.DoesNotExist:
        raise Http404("Link does not exist.")

    return redirect(link.url, permanent=settings.PERMANENT_REDIRECT)


def homepage(request):
    return render(request, "homepage.html")
