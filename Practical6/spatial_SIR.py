
#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#def initialize population (N for total population, V for infected population)
def initialize_population(N,V):
  #creat a 2d array, all elements are 0 for all people are susceptible
  population=np.zeros((N,N))
  #choose a position of infection randomly
  outbreak=np.random.choice(range(N),2)
  population[outbreak[0],outbreak[1]]=1

  return population

#def infected neighbor population, beta for infection rate
def infected_neighbor(population,beta):
  #fetch the size of array and copy current population
  N=population.shape[0]
  new_population=np.copy(population)
  #find the position of infection
  infected_indices=np.argwhere(population==1)

  #check 8 neighbor of each infections
  for x,y in infected_indices:
    for dx,dy in[(-1,0),(1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)]: #dx and dy are offset
      nx,ny=x+dx,y+dy
      #check the edge value of array
      if 0<=nx<N and 0<=ny<N:
        if population[nx,ny]==0: #only susceptible can be infected
          choice=np.random.choice([0,1], p=[1-beta,beta])
          if choice==1:
            new_population[nx,ny]=1

  return new_population

#def recover population, gamma for recovery rate
def recover(population,gamma):
  new_population=np.copy(population)
  #find the position of infection
  infected_indices=np.argwhere(population==1)
  #find an element in infected population randomly
  for x,y in infected_indices:
      choice=np.random.choice([0,1],p=[1-gamma,gamma])
      if choice==1:
          new_population[x,y]=2

  return new_population

#run 2d SIR model
#set necessary variables
def run_sir_model_2d(N=100,V=1,beta=0.3,gamma=0.1,iterations=100):
  population=initialize_population(N,V)
  plt.figure(figsize=(8,8))

  for t in range(iterations):
      #clear current graphics
      plt.clf()
      plt.imshow(population,cmap='viridis',interpolation='nearest')
      plt.title(f'Time step {t+1}')
      plt.colorbar(label='Population status (0:susceptible,1:infected,2:recovered)')

      population=infected_neighbor(population,beta) #infect neighbor
      population=recover(population,gamma) #recover

      #pause to observe animation
      plt.pause(0.05)

  plt.show()

#run the model  
run_sir_model_2d()