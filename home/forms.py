from django.forms import ModelForm
from .models import Users
from django import forms


class UsersForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({
            'class': 'input100',
            'type': 'text',
            'name': 'username',
            'placeholder': "Введіть ім'я",
        })
        self.fields["user_email"].widget.attrs.update({
            'class': 'input100',
            'type': 'email',
            'name': 'email',
            'placeholder': "Введіть пошту",
        })

    class Meta:
        model = Users
        fields = ['name', 'user_email']
