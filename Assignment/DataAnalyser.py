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
	#isolate specific column where string col refers to df[[col]]
	isolateDF = INPUT_DATAFRAME[[col]]
	#Count
	count = isolateDF.shape[0]
	#Calculate MissingPer
	nanSum = isolateDF.isna().sum()
	missingPer = 0
	if int(nanSum):
		missingPer = round(float(int(nanSum)/count)*100,2)
	#Cardinality - number of distinct answers - return series
	cardinality = int(isolateDF.apply(pd.Series.nunique))
	#Min
	min = round(float(isolateDF.min()),2)
	#1stQuart
	q1 = round(float(isolateDF.quantile(.25)),2)
	#Mean
	mean = round(float(isolateDF.mean()), 2)
	#Median
	median = round(float(isolateDF.median()),2)
	#3rdQuart
	q3 = round(float(isolateDF.quantile(.75)),2)
	#Max
	max = round(float(isolateDF.max()),2)
	#StandDev
	stdDev = round(float(isolateDF.std()),2)
	
	print((col + ": Count [" + str(count) + "], Missing Per: [" + str(missingPer) + "%],"+ " Card: [" + str(cardinality) + "], Min: [" + str(min)+ "], 1st  Quartile: [" + str(q1)+ "], Mean: [" + str(mean) + "], Median: [" + str(median) + "], 3rd Quartile: [" + str(q3) + "], Max: [" + str(max) + "], Stadard Deviation: [" + str(stdDev) +"]").upper())
	
	print("\n\n###############")
	
def processCategorical(col):
#	print("CAT ["+ col + "]")
	#Count
	count = INPUT_DATAFRAME.shape[0]
	
	#MissingPer
	nanSum = INPUT_DATAFRAME[[col]].isna().sum()
	missingPer = 0
	if int(nanSum):
		missingPer = round(float(int(nanSum)/count)*100,2)
	
	#Cardinality - number of distinct answers
#	print(INPUT_DATAFRAME.apply(pd.Series.nunique))
	
	
#	test output
#	print((col + ": Count [" + str(count) + "], Missing Per: [" + str(missingPer) + "%]\n").upper())
	
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
