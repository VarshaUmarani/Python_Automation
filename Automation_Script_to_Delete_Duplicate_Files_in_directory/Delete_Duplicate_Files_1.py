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
	
	if not os.path.exists(path):
		print("Error : The path you entered doesn't exists.!")
		exit()

	# Dictionary to hold checksum and name of duplicate files
	duplicates = {}

	for folder,subfolder,file_name in os.walk(path):
		#print("Directory name is : ",folder)
		#for sub in subfolder:
			#print("Subfolder of",folder,"is : ",sub)
		for file in file_name:
			#print("File name is : ",file)
			actualpath = os.path.join(folder,file)
			hash = Calculate_CheckSum(actualpath)

			if hash in duplicates:
				duplicates[hash].append(actualpath)		# If the checksum is already present
			else:
				duplicates[hash] = [actualpath]			# If the Checksum is not present

	return duplicates

# Function to traverse the directory and delete duplicate files present in specified directory
def Delete_DuplicateFiles(duplicates):
	# duplicates.values = ((Demo.txt), (Hello.txt,A.py,Data.txt),(Demo.pdf,Bank.pdf),(Marvellous.txt),(A.txt,B.txt,C.txt,D.txt))
	# Output = ((Hello.txt,A.py,Data.txt),(Demo.pdf,Bank.pdf),(A.txt,B.txt,C.txt,D.txt))
	# len(Output) = 2

	Output = list(filter(lambda x:len(x) > 1,duplicates.values()))

	if len(Output) > 0:
		print("There are duplicate files in specified directory.!")
	else:
		print("There are no duplicate files in specified directory.!")
		return
	
	i = 0
	iCnt = 0
	for result in Output:
		iCnt = 0
		for path in result:
			iCnt += 1
			if iCnt >= 2:
				i += 1
				os.remove(path)

	print("Number of Duplicate files deleted : ",i)

def main():
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

	Result = Directory_Traversal(argv[1])

	Delete_DuplicateFiles(Result)

if __name__ == "__main__":
	main()