from django.shortcuts import render

from monitor.authentication.models import WebUser
import logging

logger = logging.getLogger(__name__)


def index(request):
    return render(request, "index.html")


# def index(request):
#     return render(request, "table.html")


def user(request):
    return render(request, "user.html")


def table(request):
    return render(request, "table.html")


def update_user(requset):
    requset.POST
    return ""
