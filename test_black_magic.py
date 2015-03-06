#!/usr/bin/env pypy
# After importing cpyproxy.black_magic,
# all non-found modules will be automagically
# try to be imported from cpython! Good luck!
import cpyproxy.black_magic

import matplotlib.pyplot as plt
import numpy as np

rng = np.linspace(0, 10, 100)

plt.plot(rng, np.sin(rng))
plt.show()
