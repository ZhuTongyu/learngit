# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 16:09:35 2018

@author: ZTY
"""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Major ticks every 20, minor ticks every 5
major_ticks = np.arange(0, 101, 20)
minor_ticks = np.arange(0, 101, 5)

ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)

# And a corresponding grid
ax.grid(which='both',linestyle='--')

# Or if you want different settings for the grids:
ax.grid(which='minor', alpha=0.1)
ax.grid(which='major', alpha=0.8)
ax.tick_params(which = 'both', direction = 'in')
plt.show()
