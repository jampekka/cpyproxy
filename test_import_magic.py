#!/usr/bin/env pypy
# After this import cPython modules
# can be imported with cpyp-prefix,
# as seen below.
import cpyproxy.cpyp

import cpyp.matplotlib.pyplot as plt
import cpyp.numpy as cnp

rng = cnp.linspace(0, 10, 100)

plt.plot(rng, cnp.sin(rng))
plt.show()
