# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Author: Varsha Sidaray Umarani
# Date :  30-October-2023
# About:  Automation Script to traverse files, folders and subfolders present in particular directory.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Importing required modules
import os
from sys import *

# Function to traverse the specified directory
def Directory_Traversal(path):
	iCnt = 0

	if not os.path.exists(path):
		print("Error : The path you entered doesn't exists.!")
		exit()

	print("Contents of the Directory are : ")

	for folder,subfolder,file_name in os.walk(path):
		print("Directory name is : ",folder)
		for sub in subfolder:
			print("Subfolder of",folder,"is : ",sub)
		for file in file_name:
			iCnt += 1
			print("File name is : ",file)

	print("Number of Total Files Scanned is :",iCnt)

def main():
	print("-------------------------- Automation Script for Directory Traversal -------------------------")

	if len(argv) != 2:
		print("Error : Insufficient Argument to the script.!")
		exit()

	if (argv[1] == "-h") or (argv[1] == "-H"):
		print("Script Help : Automation Script for Directory Traversal.!")
		exit()

	if (argv[1] == "-u") or (argv[1] == "-U"):
		print("Script Usage : Parameters - Application_Name.py Absolute Path of the Destination Directory")
		exit()

	Directory_Traversal(argv[1])	

if __name__ == "__main__":
	main()