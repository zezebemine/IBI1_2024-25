
#import necessary libraries
from matplotlib import cm 
import numpy as np
import matplotlib.pyplot as plt

#define the basic variables 
N=10000
beta=0.3 #infection rate
gamma=0.05 #recovery rate
time_steps=1000

#determine different vaccination rate
vaccination_rate=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

#creat empty list for different vaccination rate to store population of infected
infected_counts={rate: [] for rate in vaccination_rate}

#def variables in different vaccination rate
for rate in vaccination_rate:
    population_recovered=0
    population_infected=1
    population_susceptible=N-int(rate*N)-population_infected
    population_vacciated=int(rate*N)

    #time loop to imitate epodemic
    for t in range(time_steps):
        prob_infection=beta*(population_infected/N) #the porb of infection

        #ensuer population susceptible not less than 0
        if population_susceptible <=0:
            population_susceptible=0

        infected_indices=np.random.choice(range(2), size=population_susceptible, p=[1-prob_infection,prob_infection])
        new_infection=np.sum(infected_indices) #new infected population

        population_susceptible-=new_infection
        population_infected+=new_infection

        recovered_indices=np.random.choice(range(2), size=population_infected, p=[1-gamma,gamma])
        new_recovery=np.sum(recovered_indices) #new recovered population

        population_recovered+=new_recovery
        population_infected-=new_recovery

        #store the new population of infected
        infected_counts[rate].append(population_infected)

#draw result
#determine the size and dpi of graphy
plt.figure(figsize=(6,4),dpi=150)

#draw the number of infected people corresponding to different vaccination rate
for rate, counts in infected_counts.items():
    plt.plot(counts,label=f'{int(rate*100)}%',color=cm.viridis(int(rate*100)))

plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR model in different vaccination rate')
plt.legend()

plt.show()

plt.savefig('SIR model in different vaccination rate', format='png')