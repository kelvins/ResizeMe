#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from django.core.files.base import ContentFile
from django.template import loader
import random, StringIO, datetime, os, mimetypes
from .forms import UploadFileForm
from django.conf import settings
from django.shortcuts import redirect
from PIL import Image
from wsgiref.util import FileWrapper

slogans = []
slogans.append('Resize any image to any size with few clicks!')
slogans.append('The simplest image resizing app!')
slogans.append('Just load an image, set the width and height, and click on RESIZE ME!')

def index(request):

	if request.method == 'POST':

		form = UploadFileForm(request.POST, request.FILES)

		if form.is_valid():

			filedata = request.FILES['file']

			if filedata != None:

				width = request.POST['width']
				height = request.POST['height']
				image_format = request.POST['image_format']

				image = Image.open(filedata)
				size = int(width), int(height)
				image = image.resize(size, Image.ANTIALIAS)

				magicNumber = random.randint(0, 9999999)
				#filename = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f') + "_" + str(magicNumber) + "." + str(image_format)
				filename = "resized_image." + str(image_format)

				try:
					image.save( settings.MEDIA_ROOT + "\\" + filename )
				except AttributeError:
					print("Couldn't save image {}".format(image))

				the_file = settings.MEDIA_ROOT + "\\" + filename
				filename = os.path.basename(the_file)
				chunk_size = 8192
				response = StreamingHttpResponse(FileWrapper(open(the_file, 'rb'), chunk_size), content_type=mimetypes.guess_type(the_file)[0])
				response['Content-Length'] = os.path.getsize(the_file)    
				response['Content-Disposition'] = "attachment; filename=%s" % filename
				return response

		else:

			template = loader.get_template('resize/index.html')

			index = random.randint(0, len(slogans)-1)

			context = {
				'slogan': slogans[index],
			}

			return HttpResponse(template.render(context, request))

	else:

		template = loader.get_template('resize/index.html')

		index = random.randint(0, len(slogans)-1)

		context = {
			'slogan': slogans[index],
		}

		return HttpResponse(template.render(context, request))
