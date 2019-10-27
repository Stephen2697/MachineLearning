#!/usr/local/bin/python3
#Creator: Stephen Alger C16377163
#Assignment: Machine Learening
#Document: Assignment1.py
#Start-Date:  20-OCT-2019
#Dataset Sifter

#Import Modules...
import sys, os
import pandas as pd
import jupyter as jp

#-------Define Constants
FILEINPUT_TXT = "./Data/feature_names.txt"
FILEINPUT_CSV = "./Data/dataset.csv"
FILEOUTPUT_CONT = "./Output/C16377163CONT.csv"
FILEOUTPUT_CAT = "./Output/C16377163CAT.csv"
HEADING_LIST = []
CAT_LIST = []
CONT_LIST = []
INPUT_DATAFRAME = None
OUTPUT_DATAFRAME = None

#print(INPUT_DATAFRAME.iloc[[23]])
#for index, col in INPUT_DATAFRAME.iterrows():
#    print(index)

#-------Define Functions
def buildInputDataFrame():
    global HEADING_LIST
    global INPUT_DATAFRAME
    feature_Names = open(FILEINPUT_TXT , "r")
    for feature in feature_Names:
        feature_Names = open(FILEINPUT_TXT , "r")
        HEADING_LIST.append(feature.rstrip('\n'))
        
    INPUT_DATAFRAME = pd.read_csv(FILEINPUT_CSV,names=HEADING_LIST, keep_default_na=False, na_values=[' ?','',' ','?'])
    
def separateDataTypes():
    global INPUT_DATAFRAME
    global CAT_LIST
    global CONT_LIST
    featureCols = INPUT_DATAFRAME.columns
    CONT_LIST = INPUT_DATAFRAME._get_numeric_data().columns
    CAT_LIST = list(set(HEADING_LIST) - set(CONT_LIST))

def processContinuous(col):
#	print("CONT ["+ col + "]")
#	DataFrame.append()

	#Count
	count = INPUT_DATAFRAME.shape[0]
	
	#MissingPer
	nanSum = INPUT_DATAFRAME[[col]].isna().sum()
	missingPer = 0
	if int(nanSum):
		missingPer = round(float(int(nanSum)/count)*100,2)
		
		
	#Cardinality
	#Min
	#1stQuart
	#Mean
	#Median
	#3rdQuart
	#Max
	#StandDev
	print((col + ": Count [" + str(count) + "], Missing Per: [" + str(missingPer) + "%]\n").upper())
	
def processCategorical(col):
#	print("CAT ["+ col + "]")
	#Count
	count = INPUT_DATAFRAME.shape[0]
	
	#MissingPer
	nanSum = INPUT_DATAFRAME[[col]].isna().sum()
	missingPer = 0
	if int(nanSum):
		missingPer = round(float(int(nanSum)/count)*100,2)
		
	print((col + ": Count [" + str(count) + "], Missing Per: [" + str(missingPer) + "%]\n").upper())
	
def buildOutputDataFrame():
    for col in INPUT_DATAFRAME.columns:
#		Process Continuous Data
        if col in CONT_LIST:
            processContinuous(col)
		
#		Process Categorical Data
        elif col in CAT_LIST:
            
            processCategorical(col)
        
        
#-------Function Calls & General Logic
buildInputDataFrame()
separateDataTypes()
buildOutputDataFrame()
exit()
