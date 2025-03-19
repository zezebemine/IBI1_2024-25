#import numpy and matplotlib.
import numpy as np
import matplotlib.pyplot as plt

#creat language dictionary to store languages and percentage
language_dictionary={"JavaScripy":62.3,"HTML":52.9,"Python":51,"SQL":51,"TypeScript":38.5}
#print language dictionary
print(language_dictionary)

#assign values to languages and percentage
languages=list(language_dictionary.keys())
percentage=list(language_dictionary.values())

#determine the number of vaariables
N=5

#draw bar plot
plt.bar(languages,percentage)
#determine the coordinate axis
plt.ylabel('percentage')
plt.xlabel('languages')
#determine the length of Y axis
plt.yticks(np.arange(0,101,10))
#name the bar plot
plt.title('programming language popularity')

#show the bar plot
plt.show()

#draw one language
drawed_language='Python'
#print the drawed language and percentage 
print(f"The percentage of developers who use {drawed_language} is {language_dictionary[drawed_language]}")