# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Author: Varsha Sidaray Umarani
# Date :  03-November-2023
# About:  Automation Script to traverse files, folders and subfolders present in particular
#		  directory, delete all the duplicate files present in the particular folder,
#		  add path of deleted file into the log file and send mail with attached log file
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Importing required modules
import os
import time
import hashlib
import schedule
from sys import *
from datetime import datetime

# User - defined module
from email_module import *

SEND_FROM = "varshaumarani2002@gmail.com"
SEND_TO = ["varuumarani6688@gmail.com"]
SUBJECT = "Sending Log File of Deleted Files"
MESSAGE = "Hey, I hope you are doing good today.!!\nI am attaching the log of deleted files\nPlease go through it."
USERNAME = 'varshaumarani2002@gmail.com'
PASSWORD = 'wazg xwtc ffsh bfbc'

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
def DirectoryTraversal(path):
	if not os.path.exists(path):
		print("Error : The path you entered doesn't exists.!")
		exit()
		
	duplicate = {}		# Dictionary to hold checksum and file name

	for Folder, Subfolder, Filename in os.walk(path):
		for file in Filename:
			actualpath = os.path.join(Folder,file)
			hash = Calculate_CheckSum(actualpath)
			
			if hash in duplicate:					# If checksum is already present
				duplicate[hash].append(actualpath)
			else:
				duplicate[hash] = [actualpath]		# If checksum is not present

	return duplicate

# Function to create log file containing name of deleted duplicate files
def Create_LogFile(path,FolderName="Python"):
	if not os.path.exists(FolderName):
		os.mkdir(FolderName)

	file_name = os.path.join(FolderName,"%s.log" %(datetime.now().strftime("%H-%M-%S")))

	file = open(file_name,'w')

	files = DirectoryTraversal(path)
	duplicate_files = FindDuplicate(files)
	deleted_files = DeleteDuplicate(duplicate_files)

	if len(deleted_files) != 0:
		file.write("Name of deleted files are : \n")
		for fileName in deleted_files:
			file.write("%s\n" %(fileName))

	file.write("Overall Statistics : \n")
	file.write("Total Number of Files Scanned is : %s\n" %len(files))
	file.write("Total Number of Duplicate Files found is : %s\n" %len(duplicate_files))

	if len(deleted_files) == 0:
		file.write("There are no duplicate files in the specified directory..!!\n")
	else:
		file.write("Total Number of Files deleted is : %s\n" %len(deleted_files))

	#send_mail(SEND_FROM, SEND_TO, SUBJECT, MESSAGE, files=[],server="localhost", port=587, USERNAME='', PASSWORD='',use_tls=True):
	if Check_Internet_Connection():
		send_mail(SEND_FROM,SEND_TO,SUBJECT,MESSAGE,[file_name])

	file.close()

# Function to traverse the directory and find duplicate files present in specified directory
def FindDuplicate(duplicate):
	output = list(filter(lambda x : len(x) > 1,duplicate.values()))

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

	return Arr

# Function to traverse the directory and delete duplicate files present in specified directory
def DeleteDuplicate(Arr):
	deleted_files = []
	for i in range(len(Arr)):
		os.remove(Arr[i])
		deleted_files.append(Arr[i])

	return deleted_files

def main():
	Arr = {}

	print("-------------------------------  Automation Script for Directory Traversal and Duplicate Files Cleaner with E-mail Facility  ------------------------------")

	if len(argv) < 2:
		print("Error : Insufficient Argument to the script.!")
		exit()

	if (argv[1] == "-h") or (argv[1] == "-H"):
		print("Script Help : This Script works as Directory Traversal and Delete Duplicate Files.!")
		exit()

	if (argv[1] == "-u") or (argv[1] == "-U"):
		print("Script Usage : Parameters - Application_Name.py Schedule time Absolute Path of the Destination Directory")
		exit()

	schedule.every(int(argv[1])).hour.do(Create_LogFile,argv[2])

	while True:
		schedule.run_pending()
		time.sleep(1)

if __name__ == "__main__":
	main()
