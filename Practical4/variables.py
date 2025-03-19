a = 15 
# the walk to the bus stop is 15 mins
b = 75
# the bus journey takes 75 mins 
c = a+b
# the total length of time for the bus-based commute
d = 90
# the drive takes 90 mins
e = 5
# the walk from the car park takes 5 mins
f = d+e
# the total length of time for the car-based commute
print(c , f)
if c > f:
    print("Bus-based commute is longer, car-based commute faster than bus-based")
elif c < f:
    print("Car-based commute is longer, bus-based commute faster than car-based")
else:
    print("car-based commute is same as bus-based")
    # car-based commute is longer,bus-based commute is quicker

X = True
Y = False
W = X and Y
print(W)
# the result is False
X = True
Y = True
W = X and Y
print(W)
# the result is True
X = False
Y = False
W = X and Y
print(W)
# the result is False
X = False
Y = True
W = X and Y
print(W
# the result is False

# the truth table for W
# | X | Y | W（X and Y） |
# |----|----|----|
# | True | True | True |
# | True | False | False |
# | False | True | False |
# | False | False | False |