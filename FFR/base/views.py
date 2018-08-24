from django.shortcuts import render
from .scripts import *

# Create your views here.
def index(response):
	output = {
	'output': get_random_story()\
	}
	return render(response, 'index.html', output)