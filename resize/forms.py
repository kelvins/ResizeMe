from django import forms

class UploadFileForm(forms.Form):

	file   = forms.ImageField()
	width  = forms.IntegerField()
	height = forms.IntegerField()

	CHOICES = [
		('jpg','jpg'),
		('png','png'),
		('bmp','bmp')
	]

	image_format = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())