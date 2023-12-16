# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Author: Varsha Sidaray Umarani
# Date :  04-November-2023
# About:  Automation Script that accepts directory name and extension of file from user.
# 		  and delete duplicate files of that specified extension from the specified folder.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Importing required modules
import os
import hashlib
from sys import *

# Function to calculate the checksum of file using hashlib
def Calculate_CheckSum(path,blocksize=1024):
	file = open(path,'rb')
	hobj = hashlib.md5()

	buffer = file.read(blocksize)
	while len(buffer) != 0:
		hobj.update(buffer)
		buffer = file.read(blocksize)

	file.close()
	return hobj.hexdigest()

# Function to traverse the directory and find duplicate files of specified extension present in specified directory
def Traverse_Directory(path):
	duplicate = {}
	iCnt = 0

	if not os.path.exists(path):
		print("Error : The path you entered doesn't exists.!")
		exit()

	for folder, subfolder, filename in os.walk(path):
		for file in filename:
			iCnt += 1
			actualpath = os.path.join(folder,file)
			hash = Calculate_CheckSum(actualpath)

			if hash in duplicate:					# If checksum is already present
				duplicate[hash].append(actualpath)
			else:
				duplicate[hash] = [actualpath]		# If checksum is not present

	print("Total Number of scanned files : ",iCnt)
	return duplicate

# Function to traverse the directory and delete duplicate files of specified extension present in specified directory
def Delete_Duplicates(duplicate,extension):
	Output = list(filter(lambda x: len(x) > 1,duplicate.values()))

	if len(Output) > 0:
		print("Duplicate files are present in specified directory")
	else:
		print("No duplicate files found in specified directory")
		return

	iCnt = 0
	deleted_files = 0

	for result in Output:
		iCnt = 0
		for path in result:
			iCnt += 1
			if iCnt >= 2 and extension in os.path.splitext(path):
				deleted_files += 1
				os.remove(path)

	print("Total Number of Duplicate files : ",deleted_files)
	print("Total Number of deleted files : ",deleted_files)

def main():
	print("----------------------  Script to Traverse Directory and Delete Duplicate files of specified extension  ----------------------")

	if len(argv) < 2:
		print("Error : Invalid Number of Arguments to Script.!!")
		exit()

	if (argv[1] == "-h") or (argv[1] == "-H"):
		print("Script Help : This Script works as Directory Traversal and Delete Duplicate Files of specified extension.!")
		exit()

	if (argv[1] == "-u") or (argv[1] == "-U"):
		print("Script Usage : Parameters - Application_Name.py Absolute Path of the Destination Directory Extension of file")
		exit()

	duplicate_files = Traverse_Directory(argv[1])

	Delete_Duplicates(duplicate_files,argv[2])

if __name__ == "__main__":
	main()