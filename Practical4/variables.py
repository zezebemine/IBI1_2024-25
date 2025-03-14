
# The time walk to bus stop (min)
a = 15
# The time for the bus journey (min), 1 hour and 15 minutes is turned to 75minutes
b = 75
# The total time for the bus
c = a+b
# The time for driving (min), 1 hour and 30 minutes is turned to 90 minutes
d = 90
# The time to walk from the car park (min)
e = 5
# The total time for car
f = d+e
# Compare the total times of the two methods
if c < f:
    print("bus is faster")
    # Comment: the total time c for the bus is 90 min, and the total time f for cai is 95 min. So the bus is faster than car.
else:
    print("car is faster")

X=True
Y=False
W=X and Y
print (W)
# True - table comment:
# X     Y     W
# Ture  Ture  Ture
# Ture  False False
# False True  False
# False False False