from django import forms
from django.contrib.auth.models import User

from .models import Profile, Note


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password'
        ]


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = [
            'bio'
        ]


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'title',
            'content'
        ]