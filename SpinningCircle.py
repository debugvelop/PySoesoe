#Requirement: Python 3.6 and python-tk
from tkinter import *
from tkinter import ttk
import asyncio
import math

root = Tk()
root.title("Alexius Adhitya K - 18/424179/PA/18284")

tx1 = StringVar()
ty1 = StringVar()
tx2 = StringVar()
ty2 = StringVar()
tr = StringVar()

async def drawCircle1(centerx, centery, r, deg):
    k = 0
    while k < (2*math.pi*r):
        x = centerx+round(r*math.cos(deg))
        y = centery+round(r*math.sin(deg))
        canvas.create_line(x,y,x+1,y)
        deg = deg+1/r
        root.update_idletasks()
        k = k + 1
        await asyncio.sleep(0.01)
    return

async def drawCircle2(centerx, centery, r, deg):
    k = 0
    while k < (2*math.pi*r):
        x = centerx+round(r*math.cos(deg))
        y = centery+round(r*math.sin(deg))
        canvas.create_line(x,y,x+1,y)
        deg = deg-1/r
        root.update_idletasks()
        k = k + 1
        await asyncio.sleep(0.01)
    return

async def drawCircle3(centerx, centery, r, deg):
    k = 0
    while k < (2*math.pi*r):
        x = centerx+round(r*math.cos(deg))
        y = centery+round(r*math.sin(deg))
        canvas.create_line(x,y,x+1,y)
        deg = deg-1/r
        root.update_idletasks()
        k = k + 1
        await asyncio.sleep(0.01)
    return

async def drawCircle4(centerx, centery, r, deg):
    k = 0
    while k < (2*math.pi*r):
        x = centerx+round(r*math.cos(deg))
        y = centery+round(r*math.sin(deg))
        canvas.create_line(x,y,x+1,y)
        deg = deg+1/r
        root.update_idletasks()
        k = k + 1
        await asyncio.sleep(0.01)
    return

async def drawLine1(x1, y1, x2, y2):
    if x2 < x1:
        if y1 < y2:
            currentposX = x1
            currentposY = y1
            gradient = (y2 - y1) / (x2 - x1)
            while currentposX != x2:
                canvas.create_line(currentposX, currentposY, currentposX-1, currentposY+1)
                currentposX = currentposX - 1
                currentposY = currentposY - gradient
                root.update_idletasks()
                await asyncio.sleep(0.01)
            return
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        if y1 < y2:
            currentposX = x2
            currentposY = y2
            gradient = (y2 - y1) / (x2 - x1)
            while currentposX != x1:
                canvas.create_line(currentposX, currentposY, currentposX+1, currentposY+1)
                currentposX = currentposX - 1
                currentposY = currentposY - gradient
                root.update_idletasks()
                await asyncio.sleep(0.01)
            return
    currentposX = x1
    currentposY = y1
    gradient = (y2 - y1) / (x2 - x1)
    while currentposX != x2:
        canvas.create_line(currentposX, currentposY, currentposX+1, currentposY+1)
        currentposX = currentposX + 1
        currentposY = currentposY + gradient
        root.update_idletasks()
        await asyncio.sleep(0.01)
    return

async def startDraw(*args):
    x1 = float(tx1.get())
    y1 = float(ty1.get())
    x2 = float(tx2.get())
    y2 = float(ty2.get())
    r = float(tr.get())
    gradient = (x2-x1)/(y2-y1)*-1
    k = math.sqrt((r**2)/(1+gradient**2))
    k = k * -1
    circleCenter1x = x1 + k
    circleCenter1y = y1 + k * gradient
    k = k * -1
    circleCenter2x = x2 + k
    circleCenter2y = y2 + k * gradient
    canvas.delete("all")
    if x1<x2 and y1<y2:
        degree = abs(math.acos(abs(k)/r)) * -1
        await drawCircle1(circleCenter1x, circleCenter1y, r, degree)
        await drawLine1(x1, y1, x2, y2)
        await drawCircle2(circleCenter2x, circleCenter2y, r, degree + math.pi)
    elif x1>x2 and y1>y2:
        degree = abs(math.acos(abs(k)/r)) * -1
        await drawCircle3(circleCenter1x, circleCenter1y, r, degree)
        await drawLine1(x1, y1, x2, y2)
        await drawCircle4(circleCenter2x, circleCenter2y, r, degree + math.pi)
    elif x1<x2 and y1>y2:
        degree = abs(math.acos(abs(k)/r)) * 1
        await drawCircle3(circleCenter1x, circleCenter1y, r, degree)
        await drawLine1(x1, y1, x2, y2)
        await drawCircle4(circleCenter2x, circleCenter2y, r, degree + math.pi)
    elif x1>x2 and y1<y2:
        degree = abs(math.acos(abs(k)/r)) * 1
        await drawCircle1(circleCenter1x, circleCenter1y, r, degree)
        await drawLine1(x1, y1, x2, y2)
        await drawCircle2(circleCenter2x, circleCenter2y, r, degree + math.pi)

def do_task():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(startDraw())
    finally:
        pass
        
canvas = Canvas(root, background="white", width=600, height=600)
canvas.grid(column=2, row=0)
mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W))
root.columnconfigure(0, weight=1)

entryx1 = ttk.Entry(mainframe, width=10, textvariable=tx1)
entryy1 = ttk.Entry(mainframe, width=10, textvariable=ty1)
entryx2 = ttk.Entry(mainframe, width=10, textvariable=tx2)
entryy2 = ttk.Entry(mainframe, width=10, textvariable=ty2)
entryr = ttk.Entry(mainframe, width=10, textvariable=tr)
entryx1.focus()
entryx1.grid(column=1, row=1, sticky=N + W)
entryy1.grid(column=1, row=2, sticky=N + W)
entryx2.grid(column=1, row=3, sticky=N + W)
entryy2.grid(column=1, row=4, sticky=N + W)
entryr.grid(column=1, row=5, sticky=N + W)
ttk.Label(mainframe, text="Input X1:").grid(column=0, row=1, sticky=(N, W))
ttk.Label(mainframe, text="Input Y1:").grid(column=0, row=2, sticky=(N, W))
ttk.Label(mainframe, text="Input X2:").grid(column=0, row=3, sticky=N + W)
ttk.Label(mainframe, text="Input Y2:").grid(column=0, row=4, sticky=N + W)
ttk.Label(mainframe, text="Input R:").grid(column=0, row=5, sticky=N + W)

startButton = ttk.Button(mainframe, text="Start", command=do_task)
startButton.grid(column=1, row=6, sticky=N + W)

root.mainloop()