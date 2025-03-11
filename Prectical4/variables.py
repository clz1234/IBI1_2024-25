a = 15 
# The walk to the bus stop is 15 mins
b = 75
# The bus journey takes 75 mins 
c = a+b
# The total length of time for the bus-based commute
d = 90
# The drive takes 90 mins
e = 5
# The walk from the car park takes 5 mins
f = d+e
# The total length of time for the car-based commute
print(c , f)
if c > f:
    print("car-based commute faster than bus-based")
elif c < f:
    print("bus-based commute faster than car-based")
else:
    print("car-based commute is same as bus-based")
