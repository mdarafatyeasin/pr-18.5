from django import forms
# from .models import Author
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# custom from 
# class AuthorForm(forms.ModelForm):
#     class Meta :
#         model = Author
#         fields = '__all__'

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'id_required'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


# change user data from 
class ChangeUserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',]
        # fields = "__all__"