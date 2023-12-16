# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Author: Varsha Sidaray Umarani
# Date :  04-November-2023
# About:  Automation Script that accepts directory name from user and sort all the files
#		  according to extension of files by creating separate folder for each type of extension.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Importing required modules
import os
import shutil
from sys import *

# Function to sort the files accroding to their extension in separate folder
def Arrange_Files(path):
	if not os.path.exists(path):
		print("Error : The path you entered doesn't exists.!")
		exit()

	for folder,subfolder,filename in os.walk(path):
		for file in filename:
			actualpath = os.path.join(folder,file)
			ext = actualpath.split('.')[-1]
			extension = os.path.join(path,ext)
			filepath = os.path.join(extension,file)

			if not os.path.exists(extension):
				os.mkdir(extension)
				shutil.move(actualpath,extension)
			else:
				if not os.path.isfile(filepath):
					shutil.move(actualpath,extension)

	print("All the files are sorted in folder according to their extension.!")

def main():
	print("----------------------  Script to Traverse Directory and arrange files according to their extension  ----------------------")

	if len(argv) != 2:
		print("Error : Invalid Number of Arguments to Script.!!")
		exit()

	if (argv[1] == "-h") or (argv[1] == "-H"):
		print("Script Help : This Script works as Directory Traversal and arrange the files according to their extension.!")
		exit()

	if (argv[1] == "-u") or (argv[1] == "-U"):
		print("Script Usage : Parameters - Application_Name.py Absolute Path of the Destination Directory Extension of file")
		exit()

	Arrange_Files(argv[1])

if __name__ == "__main__":
	main()