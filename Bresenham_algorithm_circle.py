# Algoritmo Bresenham del punto medio para circunferencias
from tkinter import *

# Ajustes de ventana
ventana = Tk()
ventana.title("Algoritmo Bresenham circunferencia de punto medio")

miFrame = Frame(ventana, width=1000, height=700)
miFrame.pack()
miFrame.config(background="grey")

# El icono tiene un grosor especifico. en este caso es de 10 px, para fines practicos,
# se establece en 14 px.
pixel = PhotoImage(file="ico_emoji_mini.png")
pixelWidth = 14

# Función que agrega un icono en las coordenadas dadas
def setPixel(posX, posY):
    Label(miFrame, image=pixel).place(x=pixelWidth*posX, y=pixelWidth*posY)

# Función que determina los puntos de simetría para los siete octantes
# y translada los puntos a partir del centro de la circunferencia.
def setOctaPixels(pX, pY, Xcent, Ycent):
    setPixel(pX + Xcent, pY + Ycent)
    setPixel(pX + Xcent, -pY + Ycent)
    setPixel(-pX + Xcent, pY + Ycent)
    setPixel(-pX + Xcent, -pY + Ycent)
    setPixel(pY + Xcent, pX + Ycent)
    setPixel(pY+ Xcent, -pX + Ycent)
    setPixel(-pY + Xcent, pX + Ycent)
    setPixel(-pY + Xcent, -pX + Ycent)

# Algoritmo
def bresenhamCircle(xc, yc, rad):
    # Calculos iniciales
    pk = 1 - rad
    
    x = 0
    y = rad
    # Algoritmo
    setOctaPixels(x, y, xc, yc)

    while not(x >= y):
        if (pk < 0):
            x += 1
            pk = pk + 2*x + 1
        else:
            x += 1
            y -= 1
            pk = pk + (2*x + 2) + 1 -(2*y - 2)
        
        setOctaPixels(x, y, xc, yc)
    

bresenhamCircle(35,25,20)
ventana.mainloop()