#!/usr/local/bin/python3
#Creator: Stephen Alger C16377163
#Assignment: Machine Learening
#Document: Assignment1.py
#Start-Date:  20-OCT-2019
#Dataset Sifter

#Import Modules...
import sys, os

#Define Constants
FILEINPUT_TXT = "./Data/feature_names.txt"
FILEINPUT_CSV = "./Data/dataset.csv"
FILEOUTPUT_CONT = "./Output/C16377163CONT.csv"
FILEOUTPUT_CAT = "./Output/C16377163CAT.csv"
HEADING_LIST = []

#read in
def analyseInput():
	global HEADING_LIST
	index = 0
	feature_names = open(FILEINPUT_TXT , "r")
	
	for x in feature_names:
		feature_names = open(FILEINPUT_TXT , "r")
		HEADING_LIST.append(x.rstrip('\n'))

#deal with CSV headings?
def initialiseOutput():
	#Happens once
	csvFile1 = open(FILEOUTPUT_CONT, "w")
	csvFile2 = open(FILEOUTPUT_CAT, "w")
	
	for item in HEADING_LIST:
		csvFile1.write("%s," % item)
		csvFile2.write("%s," % item)

	csvFile1.close()
	csvFile2.close()
	
#logic to treat data line
def siftLogic():
	print("hi")

#act on logic and append to appropriate csv
def splitOutput():
	
	f = open("myfile.txt", "a")
	f.write("Woops! I have deleted the content!")
	f.close()

analyseInput()
initialiseOutput()
