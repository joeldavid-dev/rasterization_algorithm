#Algoritmo DDA (Digital Diferential Analizer)
from tkinter import *

#Ajustes de ventana
ventana = Tk()
ventana.title("Algoritmo DDA")

miFrame = Frame(ventana, width=900, height=600)
miFrame.pack()
miFrame.config(background="grey")

#El icono tiene un grosor especifico. en este caso es de: 20 px
pixel = PhotoImage(file="ico_emoji.png")
pixelWidth = 20

#Función que agrega un icono en las coordenadas dadas
def setPixel(posX, posY):
    Label(miFrame, image=pixel).place(x=pixelWidth*posX, y=pixelWidth*posY)

#Algoritmo
def lineaDDA (x0, y0, xEnd, yEnd):
    #Rango de pixeles en X y Y entre el punto inicial y el final
    dx = xEnd - x0
    dy = yEnd - y0

    #Elige cual rango es mayor, esa sera la cantidad de pasos
    if (abs(dx) > abs(dy)):
        steps = abs(dx)
    else:
        steps = abs(dy)
    
    Xinc = dx/steps
    Yinc = dy/steps
    print('dx =',dx,'dy =',dy,'steps =',steps, 'Xinc =',Xinc,'Yinc =',Yinc)

    #Aumenta Xinc y Yinc a x0, y0 y redondea
    setPixel(round(x0), round(y0))
    for i in range (steps):
        x0 += Xinc
        y0 += Yinc
        setPixel(round(x0), round(y0))
        
#lineaDDA(2,7,40,19)
lineaDDA(40,19,2,7)
ventana.mainloop()