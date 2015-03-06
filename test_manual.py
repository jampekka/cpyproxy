from cpyproxy import pyslave

cpyp = pyslave.pyslave(python='/usr/bin/python')
cnp = cpyp.modules['numpy']
cplt = cpyp.modules['matplotlib.pyplot']

rng = cnp.linspace(0, 10, 100)

cplt.plot(rng, cnp.sin(rng))
cplt.show()
