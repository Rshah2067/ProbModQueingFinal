import numpy as np
import numpy.random as rv
import tqdm
import matplotlib.pyplot as plt



service_state = False
queue_size = 0
process_time = 0
completion_time = 0
num_steps = 1000

queue_plot = []

lmb = 0.1 #arrival rate (arrivals/step)
mu = 2 #service rate (time to serve one)


for i in range(1,num_steps):
  queue_size += rv.exponential(lmb)
  queue_plot.append(queue_size)
  if service_state == False:
    process_time = rv.exponential(mu)
    completion_time = i + process_time
    service_state = True
  else:
    if completion_time > i:
      pass
    else:
      service_state = False
    
timesteps = range(len(queue_plot))

plt.figure(figsize=(10, 6))
plt.scatter(timesteps, queue_plot,s = 1, marker='.', linestyle='-', color='blue')
plt.title('Queue Length Over Time')
plt.xlabel('Timestep')
plt.ylabel('Queue Length')
plt.grid(True)
xticks = []
for step in timesteps:
  if step %50 ==0:
    xticks.append(step)

plt.xticks(xticks) # Ensure all timesteps are marked on the x-axis
plt.show()