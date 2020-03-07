# Dependencies: Tkinter,Pillow
import tkinter
import math
from array import *
from PIL import Image,ImageTk

WinX=600
WinY=700

alpha=5
beta=-50
gamma=40

arr1=array('f',[0,0,0,0,0])
arr1[1]=0
arr1[2]=0.65*math.cos(alpha*math.pi/180)
arr1[3]=0.5*math.cos(beta*math.pi/180)
arr1[4]=0.5*math.cos(gamma*math.pi/180)

arr2=array('f',[0,0,0,0,0])
arr2[1]=0
arr2[2]=-0.65*math.sin(alpha*math.pi/180)
arr2[3]=-0.5*math.sin(beta*math.pi/180)
arr2[4]=-0.5*math.sin(gamma*math.pi/180)

arr3=array('f',[0,0,0,0,0])
arr3[1]=0
arr3[2]=0.65*math.sin(alpha*math.pi/180)
arr3[3]=0.5*math.sin(beta*math.pi/180)
arr3[4]=0.5*math.sin(gamma*math.pi/180)

arr4=array('f',[0,0,0,0,0])
arr4[1]=0.37
arr4[2]=0.65*math.cos(alpha*math.pi/180)
arr4[3]=0.5*math.cos(beta*math.pi/180)
arr4[4]=0.5*math.cos(gamma*math.pi/180)

arr5=array('f',[0,0,0,0,0])
arr5[1]=0
arr5[2]=0
arr5[3]=0
arr5[4]=0

arr6=array('f',[0,0,0,0,0])
arr6[1]=0
arr6[2]=2.5
arr6[3]=1.5
arr6[4]=1.7

X_WindowMin = -3
Y_WindowMin = 0
X_WindowMax = 3
Y_WindowMax = 7

X_ViewMin = 0
Y_ViewMin = 0
X_ViewMax = 600
Y_ViewMax = 700

def Win2View_X(Xw):
    return int((Xw-X_WindowMin)/(X_WindowMax-X_WindowMin)*(X_ViewMax-X_ViewMin)+X_ViewMin)
def Win2View_Y(Yw):
    return int(Y_ViewMax - ((Yw-Y_WindowMin)/(Y_WindowMax-Y_WindowMin)*(Y_ViewMax-Y_ViewMin)))

def View2Win_X(Xv):
    return (X_WindowMin+(Xv-X_ViewMin)*(X_WindowMax-X_WindowMin)/(X_ViewMax-X_ViewMin))
def View2Win_Y(Yv):
    return (Y_WindowMin+(Y_ViewMax-Yv)*(Y_WindowMax-Y_WindowMin)/(Y_ViewMax-Y_ViewMin))

bitmap = Image.new('RGB',((X_ViewMax-X_ViewMin),(Y_ViewMax-Y_ViewMin)), color='white')
pixels = bitmap.load()

# Ketebalan daun
limit=8
counter=0

# Garis transformasi daun
X_Leaf=(X_ViewMax-1)/2
Y_Leaf=Y_ViewMax-1
for count in range (0,250):
    pixels[X_Leaf,(Y_Leaf-count)]=(255,255,254)

# Membentuk pohon dari batang->daun atas->daun kiri->daun kanan
while counter<=limit:
    for count1 in range(X_ViewMin, X_ViewMax-1):
        for count2 in range(Y_ViewMin, Y_ViewMax-1):
            if(pixels[count1,count2]!=(255,255,255)):
                x1=View2Win_X(count1)
                y1=View2Win_Y(count2)
                x2=arr1[1]*x1+arr2[1]*y1+arr5[1]
                y2=arr3[1]*x1+arr4[1]*y1+arr6[1]
                x3=Win2View_X(x2)
                y3=Win2View_Y(y2)
                pixels[x3,y3]=(128,128,0)

                x2=(arr1[2]*x1)+(arr2[2]*y1)+arr5[2]
                y2=(arr3[2]*x1)+(arr4[2]*y1)+arr6[2]
                x3=Win2View_X(x2)
                y3=Win2View_Y(y2)
                pixels[x3,y3]=(0,128,0)

                x2=arr1[3]*x1+arr2[3]*y1+arr5[3]
                y2=arr3[3]*x1+arr4[3]*y1+arr6[3]
                x3=Win2View_X(x2)
                y3=Win2View_Y(y2)
                pixels[x3,y3]=(0,128,0)

                x2=arr1[4]*x1+arr2[4]*y1+arr5[4]
                y2=arr3[4]*x1+arr4[4]*y1+arr6[4]
                x3=Win2View_X(x2)
                y3=Win2View_Y(y2)
                pixels[x3,y3]=(0,128,0)
    counter+=1

root = tkinter.Tk()
root.title("Affine & Fractals Tree")
img = ImageTk.PhotoImage(bitmap)
panel = tkinter.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()