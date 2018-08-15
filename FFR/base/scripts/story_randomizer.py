from os import listdir, getcwd
from random import randint

mypath = getcwd() + '\\stories'
byte_size = 256

#get and return filenames in stories path
def get_filenames():
	return [mypath + '\\' + f for f in listdir(mypath)]
	
#read file by every 256 bytes to save on mem
def read_file(filename):
	with open(filename) as file:
		temp = file.read(byte_size)
		while temp:
			print(temp, end='')
			temp = file.read(byte_size)

#get filenames, pick one at random, and read it
def get_random_story():
	filenames = get_filenames()
	index = randint(0,len(filenames)-1)
	return filenames[index]