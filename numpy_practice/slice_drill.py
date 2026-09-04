import numpy as np

ping = np.array([
    [10, 25, 30],
    [45, 12, 18],
    [50, 60, 40]
])

betlog = ping[:, 1]
print("Slice:", betlog)
mean = ping.mean(axis=1)
print("Average response time:", mean)
