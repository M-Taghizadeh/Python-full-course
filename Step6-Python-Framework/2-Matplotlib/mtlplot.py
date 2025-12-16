"""
Author: Mohammad Taghizadeh
YouTube: https://www.youtube.com/c/MohammadTaghizadeh
"""


import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(2,100)
print(data)

fig, axs = plt.subplots(2, 2, figsize=(5, 5))
axs[0, 0].hist(data[0])
axs[0, 1].scatter(data[0], data[1])
axs[1, 0].plot(data[0], data[1])
axs[1, 1].hist2d(data[0], data[1])

plt.show()