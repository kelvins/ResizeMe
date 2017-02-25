from django import forms

class UploadFileForm(forms.Form):

	# Image file
	file   = forms.ImageField()

	# Get the width and height fields
	width  = forms.IntegerField()
	height = forms.IntegerField()

	# Image formats
	CHOICES = [
		('jpg','jpg'),
		('png','png'),
		('bmp','bmp')
	]

	image_format = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())