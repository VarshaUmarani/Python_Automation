# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Author: Varsha Sidaray Umarani
# Date :  28-October-2023
# About:  Automation Script to Create log file of the running processes.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Importing required modules
import os
import psutil
from sys import *
from datetime import datetime

# Function to create log file containing information about running processes
def Create_LogFile(FolderName):
	if not os.path.exists(FolderName):
		os.mkdir(FolderName)
	else:
		print("Destination directory is already present.!")

	file_name = os.path.join(FolderName,"%s.log" %(datetime.now().strftime("%H-%M-%S")))
	
	file = open(file_name,"w")

	Data = []

	for process in psutil.process_iter():
		value = process.as_dict(attrs = ['pid','name','username'])
		Data.append(value)

	for element in Data:
		file.write("%s\n" %(element))

def main():
	print("--------------- Automation Script to Create log file of running processes ---------------")

	print("Script Title : ",argv[0])

	if (len(argv) != 2):
		print("Error : Insufficient Argument to the script.!")
		exit()

	if (argv[1] == "-u") or (argv[1] == "-U"):
		print("Script Usage : Run the script as parameter followed by file name.!")
		exit()

	if (argv[1] == "-h") or (argv[1] == "-H"):
		print("Script Help : Automation Script to Create log file of running processes")
		exit()

	process = Create_LogFile(argv[1])

if __name__ == "__main__":
	main()