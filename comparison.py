import pandas as pd
import numpy as np
import openpyxl

# creates dataframes for each of the documents
# dataframes are a table or a two-dimensional array-like structure in which each column contains values of one variable and each row contains one set of values
# change the workbook name values inside of df1 and df2 to compare whatever workbooks you'd like
df1=pd.read_excel('HG_MSA_Copy.xlsx')
df2=pd.read_excel('HGMSASeptember.xlsx')

#ensures the shape and type of dataframes are equal
df1.equals(df2)

#compares dataframes - will print out true or false
comparison_values = df1.values == df2.values
print (comparison_values)

# tuple of rows and columns
# get index of all cells where the values differ
rows,cols=np.where(comparison_values==False)

#iterate over the cells and update df1 to display changed value in df2
for item in zip(rows,cols):
    df1.iloc[item[0], item[1]] = '{} --> {}'.format(df1.iloc[item[0], item[1]],df2.iloc[item[0], item[1]])

#export the dataframe into an excel file called Excel_diff
df1.to_excel('./Excel_differences.xlsx',index=False,header=True)
