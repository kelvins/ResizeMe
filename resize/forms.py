from django import forms

class UploadFileForm(forms.Form):
    file = forms.ImageField()
    width = forms.IntegerField()
    height = forms.IntegerField()