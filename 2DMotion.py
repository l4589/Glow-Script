Web VPython 3.2

a=vec(0,-9.8,0)

P0=vec(0,0,0) #intial position

V=vec(2,10,0)

dt=0.01



xaxis=curve(pos=[vec(-10,0,0),vec(10,0,0)])
yaxis=curve(pos=[vec(0,-10,0),vec(0,10,0)])

ball=sphere(radius=1, color=color.red, pos=P0)

while True:
    #find velocity
    V=V+a*dt
    #find new position
    ball.pos+=V*dt
    sleep(dt)
    if(ball.pos.y<=0):
        V.y=-V.y
    if (ball.pos.x<=0):
        V.y=-V.x
