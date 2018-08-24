from os import listdir, getcwd
from random import randint

mypath = getcwd() + '\\base\\stories'
byte_size = 256

# get and return filenames in stories path
def get_filenames():
	return [mypath + '\\' + f for f in listdir(mypath)]

# get filenames, picks one at random, and returns it
def select_random_file():
	filenames = get_filenames()
	index = randint(0,len(filenames)-1)
	return filenames[index]

# reads random file as a whole
def get_random_story():
	filename = select_random_file()
	with open(filename) as file:
		return file.read()
