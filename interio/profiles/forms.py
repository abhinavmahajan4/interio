from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'autofocus', 'class':'form-control', 'placeholder':'Title'}))
    sub_title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sub-title'}))
    image=forms.FileField()
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}))

    class Meta:
        model = Post
        fields= ('title', 'sub_title', 'image', 'description')