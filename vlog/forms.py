from django import forms
from .models import Post

class ImageModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {'image':''}
