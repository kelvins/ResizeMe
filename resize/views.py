#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import random
import StringIO
import datetime
from PIL import Image
from .forms import UploadFileForm
from django.core.files.base import ContentFile

def index(request):

	if request.method == 'POST':

		form = UploadFileForm(request.POST, request.FILES)

		if form.is_valid():

			filedata = request.FILES['file']

			if filedata != None:

				width = request.POST['width']
				height = request.POST['height']
				image_format = request.POST['image_format']
				print(image_format)
				image = Image.open(filedata)
				size = int(width), int(height)
				image = image.resize(size, Image.ANTIALIAS)

				magicNumber = random.randint(0, 9999999)
				filename = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f') + "_" + str(magicNumber) + "." + str(image_format)

				try:
					image.save('C:/Users/Kelvin/Desktop/Django/resizeme/resize/static/imgs/' + filename)
				except AttributeError:
					print("Couldn't save image {}".format(image))

				return HttpResponseRedirect('static/imgs/' + filename)

		else:

			template = loader.get_template('resize/index.html')

			slogans = []
			slogans.append('Resize any image to any size with few clicks!')
			slogans.append('The simplest image resizing app!')
			slogans.append('Just load an image, set the width and height, and click on RESIZE ME!')

			index = random.randint(0, len(slogans)-1)

			context = {
				'slogan': slogans[index],
			}

			return HttpResponse(template.render(context, request))

	else:

		template = loader.get_template('resize/index.html')

		slogans = []
		slogans.append('Resize any image to any size with few clicks!')
		slogans.append('The simplest image resizing app!')
		slogans.append('Just load an image, set the width and height, and click on RESIZE ME!')

		index = random.randint(0, len(slogans)-1)

		context = {
			'slogan': slogans[index],
		}

		return HttpResponse(template.render(context, request))
