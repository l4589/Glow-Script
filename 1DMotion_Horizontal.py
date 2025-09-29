Web VPython 3.2

timesteps=1000
vx=2
dt=0.01

xaxis=curve(pos=[vec(-10,0,0),vec(10,0,0)])
yaxis=curve(pos=[vec(0,-10,0),vec(0,10,0)])

ball=sphere(radius=1, color=color.red)

for i in range(timesteps):
    sleep(dt)
    dx=vx*dt
    ball.pos=vec(ball.pos.x+dx,0,0)
    sleep(dt)
