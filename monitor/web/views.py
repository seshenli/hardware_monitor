from django.http import QueryDict, HttpResponse
from django.shortcuts import render
from django.core import serializers

import json
import logging

from monitor.authentication.modelForm import WebUserForm
from monitor.authentication.models import WebUser

logger = logging.getLogger(__name__)


def index(request):
    return render(request, "index.html")


# def index(request):
#     return render(request, "table.html")


def user(request):

    return render(request, "user.html")


def table(request):
    return render(request, "table.html")


def update_user(request):
    result = {}
    web_user = WebUserForm(request.POST)

    if web_user.is_valid():
        web_user.save()
    else:
        print("xxxxxxxxxxxxxxxx")

    result['success'] = True
    result['message'] = "ok"
    return HttpResponse(json.dumps(result))
