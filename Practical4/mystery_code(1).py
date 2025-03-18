# What does this piece of code do?
# Answer:Draw one number from each of the two samples of between 1 and 6, stop until the two samples draw the same number, and print the number of draws

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

# Define a varible called progress
progress=0

# Creat a while loop
# If the progress is largeer than or equal to 0
# The value of progress will add 1 
while progress>=0:
	progress+=1
	# Creat a randint first_n, range between 1 and 6
	first_n = randint(1,6)
	# Creat a randint second_n, range between 1 and 6
	second_n = randint(1,6)
	# Judge whether first_n is equal to second_n
	if first_n == second_n:
		#if they are equal, print progress
		print(progress)
		#jump out of the loop
		break

