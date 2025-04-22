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
a=dalys_data.iloc[0:10,2]
print(a)# 1999 was the 10th year with DALYs datarecorded in Afghanistan

#obtain the Boolean type sequence with the Year 1990
condition = dalys_data['Year'] == 1990
#Filter out Entity and DALYs
dalys_1990 = dalys_data.loc[condition, [True,False,False,True]]
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
#adjust the X-axis to make the plot nicer
plt.xticks(uk.Year,rotation=-90)
plt.show()

#extract the data of China and the United Kingdom
china = dalys_data.loc[dalys_data.Entity == "China", ["Year", "DALYs"]]
uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["Year", "DALYs"]]
#draw a line graph showing the changes of DALYs in China over time
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