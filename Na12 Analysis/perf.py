from neuron import h, gui
from neuron import coreneuron
import time

pc = h.ParallelContext()

h.load_file("init.hoc")

s = h.cADpyr232_L5_TTPC1_0fb1ca4724[0].soma[0]
ic = h.IClampQ(s(.5))
ic.delay = 1
ic.dur = 1
ic.amp = 5

def run(corenrn=0):
    coreneuron.enable = corenrn
    h.dt = 0.025
    pc.set_maxstep(1000)
    h.finitialize(-65)
    x = time.time()
    pc.psolve(100)
    print("psolve time = ", time.time() - x)
    print("h.dt = ", h.dt)
    coreneuron.enable = 0

run(0)
h.cvode.cache_efficient(1)
run(0)
run(1)
