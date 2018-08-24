from django.shortcuts import render
from .scripts import *

# Create your views here.
def index(response):
	return render(response, 'index.html', \
		{'output': get_random_story()})