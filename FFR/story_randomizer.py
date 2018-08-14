from os import listdir
from random import randint

#get and return filenames in stories path
def get_filenames():
	mypath = getcwd() + '\\stories'
	return [mypath + '\\' + f for f in listdir(mypath)]
	
#read file by every 256 bytes to save on mem
def read_file(filename):
	byte_size = 256
	with open(filename) as file:
		temp = file.read(byte_size)
		while temp:
			print(temp, end='')
			temp = file.read(byte_size)

#get filenames, pick one at random, and read it
def get_random_story():
	filenames = get_filenames()
	index = randint(0,len(filenames)-1)
	read_file(filenames[index])