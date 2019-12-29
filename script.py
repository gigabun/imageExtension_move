import os, shutil 

destination_directory = '/home/giovanna/all_images/'

directories = set([
	'/home/giovanna/', 
	'/home/giovanna/Downloads/'
	])

for directory in directories:
	for file in os.listdir(directory):
		if file.endswith('.jpeg') or file.endswith('.png'):
			shutil.move('{}{}'.format(directory, file), destination_directory)