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



#Edit user and Avatar
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Change e-mail")
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput) 
    first_name = forms.CharField(label="Name", max_length=50, required=False)
    last_name = forms.CharField(label="Last Name", max_length=50, required=False)

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name' ] 
        help_texts = { k:"" for k in fields}


class AvatarForm(forms.Form):
    image = forms.ImageField(required=True)     