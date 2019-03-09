#!/usr/bin/env python


from argparse import ArgumentParser

parser = ArgumentParser(description='A CSV reader + stats makes')
parser.add_argument('csvfile', help ='path to the input of csv file')

parsed_args = parser.parse_args()
print(parsed_args)
print(parsed_args.csvfile)

my_csv_file = parsed_args.csvfile

import os

#if os.path.isfile(my_csv_file):
#	print("The file is Valid")
#else:
#	print("Opps! Invalid file. Enter a valid file")

#if not os.path.isfile(my_csv_file):
#	raise ValueError("not a valid file")
 
assert os.path.isfile(my_csv_file), "Please Enter a valid file"

print("The file exists")

#Solution 1(b) - Import the file

import pandas as pd

#data = pd.read_csv(my_csv_file, sep='\s+|,',skiprows=[0],header=None, engine='python')
data = pd.read_csv(my_csv_file, sep='\s+|,', engine='python') #for data with default header
print("Data Preview","\n",data.head())
print("\n",data.shape)

# This session  Accesses Rows and Columns

print("\n","Rows 3 and 4","\n",data.iloc[3:5,:]) #Access Row
print("\n", "Column 3" "\n", data.iloc[:,3]) #Access Column


# This session computes Summary Statistics (Mean and Standard Deviation)

import numpy as np

print("\n","Mean of Features","\n",np.mean(data,axis=0))
print("\n")
print("Standard Deviation of Features", "\n", np.std(data,axis=0))

# This session is for plotting

import matplotlib.pyplot as plt
import seaborn as sns

# This session plots Histogram of each feature (column)

#for i, column in enumerate(data.columns):
#	plt.figure(i)
#	sns.distplot(data[column])
#	plt.savefig('histogram_''{0}.pdf'.format(column))
#plt.show()
#plt.close()

# This session plots Scatterplot for any 2 pairs of features (columns)

#for i, column1 in enumerate(data.columns):
#	for j, column2 in enumerate (data.columns[i+1:]):
		#print (column1, column2)
#		data1 = data[column1]
#		data2 = data[column2]
#		plt.figure()
#		sns.scatterplot(data1, data2)
#		plt.savefig("Scatterplot_{}_{}.pdf".format(column1, column2))
#plt.show()
#plt.close()

# CLASS7 HOMEWORK

import itertools
#data_focus =  data.loc[:, ['AGE', 'BMI', 'BP', 'Y']]  #To create new dataframe of target columns from df
for pair in itertools.combinations((data.columns), 4): #Computes Columns Combination 4
	data1 = data[list(pair)]
#	print (data1)
	sns.pairplot(data1, kind='reg')
	plt.savefig("Pairplot_{}.pdf".format(pair))
plt.show()
plt.close()






