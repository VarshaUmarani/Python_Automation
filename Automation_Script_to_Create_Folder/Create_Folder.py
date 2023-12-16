# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Author: Varsha Sidaray Umarani
# Date :  27-October-2023
# About:  Automation Script to Create Folder in specified directory.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Importing required modules
import os
import time
import psutil
from sys import *

# Function to create folder in specified directory
def Create_Folder(FolderName):
	if not os.path.exists(FolderName):
		os.mkdir(FolderName)
	else:
		print("Destination directory is already present.!")
		exit()

def main():
	print("--------------- Automation Script to Create Directory ---------------")

	print("Script Title : ",argv[0])

	if (len(argv) != 2):
		print("Error : Insufficient Argument to the script.!")
		exit()

	if (argv[1] == "-u") or (argv[1] == "-U"):
		print("Script Usage : Run the script as parameter followed by file name.!")
		exit()

	if (argv[1] == "-h") or (argv[1] == "-H"):
		print("Script Help : Automation Script to Create Directory")
		exit()

	process = Create_Folder(argv[1])

if __name__ == "__main__":
	main()