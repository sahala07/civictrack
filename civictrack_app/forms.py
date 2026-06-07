from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Issue


class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

        widgets = {

            'username': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class IssueForm(forms.ModelForm):

    class Meta:

        model = Issue

        fields = [
            'title',
            'category',
            'description',
            'location',
            'image'
        ]

        widgets = {

            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Complaint Title'
                }
            ),

            'category': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5,
                    'placeholder': 'Describe the issue'
                }
            ),

            'location': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Location'
                }
            ),
        }


class IssueUpdateForm(forms.ModelForm):

    class Meta:

        model = Issue

        fields = [
            'status',
            'resolution_note',
            'resolution_image'
        ]

        widgets = {

            'status': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'resolution_note': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Authority remarks'
                }
            ),
        }