'''
Import the necessary libraries
Use the os.chdir() function to switch the working directory to the path where the data file is located and read the data set
Display the "Year" column (the third column) of the first 10 rows
Filter the DALYs data of 1990 to create a Boolean sequence data_1990: Determine whether the "Year" column is equal to 1990
Calculate the average DALYs of the United Kingdom and France, print the mean values of the two countries, compare their sizes, and output the results
Draw a line graph of the DALYs in the UK over time
Extract the columns of "Year" and "DALYs" for comparison and plotting
'''
#import the necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#modify the working directory to the path where the data file is located
os.chdir("/Users/cuilizi/Desktop/Lecture/IBI/IBI1/IBI1_2024-25/IBI1_2024-25/Practical10")
#read the data set
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

#display the third column (year) of the first 10 rows
frist_ten_year=dalys_data.iloc[0:10,2]
print(frist_ten_year)# 1999 was the 10th year with DALYs datarecorded in Afghanistan

#obtain the Boolean type sequence with the Year 1990.
data_1990 = dalys_data['Year'] == 1990
#Filter out Entity and DALYs
dalys_1990 = dalys_data.loc[data_1990, [True,False,False,True]]
print(dalys_1990)

#extract the data of the UK and France
uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs"]]
france = dalys_data.loc[dalys_data.Entity=="France", ["DALYs"]]
#value the mean
uk_mean = uk.mean()
france_mean = france.mean()
print("UK's mean is ", uk_mean.values[0])
print("France's mean is ", france_mean.values[0])
#make a comparison
if uk_mean.values[0] > france_mean.values[0]:
    print("the mean DALYs in the UK was greater than France")
elif uk_mean.values[0] < france_mean.values[0]:
    print("the mean DALYs in the UK was smaller than France")
# the mean DALYs in the UK was greater than France

#extract the data of the UK
uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]]
#draw a line graph showing the changes of DALYs in UK over time
plt.plot(uk.Year, uk.DALYs, 'b+')
plt.title('DALYs in the UK Over Time')
#adjust the X-axis to make the plot nicer
plt.xticks(uk.Year,rotation=-45)
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.show()

#extract the data of China and the United Kingdom
china = dalys_data.loc[dalys_data.Entity == "China", ["Year", "DALYs"]]
uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["Year", "DALYs"]]
plt.plot(china.Year, china.DALYs, label='China', marker='o')
#draw a line graph showing the changes of DALYs in UK over time
plt.plot(uk.Year, uk.DALYs, label='United Kingdom', marker='s')
#set the figure title and label
plt.title('DALYs in China and the UK Over Time')
plt.xlabel('Year')
plt.ylabel('DALYs')
#add the legend and show the whole figure
plt.legend()
plt.show()
#the relationship between the DALYs in China and the UK become more similar
