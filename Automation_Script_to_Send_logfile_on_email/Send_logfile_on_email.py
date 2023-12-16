# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Author: Varsha Sidaray Umarani
# Date :  30-October-2023
# About:  Automation Script to Create log file of the running processes and send mail attaching log file.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Importing required modules
import os
import time
import psutil
import schedule
from sys import *
from datetime import datetime

# User - defined module
from email_module import *

SEND_FROM = "varshaumarani2002@gmail.com"
SEND_TO = ["varuumarani6688@gmail.com"]
SUBJECT = "Sending Log File of Running processes"
MESSAGE = "Hey, I hope you are doing good today.!!\nI am attaching the log of running processes\nPlease go through it."

# Function to create log file containing information of running processes
def Create_LogFile(FolderName="Python"):
	if not os.path.exists(FolderName):
		os.mkdir(FolderName)

	file_name = os.path.join(FolderName,"%s.log" %(datetime.now().strftime("%H-%M-%S")))

	file = open(file_name,'w')

	Data = []

	for process in psutil.process_iter():
		Value = process.as_dict(attrs=['pid','name','username'])
		Data.append(Value)

	for element in Data:
		file.write("%s\n" %element)

	#send_mail(SEND_FROM, SEND_TO, SUBJECT, MESSAGE, files=[],server="localhost", port=587, username='', password='',use_tls=True):
	send_mail(SEND_FROM,SEND_TO,SUBJECT,MESSAGE,[file_name])

	file.close()

def main():
	print("------------------------------------- Automation Script to Create log file of running processes and Send mail attaching log file --------------------------------------")

	print("Script Title : ",argv[0])

	if (len(argv) != 2):
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
