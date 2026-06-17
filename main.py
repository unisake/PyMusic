#main.py
import PyMusic as pm
import numpy as np  

scale = pm.Scale("C")

C4 = scale[1]
#print(type(C4), C4)
sine_C4 = pm.sine(4*pm.beat,C4)
sine_C4.out("sine_C4.wav")