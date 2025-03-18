#import matplotlib
import matplotlib.pyplot as plt
#creat a list to store uk and zhejiang neighbor provinxes population
uk_countries=[57.11,3.13,1.91,5.45]
zhejiang_neighbor_provinces=[65.77,41.88,45.28,61.27,85.15]
#sort the populations of each part of uk
uk_sorted=sorted(uk_countries)
uk_countries.sort()
#sort the populations in zhejiang neighbor provinces
zhejiang_neighbor_sorted=sorted(zhejiang_neighbor_provinces)
zhejiang_neighbor_provinces.sort()
#print the two list
print(uk_countries,zhejiang_neighbor_provinces)
#creat pie plots
#determine the size and label of uk contries
uk_population = uk_countries
uk_labels = ['Northern Ireland','Wales','Scotland','England']
#determine the size and label of zhejiang neighbor provinces
zj_neighbor_population = zhejiang_neighbor_provinces
zj_neighbor_labels = ['Fujian','Jiangxi','Anhui','Zhejiang','Jiangsu']
#creat a figure contains two subplots
fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(15,8))
#define the parameters highlighted in the pie plot of uk
explode1=(0.1,0,0,0)
#set prominent parameters,labels and percentage formats of uk pie plot
ax1.pie(uk_population, explode=explode1,labels=uk_labels, autopct='%1.1f%%')
#name ax1
ax1.set_title('Population Distribution in UK Countries')
#efine the parameters highlighted in the pie plot of zhejiang neighbor provinces
explode2=(0,0,0,0,0.1)
#set prominent parameters,labels and percentage formats of zhejiang neighbor provinces pie plot
ax2.pie(zj_neighbor_population, explode=explode2,labels=zj_neighbor_labels, autopct='%1.1f%%')
#name ax2
ax2.set_title('Population Distribution in Zhejiang - Neighbouring Provinces')

plt.show()