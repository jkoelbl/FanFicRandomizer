from random import randint
from os import listdir, getcwd

def get_filenames():
	mypath = getcwd() + '\\stories'
	return [mypath + '\\' + f for f in listdir(mypath)]

def read_file(filename):
	with open(filename) as file:
		print(file.read())

def get_random_story():
	filenames = get_filenames()
	index = randint(0,len(filenames)-1)
	read_file(filenames[index])

get_random_story()