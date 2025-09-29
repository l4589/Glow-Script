Web VPython 3.2

timesteps=1000
vx=2
vy=0
dt=0.01
a=-9.81


xaxis=curve(pos=[vec(-10,0,0),vec(10,0,0)])
yaxis=curve(pos=[vec(0,-10,0),vec(0,10,0)])

ball=sphere(radius=1, color=color.red, pos=vec(0,10,0))

for i in range(timesteps):
    sleep(dt)
    dv=a*dt
    vy=vy+dv
    dy=vy*dt
    ball.pos=vec(0,ball.pos.y+dy,0)
    sleep(dt)
    if(ball.pos.y<=0):
        vy=-vy
