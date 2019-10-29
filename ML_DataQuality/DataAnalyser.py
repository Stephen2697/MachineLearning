#!/usr/local/bin/python3
#Creator: Stephen Alger
#Machine Learening Introduction - Modelling Data, Deriving Modal Values, Measures of Central Tendency, Variation & Standard Deviation
#PyDocument: DataAnalyser.py
#Start-Date:  20-OCT-2019
#Version: 1.0
#Program Descriptor: Utilising Pandas and Jupyter to create Dataframes to read in 1994 US Census data to compile an Analytical Base Table (ABT) which displays a Categorical and Continuous Data Quality Report. Dealing with Data Quality Issues (DQIs) such as Cardinality Issues, Outliers and Missing Values.


#Import Modules...
import sys, os, pandas as pd, jupyter as jp, numpy as np, matplotlib.pyplot as plt

#-------Define Constants
FILEINPUT_TXT = "./Census-Data-Input/feature_names.txt"
FILEINPUT_CSV = "./Census-Data-Input/dataset.csv"
FILEOUTPUT_CONT = "./Output/ContinuousDataQualityReportABT.csv"
FILEOUTPUT_CAT = "./Output/CategoricalDataQualityReportABT.csv"
CONT_COL_LIST = ["FEATURENAME","Count","Missing %","Cardinality","Min Value","1st Quartile","Mean","Median","3rd Quartile","Max", "Standard Deviation"]
CAT_COL_LIST = ["FEATURENAME","Count","Missing %","Cardinality","Modal Value","Mode FreQ","Mode %","2nd Modal Value","2nd Mode FreQ","2nd Mode %"]
MODE_ERROR = "NoValidMode"

#-------Initialise Global Variable Lists and Dataframes

HEADING_LIST = []
CAT_LIST = []
CONT_LIST = []
INPUT_DATAFRAME = None
OUTPUT_DATAFRAME_CONT = pd.DataFrame(columns=CONT_COL_LIST)
OUTPUT_DATAFRAME_CAT = pd.DataFrame(columns=CAT_COL_LIST)


#-------Define Functions

#Creating Input dataframe from Headings in text file and Census Data
def buildInputDataFrame():
    global HEADING_LIST
    global INPUT_DATAFRAME
    
    feature_Names = open(FILEINPUT_TXT , "r")
    for feature in feature_Names:
        feature_Names = open(FILEINPUT_TXT , "r")
        HEADING_LIST.append(feature.rstrip('\n'))
        
#	Read CVS into the Input Dataframe, Format Missing Values to 'NaN'
    INPUT_DATAFRAME = pd.read_csv(FILEINPUT_CSV,names=HEADING_LIST, keep_default_na=False, na_values=[' ?','',' ','?'])
    


#Example Plot Function to Plot age & hours worked per week from Census
def samplePlotFunction():
	global INPUT_DATAFRAME

	titles = ['Hours Per Week Worked Distribution','Age Distribution']
	xLables = ['Hours Per Week','Age']
	yLabel = "Entries"
	colors = ["b", "r"]
	plots = [INPUT_DATAFRAME['hours-per-week'], INPUT_DATAFRAME['age']]
	plt.figure("Data Analytics - Stephen Alger")
	for i in range(2):
	    plt.subplot(1,2,i+1), plt.hist(plots[i], color = colors[i])
	    plt.title(titles[i])
	    plt.xlabel(xLables[i])
	    plt.ylabel(yLabel)
	plt.show()

#Separate (Numeric) Continuous Data from Categorical Columns
def separateDataTypes():
    global INPUT_DATAFRAME
    global CAT_LIST
    global CONT_LIST
    featureCols = INPUT_DATAFRAME.columns
    CONT_LIST = INPUT_DATAFRAME._get_numeric_data().columns
    CAT_LIST = list(set(HEADING_LIST) - set(CONT_LIST))

