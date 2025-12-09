import matplotlib.pyplot as plt

# Ensure queue_plot is defined. Assuming it's already available from previous cells.
# In the provided notebook state, the variable is named 'queue_plot'.
# If it were 'queue_size' as previously inferred, please adjust the variable name.
def plot (queue_plot)
    timesteps = range(len(queue_plot))

    plt.figure(figsize=(10, 6))
    plt.plot(timesteps, queue_plot, marker='o', linestyle='-', color='blue')
    plt.title('Queue Length Over Time')
    plt.xlabel('Timestep')
    plt.ylabel('Queue Length')
    plt.grid(True)
    plt.xticks(timesteps) # Ensure all timesteps are marked on the x-axis
    plt.show()