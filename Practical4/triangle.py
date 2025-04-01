#triangular numbers
#It can be calculated as the sum of the n numbers from 1 to n
#for n in range (1, 11)
#print each n and corresponding y

# initialize a variable to store the sum of the sequence
y = 0
# use a loop from 1 to 10
for n in range(1, 11):
# in each loop, count the number of triangles for the current number
    y += n
# print out the number of triangles
    print(n,y)