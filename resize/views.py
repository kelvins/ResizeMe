#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
	template = loader.get_template('resize/index.html')
	context = {
		'name': 'Django',
	}
	return HttpResponse(template.render(context, request))
