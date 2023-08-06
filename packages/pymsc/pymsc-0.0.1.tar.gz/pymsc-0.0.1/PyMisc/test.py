import pymisc
import time as t

p = pymisc.PyMisc("I'm foo!")

p.oi()

p.customExit(cls=True, isDelayed=True, delay=3)
