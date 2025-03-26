#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#as guide required, define the basic variables. And S for susceptible but healthy individuals, I for infected, R for recover, N for total,
#beta for infection probability upon contact, gamma for recovery probability.
S = 9999
I = 1
R = 0
N = 10000
beta = 0.3
gamma = 0.05
#create arrays for each of my variables
S_list = [9999]
I_list = [1]
R_list = [0]
#for t in range(1000):
     #calculate the probability of infection
     #randomly infected number S
     #randomly recovered number R
     #update number of S,I,R
     #add elements to arrays
for t in range(1000):
    prob_infection = beta * (I / N) #search for how to use arrays' last element, and get [-1]
    prob_infection = min(1, max(0, prob_infection))
    num_infected = np.random.choice(range(2), S, p=[1 - prob_infection, prob_infection])
    sum_new_infected = sum(num_infected)
    num_recovered = np.random.choice(range(2), I, p=[1 - gamma, gamma])
    sum_new_recovered = sum(num_recovered)
    S = S - sum_new_infected 
    I = I + sum_new_infected - sum_new_recovered
    R = R + sum_new_recovered
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)
#plot my results, plot the numbers of susceptible, infected, and recovered people as a function of time.
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_list, label='susceptible')
plt.plot(I_list, label='infected')
plt.plot(R_list, label='recovered')
#set x,ylabel and title
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()
#save the plot
plt.savefig("SIR_figure.png")
plt.show()