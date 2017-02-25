from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from django.core.files.base import ContentFile
from django.template import loader
import StringIO, os, mimetypes, random
from .forms import UploadFileForm
from django.conf import settings
from PIL import Image
from wsgiref.util import FileWrapper

slogans = []
slogans.append('Resize any image to any size with few clicks!')
slogans.append('The simplest image resizing app!')
slogans.append('Just load an image, set the width and height, and click on RESIZE ME!')

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
				width  = request.POST['width']
				height = request.POST['height']

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

				# Create an image object using the Pillow library
				image = Image.open(filedata)

				# Create a size variable using the width and height
				size = int(width), int(height)

				# Resize the image using the width and height defined by the user
				image = image.resize(size, Image.ANTIALIAS)

				# Create a "unique" file name
				#magicNumber = random.randint(0, 9999999)
				#filename = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f') + "_" + str(magicNumber) + "." + str(image_format)
				filename = "resized_image." + str(image_format)
				filepath = settings.MEDIA_ROOT + "\\" + filename

				# Try to save the image in the MEDIA_ROOT
				try:
					image.save( filepath )

					file = os.path.basename(filepath)
					chunk_size = 8192
					response = StreamingHttpResponse(FileWrapper(open(filepath, 'rb'), chunk_size), content_type=mimetypes.guess_type(filepath)[0])
					response['Content-Length'] = os.path.getsize(filepath)    
					response['Content-Disposition'] = "attachment; filename=%s" % file
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
