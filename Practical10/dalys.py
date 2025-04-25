
#import necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#find the dictionary where the target file is in
os.chdir("D:\IBI1\IBI1_2024-25\Practical10")

#read the data from target file and store them
dalys_data=pd.read_csv("dalys-rate-from-all-causes.csv")

'''
print(dalys_data.head(5))
print(dalys_data.infro())

sum=dalys_data.describe()

max_DALYs=sum.loc['max','DALYs']
min_DALYs=sum.loc['min','DALYs']

earliest_year=dalys_data['Year'].min()
recent_year=dalys_data['Year'].max()

print(f"maximum DALYs:{max_DALYs}")
print(f"minimum DALYs:{min_DALYs}")
print(f"first year when DALYs were recorded:{earliest_year}")
print(f"most recent year:{recent_year}")
'''

#show the 3rd column for the first 10 rows (inclusive)
print(dalys_data.iloc[0:10,3])
#1999 was the 10th year with DALYs data recorded in Afghanistan
#print the 10th year with DALYs data recorded in Afghanistan
print(dalys_data.iloc[9,2])

#pick all the data of years
years=dalys_data.loc[0:,'Year']
#select all 1990 data
is_1990=years==1990
#select 1990 DALYs of all entity
dalys_1990=dalys_data.loc[is_1990,['Entity','DALYs']]
#show the 1990 DALYs and the corresponding entities
print(dalys_1990)

#the mean DALYs in UK was greater than France
#select the DALYs of UK and France
uk=dalys_data.loc[dalys_data.Entity=="United Kingdom",["DALYs","Year"]]
france=dalys_data.loc[dalys_data.Entity=="France",["DALYs","Year"]]

#calculate the DALYs mean value of the two countrie
uk_dalys_mean=uk["DALYs"].mean()
france_dalys_mean=france["DALYs"].mean()

#compare the DALYs of UK and France
if uk_dalys_mean>france_dalys_mean:
    print("the mean DALYs in UK was greater than France")
else:
    print("the mean DALYs in France was greater than UK")
    
#show the two mean value
print(uk_dalys_mean)
print(france_dalys_mean)

#select the years of
uk_year=uk["Year"]

#determine the size of figure
plt.figure(figsize=(12,8))

#draw the plot
plt.plot(uk.Year,uk.DALYs,'b+') #different commands like "b+", "r+" and "bo" refer to different shape of the dot.
plt.xticks(uk.Year,rotation=-90) #the different numbers refer to the angle formed by the string and the x-axis that represents the year

#determine the title, xlabel and ylabel of the plot
plt.title('DALYs over time in the UK')
plt.xlabel('Year')
plt.ylabel('DALYs')

#show the plot
plt.show()

#from here to adress the additional question

#draw a line chart of the number of annual DALYs of these two countries
#select the DALYs and years data of China and United States
china=dalys_data.loc[dalys_data.Entity=="China",["DALYs","Year"]]
usa=dalys_data.loc[dalys_data.Entity=="United States",["DALYs","Year"]]

#determine the size of the plot
plt.figure(figsize=(12,8))

#draw the plot
plt.plot(china.Year,china.DALYs,label='China')
plt.plot(usa.Year,usa.DALYs,label='United States')

#determine the title, xlabel and ylabel of the plot
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('Change of DALYs in China and United States over time')

#add figure legend
plt.legend()

#show the plot
plt.show()

#draw a line chart to mirror the person correlation coefficient over the time to judge whether the changes of the two countries' DALYs have similarity over time
#determine the size of window
window_size=5

#creat a list to store the person correlation coefficients
correlation=[]

#travel through all years
for i in range(len(china.DALYs)-window_size+1):

    #store the DALYs corresponding to each sliding windows
    window_china=china.DALYs[i:i+window_size]
    window_usa=usa.DALYs[i:i+window_size]

    #calculate person correlation coefficient
    corr=np.corrcoef(window_china,window_usa)[0,1]
    #add calculated person correlation coefficients to the list
    correlation.append(corr)

#generate the corresponding year range (corresponding to the starting year of each sliding window)
window_years=china['Year'].iloc[:len(correlation)].values

#determine the size of plot
plt.figure(figsize=(12,8))

#draw the plot
plt.plot(window_years,correlation)

#determine the title, xlabel and ylabel of the plot
plt.xlabel('Year')
plt.ylabel('Person correlation coefficient')
plt.title('sliding window correlation of DALYs between China and USA')

#show the plot
plt.show()
