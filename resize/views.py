from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from django.core.files.base import ContentFile
from django.template import loader
import os, random
from .forms import UploadFileForm
#from django.conf import settings
from PIL import Image
from wsgiref.util import FileWrapper
import tempfile

slogans = []
slogans.append('Resize any image to any size with few clicks!')
slogans.append('The simplest image resizing app!')
slogans.append('Just load an image, set the width and height, select an image format and click on RESIZE ME!')
slogans.append('This is an open source project created under the MIT license, feel free to contribute to the project on Github!')
slogans.append('If you liked the app please share with your friends!')
slogans.append('If you find any bug please create an issue on Github!')

def index(request):

	error_message = ''

	# If the method is POST
	if request.method == 'POST':

		# Get the form
		form = UploadFileForm(request.POST, request.FILES)

		# Check if the form is valid
		if form.is_valid():

			# Get the file data
			filedata = request.FILES['file']

			# If the file data is not null
			if filedata != None:

				# Get the width and height
				width  = int(request.POST['width'])
				height = int(request.POST['height'])

				# If the width is invalid (it should never happen because it is already validated in HTML and Javascript)
				if width <= 0 or width > 5000:
					width = 100

				# If the height is invalid (it should never happen because it is already validated in HTML and Javascript)
				if height <= 0 or height > 5000:
					height = 100

				image_format = request.POST['image_format']

				# If the image format is invalid, set the PNG as default
				if image_format != "jpg" and image_format != "png" and image_format != "bmp":
					image_format = "png"

				# The "image.save(tempFile, image_format)" function uses "jpeg" as the image format
				if image_format == "jpg":
					image_format = "jpeg"

				# Create an image object using the Pillow library
				image = Image.open(filedata)

				# Create a size variable using the width and height
				size = width, height

				# Resize the image using the width and height defined by the user
				image = image.resize(size, Image.ANTIALIAS)
				
				# Temp file (NamedTemporaryFile delete the file as soon as possible)
				tempFile = tempfile.NamedTemporaryFile()

				# Try to save the image in the MEDIA_ROOT
				try:
					image.save(tempFile, image_format)
					tempFile.seek(0)

					wrapper  = FileWrapper(tempFile)
					response = StreamingHttpResponse(wrapper, 'image/%s' % image_format)
					response['Content-Disposition'] = 'attachment; filename=resized_image.%s' % image_format

					return response

				except AttributeError:
					error_message = 'Error: unfortunately, we could not resize your image, please try again in a few seconds!'

	template = loader.get_template('resize/index.html')

	index = random.randint(0, len(slogans)-1)

	context = {
		'slogan': slogans[index],
		'error_message': error_message,
	}

	return HttpResponse(template.render(context, request))
