from graphics import GraphWin,Point,Line,Text,update

def trans_X(Xw):
    return int((Xw-Xwmin)/(Xwmax-Xwmin)*(Xvmax-Xvmin)+Xvmin)
def trans_Y(Yw):
    return int(Yvmax - ((Yw-Ywmin)/(Ywmax-Ywmin)*(Yvmax-Yvmin)))

Xwmin = -4
Xwmax = 4
Ywmax = 6
Ywmin = -2
Xvmin = 0
Xvmax = int(input("Enter your screen width : "))
Yvmax = int(input("Enter your screen height: "))
Yvmin = 0

win = GraphWin("Alexius Adhitya K - 18/424179/PA/18284", Xvmax, Yvmax,autoflush=False)

p1 = Point(trans_X(-3),trans_Y(0))
p2 = Point(trans_X(3),trans_Y(0))
line = Line(p1,p2)
line.draw(win)
p1 = Point(trans_X(0),trans_Y(5))
p2 = Point(trans_X(0),trans_Y(-1))
line = Line(p1,p2)
line.draw(win)

i = -3
while i <= 3:
    if i!=0:
        p1 = Point(trans_X(i),trans_Y(-0.1))
        teks = Text(p1,i)
        teks.draw(win)
    i = i+1

i=-1
while i<=5:
    if i!=0:
        p1 = Point(trans_X(0.05),trans_Y(i))
        teks = Text(p1,i)
        teks.draw(win)
    i = i+1

x = float(-2)
while x <= 2 :
    nx = x
    ny = x**2
    point = Point(trans_X(nx),trans_Y(ny))
    point.draw(win)
    update(2000)
    x = x + 0.001

win.getMouse()
win.close()
write()