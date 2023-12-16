# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Author: Varsha Sidaray Umarani
# Date :  01-November-2023
# About:  Automation Script to traverse the given directory and find the search 
#		  results of specific file in that directory.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Importing required modules
import os
from sys import *

# Function to explore (search) the file in specified directory
def File_Explorer(path,Filename):
	iCnt = 0
	File_search = []

	if not os.path.exists(path):
		print("Error : The path you entered doesn't exists.!")
		exit()

	for Folder,Subfolder,filename in os.walk(path):
		#print("Directory name is : ",folder)
		#for sub in subfolder:
			#print("Subfolder of",folder,"is : ",sub)
		for file in filename:
			iCnt += 1
			if file == Filename:
				actualpath = os.path.join(Folder,file)
				File_search.append(actualpath)

	print("Number of Total Files Scanned is :",iCnt)
	return File_search

def main():
	print("----------------------- Script for Directory Traversal and File Explorer --------------------")

	if len(argv) < 2:
		print("Error : Invalid Arguments for the script")
		exit()

	if argv[1] == "-h" or argv[1] == "-H":
		print("Script Help : This Script works as File Explorer and Directory Traveller")
		exit()

	if argv[1] == "-u" or argv[1] == "-U":
		print("Usage : Script_Name, Folder_Name  & File_Name to Search in Directory")
		exit()
	
	search_result = File_Explorer(argv[1],argv[2])
	print("The Search Results of", argv[2]," : ")

	for file_name in search_result:
		print(file_name)

if __name__ == "__main__":
	main()