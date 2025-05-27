'''
import necessary libraries
define basic information, set nesscary array
For different vaccination rates, simulate the situation of the number of infections in 1,000 cycles
set the figure
'''
#use nice colour scheme
from matplotlib import cm
#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#define the basic variables. N for total, beta for infection probability upon contact, gamma for recovery probability.
N = 10000
beta = 0.3
gamma = 0.05
#create arrays for each of my variables
#add the array for vaccinated people
vaccination_rates = [i / 10 for i in range(11)]  # set the rate for vaccination[0.0, 0.1, ..., 1.0]
#create plot and set size
plt.figure(figsize=(6, 4))
num_rates = len(vaccination_rates)
colors = cm.viridis(np.linspace(0, 1, len(vaccination_rates)))
#traverse different probabilities, i let "I" is "infected", "R" is "recovered", "V" is "vaccinated", "S" is "susceptible"
for i, rate in enumerate(vaccination_rates):
    I = 1
    R = 0
    V = int(N*rate)
    S = N-V-I #becase vaccinated rate is change, so the susceptible people will change too
    S_list = [S]
    I_list = [1]
    R_list = [0]
     #for t in range(1000):
     #if S>0and N-V!=0, there will some people can be infected
     #calculate the probability of infection
     #else, prob = 0
     #randomly infected number S
     #randomly recovered number R
     #update number of S,I,R
     #add elements to arrays
    for t in range(1000):
        if S>0 and N>0:
            prob_infection = beta * (I / N) #the vaccinated people will never be infected
        else:
            prob_infection = 0
        if S>0 :
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
    #presents images with different probabilities
    plt.plot(I_list, label=f'{rate * 100}% vaccination',color=colors[i])
#set x,ylabel and title
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.legend()
#save the plot
plt.savefig("SIR model with different vaccination figure.png")
plt.show()