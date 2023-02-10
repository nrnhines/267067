from neuron import h, gui
h.load_file("init.hoc")

s = h.cADpyr232_L5_TTPC1_0fb1ca4724[0].soma[0]
ic = h.IClampQ(s(.5))
ic.delay = 1
ic.dur = 1
ic.amp = 5

from nrndc1 import run, DC1Access
dc1access = DC1Access(s(.5))

run(dc1access)
