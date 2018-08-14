from random import randint
from os import listdir, getcwd

def get_filenames():
	mypath = getcwd() + '\\stories'
	return [mypath + '\\' + f for f in listdir(mypath)]

def read_file(filename):
	with open(filename) as file:
		temp = file.read(256)
		while temp:
			print(temp, end='')
			temp = file.read(256)

def get_random_story():
	filenames = get_filenames()
	index = randint(0,len(filenames)-1)
	read_file(filenames[index])

get_random_story()