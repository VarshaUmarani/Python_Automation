# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Author: Varsha Sidaray Umarani
# Date :  02-November-2023
# About:  Automation Script to traverse files, folders and subfolders present in particular 
#         directory and display all the duplicate files present in the particular folder.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Importing required modules
import os
import hashlib
from sys import *

# Function to calculate the checksum of file using hashlib
def Calculate_CheckSum(path,blocksize = 1024):
	fd = open(path,'rb')
	hobj = hashlib.md5()

	buffer = fd.read(blocksize)
	while len(buffer) != 0:
		hobj.update(buffer)
		buffer = fd.read(blocksize)

	fd.close()
	return hobj.hexdigest()

# Function to traverse the directory and find duplicate files present in specified directory
def Directory_Traversal(path):
	# Dictionary to hold checksum and name of duplicate files
	duplicates = {}
	iCnt = 0

	if not os.path.exists(path):
		print("Error : The path you entered doesn't exists.!")
		exit()

	for folder,subfolder,file_name in os.walk(path):
		#print("Directory name is : ",folder)
		#for sub in subfolder:
			#print("Subfolder of",folder,"is : ",sub)
		for file in file_name:
			#print("File name is : ",file)
			iCnt += 1
			actualpath = os.path.join(folder,file)
			hash = Calculate_CheckSum(actualpath)

			if hash in duplicates:
				duplicates[hash].append(actualpath)		# If the checksum is already present
			else:
				duplicates[hash] = [actualpath]			# If the Checksum is not present

	print("Number of Total Files Scanned is :",iCnt)
	return duplicates

# Function to traverse the directory and display duplicate files present in specified directory
def Display_DuplicateFiles(duplicates):
	Output = list(filter(lambda x:len(x) > 1,duplicates.values()))

	if not len(Output) != 0:
		print("There are no duplicate files in specified directory.!")
		return

	print("List of duplicate files are : ")
	
	iCnt = 0
	for result in Output:
		iCnt = 0
		for path in result:
			iCnt += 1
			if iCnt >= 2:
				print(path)

def main():
	print("-------------------------- Script for Directory Traversal and Display Duplicate Filename -------------------------")

	if len(argv) != 2:
		print("Error : Insufficient Argument to the script.!")
		exit()

	if (argv[1] == "-h") or (argv[1] == "-H"):
		print("Script Help : This Script works as Directory Traversal and Display Duplicate Files.!")
		exit()

	if (argv[1] == "-u") or (argv[1] == "-U"):
		print("Script Usage : Parameters - Application_Name.py Absolute Path of the Destination Directory")
		exit()

	Result = Directory_Traversal(argv[1])

	Display_DuplicateFiles(Result)

if __name__ == "__main__":
	main()