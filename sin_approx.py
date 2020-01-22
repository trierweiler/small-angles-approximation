# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:32:30 2020

Script to demonstrate small angles approximation sin(theta) = theta

@author: https://www.linkedin.com/in/gabrieltribeiro/
"""

import math
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 45, 46)
y_sin = np.sin(theta*math.pi/180)

err_sin = np.cumsum(abs(100*(y_sin[1:] - theta[1:]*math.pi/180) / y_sin[1:]))

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10,5))

axes[0].plot(theta, theta*math.pi/180)
axes[0].plot(theta, y_sin)
axes[0].legend(['theta', 'sin(theta)'])
axes[0].set_xlabel('Angle (deg)', style='italic', fontsize='large')
axes[0].set_ylabel('Function value', style='italic', fontsize='large')
axes[0].set_xticks(ticks=np.linspace(0, 45, 10))
axes[0].grid()

axes[1].bar(theta[1:16], err_sin[0:15])
axes[1].hlines(y=1, xmin=theta[1], xmax=theta[16], linestyles='dashed')
axes[1].set_xlabel('Angle (deg)', style='italic', fontsize='large')
axes[1].set_ylabel('% of error', style='italic', fontsize='large')
axes[1].set_xticks(ticks=np.linspace(0, 15, 16))
