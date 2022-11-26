from django import forms
from django.contrib.auth import get_user_model
from webapp.models import Photo


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Поиск")


class PhotoForm(forms.ModelForm):
    author = get_user_model()

    class Meta:
        model = Photo
        fields = ('image', 'sign')

