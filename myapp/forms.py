from django import forms
from django.forms import ModelForm
from .models import ImageUpload

class ImageForm(ModelForm):
    class Meta:
        model = ImageUpload
        fields = '__all__'


