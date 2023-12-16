# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Author: Varsha Sidaray Umarani
# Date :  02-November-2023
# About:  Automation Script to traverse files, folders and subfolders present in particular
#		  directory and delete all the duplicate files present in the particular folder.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Importing required modules
import os
import hashlib
from sys import *

# Function to calculate the checksum of file using hashlib
def CalculateCheckSum(path,blocksize = 1024):
	fd = open(path,"rb")
	hobj = hashlib.md5()

	buffer = fd.read(blocksize)
	while len(buffer) > 0:
		hobj.update(buffer)
		buffer = fd.read(blocksize)

	fd.close()
	return hobj.hexdigest()

# Function to traverse the directory and find duplicate files present in specified directory
def DirectoryTraversal(path):
	duplicate = {}		# Dictionary to hold checksum and file name
	iCnt = 0

	if not os.path.exists(path):
		print("Error : The path you entered doesn't exists.!")
		exit()

	for Folder, Subfolder, Filename in os.walk(path):
		for file in Filename:
			iCnt = iCnt + 1
			actualpath = os.path.join(Folder,file)
			hash = CalculateCheckSum(actualpath)
			
			if hash in duplicate:					# If checksum is already present
				duplicate[hash].append(actualpath)
			else:
				duplicate[hash] = [actualpath]		# If checksum is not present

	print("Number of Total Files Scanned is :",iCnt)
	return duplicate

# Function to traverse the directory and find duplicate files present in specified directory
def FindDuplicate(duplicate):
	output = list(filter(lambda x : len(x) > 1,duplicate.values()))

	if len(output) > 0:
		print("There are duplicate files in specified directory.!")

	iCnt = 0
	i = 0
	Arr = []
	for result in output:
		iCnt = 0
		for path in result:
			iCnt = iCnt + 1
			if iCnt >= 2:
				i = i + 1
				Arr.append(path)

	if i == 0:
		print("No duplicate files found in specified directory")
		exit()
	else:
		print("Number of Duplicate files found : ",i)
		return Arr

# Function to traverse the directory and delete duplicate files present in specified directory
def DeleteDuplicate(Arr):
	iCnt = 0
	for i in range(len(Arr)):
		if prompt.lower() == "yes":
			iCnt = iCnt + 1
			os.remove(Arr[i])
		elif prompt.lower() == "no":
			continue
		else:
			print("Error : Invalid Input....!!!!")
			continue

	print("Total Number of Files deleted :",iCnt)

def main():
	Arr = {}

	print("-------------------------- Script for Directory Traversal and Duplicate Files Cleaner -------------------------")

	if len(argv) != 2:
		print("Error : Insufficient Argument to the script.!")
		exit()

	if (argv[1] == "-h") or (argv[1] == "-H"):
		print("Script Help : This Script works as Directory Traversal and Delete Duplicate Files.!")
		exit()

	if (argv[1] == "-u") or (argv[1] == "-U"):
		print("Script Usage : Parameters - Application_Name.py Absolute Path of the Destination Directory")
		exit()

	files = DirectoryTraversal(argv[1])
	duplicate_files = FindDuplicate(files)
	
	DeleteDuplicate(duplicate_files)

if __name__ == "__main__":
	main()