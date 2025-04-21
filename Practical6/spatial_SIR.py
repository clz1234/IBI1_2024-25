"""
import neccesary libraries
make array of all susceptible population
chose a random person as infected one
define deta and gamma
randomly select one infected individual (1).
for each time step:
    find all infected
    for each infected, infect neighbors with probability β.
    recover infected person with probability γ.
save plots at t=0,10,50,100.
"""

#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
#make array of all susceptible population, learn from Practical6_guide
population = np.zeros((100, 100))
#chose a random person as infected one, learn from Practical6_guide
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1
#chose these times'plot
plot_point = [0, 10, 50, 100]
plots = {}
#define deta and gamma
beta = 0.3
gamma = 0.05
#enter the loop
for i in range(101):
    #locate the positions of all current infected individuals
    infected_positions = np.where(population == 1)
    # store the new infections
    new_infections = []
    #infect the neighbor
    for x, y in zip(infected_positions[0], infected_positions[1]):
        potential_neighbors = []
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
            nx, ny = x + dx, y + dy
            #storage in potental_neighbors
            potential_neighbors.append((nx, ny))
        #remove the nx and ny which are not in this area
        valid_neighbors = [(nx, ny) for nx, ny in potential_neighbors if 0 <= nx < 100 and 0 <= ny < 100]
        for nx, ny in valid_neighbors:
            #create a new infected person
            if population[nx, ny] == 0:
                if np.random.rand() < beta:
                    new_infections.append((nx, ny))

        #if the person recoved, and mark the recoved one as 2
        if np.random.rand() < gamma:
            population[x, y] = 2
    for (nx, ny) in new_infections:
        population[nx, ny] = 1
    if i in plot_point:
        plots[i] = population.copy()
#create a graph containing multiple subgraphs
fig, axes = plt.subplots(1, len(plot_point), figsize=(15, 4), dpi=150)
for idx, i in enumerate(plot_point):
    axes[idx].imshow(plots[i], cmap= cm.get_cmap('viridis', 3), interpolation='nearest')
    axes[idx].set_title(f"Time {i}")
    axes[idx].axis('off')
#show the figure and save it 
plt.tight_layout()
plt.show()