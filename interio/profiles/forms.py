from django import forms
from .models import Post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'autofocus', 'class':'form-control', 'placeholder':'Title'}))
    sub_title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sub-title'}))
    image=forms.FileField()
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}))

    class Meta:
        model = Post
        fields= ('title', 'sub_title', 'image', 'description')

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'autofocus', 'class':'form-control', 'placeholder':'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    
    class Meta:
        model = User
        fields=['username', 'first_name', 'last_name', 'email', 'password']

class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'autofocus', 'class':'form-control', 'placeholder':'Username'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    
    class Meta:
        model = User
        fields=['username', 'password']


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'autofocus', 'class':'form-control', 'placeholder':'Name'}))    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}))    
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Message'}))
    