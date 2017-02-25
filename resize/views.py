#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import random

def index(request):

	if request.method == 'POST':

		template = loader.get_template('resize/index.html')

		slogans = []
		slogans.append('Resize any image to any size with few clicks!')
		slogans.append('The simplest image resizing app!')
		slogans.append('Just load an image, set the width and height and click on RESIZE ME!')

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
		slogans.append('Just load an image, set the width and height and click on RESIZE ME!')

		index = random.randint(0, len(slogans)-1)

		context = {
			'slogan': slogans[index],
		}

		return HttpResponse(template.render(context, request))