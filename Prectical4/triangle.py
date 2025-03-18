#     triangular numbers
#         How to calculated
#            It can be calculated as the sum of the n numbers from 1 to n
#            for n in range (1, 11)

# Compute the first ten values of the triangular series
# Step 1: Initialize a variable to store the sum of the sequence
# Step 2: Use a loop from 1 to 10
# Step 3: In each loop, count the number of triangles for the current number
# Step 4: Print out the number of triangles

# Step 1: Initialize a variable to store the sum of the sequence
y = 0
# Step 2: Use a loop from 1 to 10
for n in range(1, 11):
# Step 3: In each loop, count the number of triangles for the current number
    y += n
# Step 4: Print out the number of triangles
    print(n,y)