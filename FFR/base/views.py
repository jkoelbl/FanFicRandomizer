from django.shortcuts import render
import randomize

# Create your views here.
def index(response):
	return render(response, 'index.html')

def output(request):
	if request.is_ajax():
		filename = randomize()
		with open('stories\\' + filename) as file:
			return render(request, 'output.html', {'output': file.read()})