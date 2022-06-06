import numpy as np
import matplotlib.pyplot as plt

# degrees to radian converter
def mm_to_meters(d):
    m=1000
    return d/m

qi = float(input('qi = ')) # initial position
qi = mm_to_meters(qi)

vi = float(input('vi = ')) # initial velocity
vi = mm_to_meters(vi)

qf = float(input('qf = ')) # final position
qf = mm_to_meters(qf)

vf = float(input('vf = ')) # final velocity
vf = mm_to_meters(vf)

ti = float(input('ti = ')) # initial time
tf = float(input('tf = ')) # final time

# Cubic
# Solve the solution for q(t) = a + (3*(b-a)/c**2)*t**2 - (2*(b-a)/c**3)*t**3

x = np.arange(ti,tf,0.05)

def cubic(t,a,b,c):
    return a + (3*(b-a)/c**2)*t**2 - (2*(b-a)/c**3)*t**3

y = cubic(x,qi,qf,tf)

plt.figure()
plt.plot(x,y,'b',linestyle='-')
plt.text(1,-1.5,'q(t) = a + (3*(b-a)/c**2)*t**2 - (2*(b-a)/c**3)*t**3')
plt.grid(True)
plt.show()