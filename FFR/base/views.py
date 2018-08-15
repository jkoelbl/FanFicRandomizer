from django.shortcuts import render
from .scripts import *

# Create your views here.
def index(response):
	return render(response, 'index.html')

def output(request):
	if request.is_ajax():
		filename = get_random_story()
		with open('stories\\' + filename) as file:
			return render(request, 'index.html', {'output': file.read()})