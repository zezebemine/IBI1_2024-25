# Initialise an empty list to store the sequence of triangle numbers
# It will be used to calculate triangular numbers.
a = 0
# Use a for loop. The variable 'i' will take integer valies from 1 to 10 in sequence.
# This is for calculating the first ten triangular numbers.
for i in range(1,11):
    # Add the value of i to a
    # In each iteration, it accumulates va;ues from 1 to the current value of i
    # thus obtaining the 'i'th triangular number.
    a+=i
    # Print the triangular number obtained in each iteration.
    print(a)