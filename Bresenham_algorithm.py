# Algoritmo Bresenham para lineas con pendiente |m| < 1
from tkinter import *

# Ajustes de ventana
ventana = Tk()
ventana.title("Algoritmo Bresenham")

miFrame = Frame(ventana, width=1000, height=600)
miFrame.pack()
miFrame.config(background="grey")

# El icono tiene un grosor especifico. en este caso es de 20 px, para fines practicos
# se establece en 24 px
pixel = PhotoImage(file="ico_emoji.png")
pixelWidth = 24

# Función que agrega un icono en las coordenadas dadas
def setPixel(posX, posY):
    Label(miFrame, image=pixel).place(x=pixelWidth*posX, y=pixelWidth*posY)

# Algoritmo
def lineaBresenham (x0, y0, xEnd, yEnd):
    # Calculos iniciales
    dx = xEnd - x0
    dy = yEnd - y0
    p = 2 * dy - dx
    dosDy = 2 * dy
    dosDyMdx = 2 * (dy - dx)

    # Elige cual es el punto inicial en medida de cual es el punto mas cercano al origen
    if (x0 > xEnd):
        x = xEnd
        y = yEnd
        xEnd = x0
    else:
        x = x0
        y = y0
    
    print('dx =',dx,'dy =',dy,'p0 =',p, 'dosDy =',dosDy,'dosDyMdx =',dosDyMdx)
    
    setPixel(x, y)
    while (x < xEnd):
        x += 1
        if (p < 0):
            p += dosDy
        else:
            y += 1
            p += dosDyMdx
        setPixel(x, y)
        
lineaBresenham(2,7,40,19)
ventana.mainloop()