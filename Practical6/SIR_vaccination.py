#use nice colour scheme
from matplotlib import cm
#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#as guide required, define the basic variables. And S for susceptible but healthy individuals, I for infected, R for recover, N for total,
#beta for infection probability upon contact, gamma for recovery probability.
N = 10000
beta = 0.3
gamma = 0.05
#create arrays for each of my variables
#add the array for vaccinated people
vaccination_rates = [i / 10 for i in range(11)]  # set the rate for vaccination[0.0, 0.1, ..., 1.0]
#becase vaccinated rate is change, so the susceptible people will change too
for rate in vaccination_rates:
    I = 1
    R = 0
    V = int(N*rate)
    S = N-V-I
    S_list = [S]
    I_list = [1]
    R_list = [0]
     #for t in range(1000):
     #calculate the probability of infection
     #randomly infected number S
     #randomly recovered number R
     #update number of S,I,R
     #add elements to arrays
    for t in range(1000):
        if N-V != 0:
            prob_infection = beta * (I / (N-V)) #the vaccinated people will never be infected
        else:
            prob_infection = 0
        if S > 0:
            num_infected = np.random.choice(range(2),int(S) , p=[1 - prob_infection, prob_infection])
            sum_new_infected = sum(num_infected)
            num_recovered = np.random.choice(range(2), I, p=[1 - gamma, gamma])
            sum_new_recovered = sum(num_recovered)
        else:
            num_infected = 0
        S = S - sum_new_infected 
        I = I + sum_new_infected - sum_new_recovered
        R = R + sum_new_recovered
        S_list.append(S)
        I_list.append(I)
        R_list.append(R)
#plot my results, plot the numbers of susceptible, infected, and recovered people as a function of time.
    #presents images with different probabilities
    plt.plot(I_list, label=f'{rate * 100}% vaccination')
#set x,ylabel and title
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.legend()
#save the plot
plt.savefig("<SIR model with different vaccination figure>", type="png", figsize=(6, 4))
plt.show()