from isrbackend import *
import vpython as vp


#vector as x,y,z in matrix

sphere_location = vp.vector(0,0,0)
sphere2_location = vp.vector(2,0,0)

sphere1 = vp.sphere(pos=sphere_location, radius=0.5,color=vp.color.green)
sphere2 = vp.sphere(pos=sphere2_location, radius=0.5)

#defining time and position differentials
time = 0
dt = 0.01

while time <= 1000:
    vp.rate(240)
    sphere1.pos.x = cos(time)
    sphere2.pos.y = sin(time)
    time = time + dt
