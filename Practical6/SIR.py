
#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#define the basic variables 
N=10000
population_infected=1
population_susceptible=N-1
population_recovered=0
beta=0.3 #infection rate
gamma=0.05 #recovery rate

#creat array to store new recovered and infected population
infected_list=[population_infected]
susceptible_list=[population_susceptible]
recovered_list=[population_recovered]

#set time step
time_steps=1000

#time loop to imitate epodemic
for t in range(time_steps):
    prob_infection=beta*(population_infected/N) #the porb of infection

    infected_indices=np.random.choice(range(2), size=population_susceptible, p=[1-prob_infection,prob_infection])
    new_infection=np.sum(infected_indices) #new infected population

    population_susceptible-=new_infection
    population_infected+=new_infection

    recovered_indices=np.random.choice(range(2), size=population_infected, p=[1-gamma,gamma])
    new_recovery=np.sum(recovered_indices) #new recovered population

    population_recovered+=new_recovery
    population_infected-=new_recovery

    #store the new population to array
    infected_list.append(population_infected)
    susceptible_list.append(population_susceptible)
    recovered_list.append(population_recovered)

#draw the plot
plt.figure(figsize=(6,4),dpi=150)
plt.plot(infected_list, label='Infected',color='red')
plt.plot(susceptible_list, label='Susceptible',color='blue')
plt.plot(recovered_list,label='recovered',color='green')
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Mode')
plt.legend()

plt.show()

plt.savefig('SIR MODEL',format='png')