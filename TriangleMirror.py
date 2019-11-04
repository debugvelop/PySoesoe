from graphics import *

win=GraphWin("TriangleMirror",1200,800)
GraphWin.setBackground(win,'white')
instruction=Text(Point(350,15),"")
instruction.setText("Instruction: Click 3 times anywhere to make triangle, then click 2 times anywhere to make mirror line")
instruction.setFace("arial")
instruction.setSize(11)
instruction.setTextColor("black")
instruction.draw(win)

click1=win.getMouse()
click1.draw(win)
x1=int(click1.getX())
y1=int(click1.getY())

click2=win.getMouse()
click2.draw(win)
x2=int(click2.getX())
y2=int(click2.getY())

click3=win.getMouse()
click3.draw(win)
x3=int(click3.getX())
y3=int(click3.getY())

p1=Point(x1,y1)
p2=Point(x2,y2)
p3=Point(x3,y3)
line1=Line(p1,p2)
line1.draw(win)
line2=Line(p2,p3)
line2.draw(win)
line3=Line(p1,p3)
line3.draw(win)

click4=win.getMouse()
click4.draw(win)
clickx4=int(click4.getX())
clicky4=int(click4.getY())

click5=win.getMouse()
click5.draw(win)
clickx5=int(click5.getX())
clicky5=int(click5.getY())

mirror=Line(click4,click5)
mirror.draw(win)

sideA=clicky5-clicky4
sideB=(clickx5-clickx4)*-1
sideC=(-sideA*clickx4)-(sideB*clicky4)

mirrorDist=(sideA**2+sideB**2)
side_A=sideA/(mirrorDist**0.5)
side_B=sideB/(mirrorDist**0.5)
side_C=sideC/(mirrorDist**0.5)

def distPoint(x,y,sideA,sideB,sideC):
    val=sideA*x+sideB*y+sideC
    return Point(x-2*sideA*val,y-2*sideB*val)

p_1=distPoint(x1,y1,side_A,side_B,side_C)
p_2=distPoint(x2,y2,side_A,side_B,side_C)
p_3=distPoint(x3,y3,side_A,side_B,side_C)

line_1=Line(p_1,p_2)
line_1.draw(win)
line_2=Line(p_2,p_3)
line_2.draw(win)
line_3=Line(p_1,p_3)
line_3.draw(win)

win.getMouse()
win.close()