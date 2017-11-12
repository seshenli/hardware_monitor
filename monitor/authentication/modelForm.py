from django.forms import ModelForm

from monitor.authentication.models import WebUser


class WebUserForm(ModelForm):
    class Meta:
        model = WebUser
        fields = '__all__'