#Process Continuous Data Column
def processContinuous(col):
	global OUTPUT_DATAFRAME_CONT
	rowList = [col]
	
	#isolate specific column where string col refers to df[[col]]
	isolateDF = INPUT_DATAFRAME[[col]]
	
	#Count
	rowList.append(isolateDF.shape[0])
	
	#Calculate MissingPer
	nanSum = isolateDF.isna().sum()
	missingPer = 0
	if int(nanSum):
		missingPer = round(float(int(nanSum)/isolateDF.shape[0])*100,2)
	rowList.append(missingPer)
	
	#Cardinality - number of distinct answers - return series
	rowList.append(int(isolateDF.apply(pd.Series.nunique)))
	
	#Min
	rowList.append(int(isolateDF.min()))
	
	#1stQuart
	rowList.append(int(isolateDF.quantile(.25)))
	
	#Mean
	rowList.append(round(float(isolateDF.mean()), 2))
	
	#Median
	rowList.append(int(isolateDF.median()))
	
	#3rdQuart
	rowList.append(int(isolateDF.quantile(.75)))
	
	#Max
	rowList.append(int(isolateDF.max()))
	
	#StandDev
	rowList.append(round(float(isolateDF.std()),2))
	
	#Add row to dataframe
	tempOUTPUT_DATAFRAME_CONT = pd.DataFrame([rowList], columns=CONT_COL_LIST)
	OUTPUT_DATAFRAME_CONT = OUTPUT_DATAFRAME_CONT.append(tempOUTPUT_DATAFRAME_CONT, ignore_index=True)
	
#Process Categorical Data Column
def processCategorical(col):
	global OUTPUT_DATAFRAME_CAT
	rowList = [col]
	
	#isolate specific column where string col refers to df[[col]]
	isolateDF = INPUT_DATAFRAME[[col]]
	
	#Count
	rowList.append(isolateDF.shape[0])
	
	#Calculate MissingPer
	nanSum = isolateDF.isna().sum()
	missingPer = 0
	if int(nanSum):
		missingPer = round(float(int(nanSum)/isolateDF.shape[0])*100,2)
	rowList.append(missingPer)
	
	#Cardinality - number of distinct answers - return series
	rowList.append(int(isolateDF.apply(pd.Series.nunique)))
	
	#Mode
	#Get 2 Modal Values and number of times each occurs
	structModeNames = isolateDF[col].value_counts()[:2].index.tolist()
	structModeFreqs = isolateDF[col].value_counts()[:2].values
	
	#I.E. mode does not exist if our mode returned does not occur more than once
	if (structModeFreqs[0] == 1):
		#Mode
		rowList.append(MODE_ERROR)
		#modeFreq
		rowList.append(MODE_ERROR)
		#modePercent
		rowList.append(MODE_ERROR)
		#mode_2
		rowList.append(MODE_ERROR)
		#modeFreq_2
		rowList.append(MODE_ERROR)
		#modePercent_2
		rowList.append(MODE_ERROR)
	else:
		#mode
		rowList.append(structModeNames[0])
		#modeFreq
		rowList.append(structModeFreqs[0])
		#modePercent
		rowList.append( round( structModeFreqs[0]/isolateDF.shape[0],2))
		#mode_2
		rowList.append(structModeNames[1])
		#modeFreq_2
		rowList.append(structModeFreqs[1])
		#modePercent_2
		rowList.append(round(structModeFreqs[1]/isolateDF.shape[0],2))

	
	#Add row to dataframe
	tempOUTPUT_DATAFRAME = pd.DataFrame([rowList], columns=CAT_COL_LIST)
	OUTPUT_DATAFRAME_CAT = OUTPUT_DATAFRAME_CAT.append(tempOUTPUT_DATAFRAME, ignore_index=True)
	
def buildOutputDataFrame():
	index = 0
	for col in INPUT_DATAFRAME.columns:
#		Process Continuous Data
		if col in CONT_LIST:
			processContinuous(col)
#		Process Categorical Data
		elif col in CAT_LIST:
			if index != 0:
				processCategorical(col)
			#Exclude Id column - not to be processed
			index += 1
        
        
#-------Function Calls & General Logic
buildInputDataFrame()
separateDataTypes()
buildOutputDataFrame()
samplePlotFunction()

#-------Output to CSV
print("\n=====================================================\nYour Continuous Data ABT Report is Available in CSV @ " + FILEOUTPUT_CONT)
export_csv = OUTPUT_DATAFRAME_CONT.to_csv (FILEOUTPUT_CONT, index = None, header=True)
print("Your Categorical Data ABT Report is Available in CSV @ " + FILEOUTPUT_CAT +"\n=====================================================\n")
export_csv = OUTPUT_DATAFRAME_CAT.to_csv (FILEOUTPUT_CAT, index = None, header=True)
exit()

