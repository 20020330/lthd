from typing import Any
from django import forms
from django.forms import MultiWidget

from .models import Post


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'})
    )

class RegisterForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100, required=True)
    email = forms.EmailField(label="Email", required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    c_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput())

    # validation
    def clean(self) -> dict[str, Any]:
        if self.cleaned_data['password'] != self.cleaned_data['c_password']:
            raise forms.ValidationError("Passwords don't match")
        return super().clean()
    
# Post section
    
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 
                  'slug',
                  'description', 
                  'content',
                  'keyword',]
        exclude = ['author'],
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Slug'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content'}),
            'keyword': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Keyword'}),
        }
    