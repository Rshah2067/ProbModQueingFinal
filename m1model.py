import numpy as np
import numpy.random as rv
import tqdm


service_state = false
queue_size = 0
process_time = 0
completion_time = 0
num_steps = 1000

queue_plot = []

lmb = 0.1 #arrival rate (arrivals/step)
mu = 2 #service rate (time to serve one)


for i in tqdm(range(1,num_steps)):
  queue_size += rv.exponential(lmb)
  queue_plot.append(queue_size)
  if service_state == false:
    process_time = rv.exponential(mu)
    completion_time = i + process_time
    service_state = true
  else:
    if completion_time > i:
      pass
    else:
      service_state = false
