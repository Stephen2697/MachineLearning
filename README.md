# DataAnalyser .py [v1.0]
* * *
###### Creator: Stephen Alger
###### Machine Learening Introduction - Modelling Data, Deriving Modal Values, Measures of Central Tendency, Variation & Standard Deviation.
###### Last Update: 29 October 2019
<br/><br/>
### Program Descriptor: 
Utilising Pandas and Jupyter to create Dataframes to read in 1994 US Census data to compile an Analytical Base Table (ABT) which displays a Categorical and Continuous Data Quality Report. Dealing with Data Quality Issues (DQIs) such as Cardinality Issues, Outliers and Missing Values.

### How to Run DataAnalyser Script:

```sh
--Run This Script as Follows
$ cd /Github/ML/ML_DataQuality
$ chmod 755 DataAnalyser.py     #-- if needed 
$ python3 DataAnalyser.py
```

### Data Set In Use: 1994 US Census Data - see files below:
https://archive.ics.uci.edu/ml/datasets/Adult
http://cseweb.ucsd.edu/classes/sp15/cse190-c/reports/sp15/048.pdf

### Design Notes:
- Read in US Census Data from .csv into panda Dataframe
- Get the Column Headings from .txt file
- Separate Continuous and Categorical Columns
- Process Both types of Data in their respective ways:
*Continuous -[1st Quartile ,Mean ,Median ,3rd Quartile ,Max ,Standard Deviation]
*Categorical -[Modal Value, Mode FreQ, Mode %, 2nd Modal Value, 2nd Mode FreQ, 2nd Mode %]
- Build respective output dataframes with input data columns as features
- Output both Categorical and Continuous Data to separate CSV files in Analytical Base Table Format

### Compatibility: 
* Tested on Python 3.7.2 - Mac OS Catalina (Not Compatible with Python 2.7)
* Also Tested in Jupyter Notebook

### Output Files:
- ContinuousDataQualityReportABT.csv
- CategoricalDataQualityReportABT.csv


### Known Issues/ Points of Improvement (Non-Exhaustive) :
- Yet to Be Added...



