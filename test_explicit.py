#!/usr/bin/env pypy
import cpyproxy.cpyp
import cpyp.matplotlib.pyplot as plt
import cpyp.numpy as cnp

rng = cnp.linspace(0, 10, 100)

plt.plot(rng, cnp.sin(rng))
plt.show()
