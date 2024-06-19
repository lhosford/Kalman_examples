import random
import matplotlib.pyplot as plt

#Create a super simple "plant" that only generates a 
#random number between an upper and lower bound.

def stationary_plant(lower,upper):
    y = random.uniform(lower,upper)
    return y

#alpha beta filter 
#n is number of times filter has been run
#z_n is current measurement
#x_0 is past estimate
def alpha_beta_filter(n,z_n,x_0):
    x_n = x_0 + 1/n*(z_n- x_0)
    return x_n

initial_guess = 10
cycle = 100
estimate_0= initial_guess
cycle_number = [0]*cycle
measurement = [0]*cycle
estimate = [0]*cycle
for i in range(0,cycle):
    cycle_number[i] = i+1
    measurement[i] = stationary_plant(5,15)
    estimate[i] = alpha_beta_filter(i+1,measurement[i],estimate_0)
    estimate_0 = estimate[i]

fig, ax = plt.subplots()
ax.plot(cycle_number,estimate,'o',label='estimate')
ax.plot(cycle_number,measurement,'x',label='measurement')
ax.plot(cycle_number,[initial_guess]*cycle,label='true value')
ax.legend()
ax.set_xlabel('cycle number')
ax.set_ylabel('static weight')
plt.show()
#print(estimate)
#print(measurement)
#print(cycle_number)
    

