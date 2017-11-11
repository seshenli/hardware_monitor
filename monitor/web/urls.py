from django.conf.urls import url
from django.views.generic import RedirectView

from monitor.web import views

app_name = "monitor"
urlpatterns = [
    url(r'^$', RedirectView.as_view(url='index/', permanent=False), name='home'),
    url(r'^index/$', views.index, name="index"),
    url(r'^user/$', views.user, name="user"),
    url(r'^table/$', views.table, name="table"),
]
