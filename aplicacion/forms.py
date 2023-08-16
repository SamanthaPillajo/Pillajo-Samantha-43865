from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BusquedaForm(forms.Form):
    termino_busqueda = forms.CharField(label='Buscar', max_length=100)


#Register
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Username")
    password1= forms.CharField(label="Password", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}    