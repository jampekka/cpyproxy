# Run with pypy -m cpyproxy.black_magic
# Can't put it here as there's /usr/bin/env is
# catastrophically broken with arguments

import matplotlib.pyplot as plt
import numpy as np

rng = np.linspace(0, 10, 100)

plt.plot(rng, np.sin(rng))
plt.show()
