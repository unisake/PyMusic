#main.py
import PyMusic as pm  

scale = pm.Scale("C")

beat = pm.beat

master = pm.null(12*pm.beat)

def sine(a,b):
    return pm.sine(a,b)

C4 = scale[1]
E4 = scale[3]
G4 = scale[5]
C5 = scale[1,1]

master[:2*beat] += sine(2*beat,C4)
master[2*beat:3*beat] += sine(beat,E4)
master[2*beat:3*beat] += sine(beat,G4)

master.out("test.wav")