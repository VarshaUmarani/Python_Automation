# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Author: Varsha Sidaray Umarani
# Date :  29-October-2023
# About:  Automation Script to Create log file of the running processes periodically.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Importing required modules
import os
import time
import psutil
import schedule
from sys import *
from datetime import datetime

# Function to create log file containing information about running processes
def Create_LogFile(FolderName="Python"):
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

	if (len(argv) < 2):
		print("Error : Insufficient Argument to the script.!")
		exit()

	if (argv[1] == "-u") or (argv[1] == "-U"):
		print("Script Usage : Parameters - Application_Name.py Schedule_Time Directory_Name")
		exit()

	if (argv[1] == "-h") or (argv[1] == "-H"):
		print("Script Help : Automation Script to Create log file of running processes")
		exit()

	schedule.every(int(argv[1])).minutes.do(Create_LogFile)

	while True:
		schedule.run_pending()
		time.sleep(1)

if __name__ == "__main__":
	main()
