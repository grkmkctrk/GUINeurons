import tkinter as tk
import tkinter.font as font

WIDTH = 1080
HEIGHT = 840

mywindow = tk.Tk() #Change the name for every window you make
font = font.Font(family='Helvetica', size=6, weight='bold')

canvas = tk.Canvas(mywindow, width=WIDTH, height=HEIGHT, borderwidth=0, highlightthickness=0, bg="brown")
canvas.grid()

## circle method
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

## window setting
mywindow.title("Neuron Network") #This will be the window title
mywindow.geometry(f"{WIDTH}x{HEIGHT}") #This will be the window size (str)
mywindow.minsize(540, 420) #This will be set a limit for the window's minimum size (int)
mywindow.configure(bg="brown") #This will be the background color


# katman sayisi exp = => [2 3 4 1]
def cizdir(much):
    baslax = 100
    aralik = 150
    
    # Neurons
    [
     canvas.create_circle(baslax + (i*aralik), (j+1)*HEIGHT/(much[i]+1), 25, fill="blue", outline="")
     for i in range(len(much)) 
     for j in range(much[i])
    ]
    # Connections
    [
     [canvas.create_line(baslax + (n*aralik), (i+1)*HEIGHT/(much[n]+1), baslax + ((n+1)*aralik), (j+1)*HEIGHT/(much[n+1]+1), width = 1,  fill = 'blue')]
     #[canvas.create_text(text=f'W{i}').place(x = ((baslax + ((n+1)*aralik))-(baslax + (n*aralik)))/2,y = (((i+1)*HEIGHT/(much[n]+1))-((j+1)*HEIGHT/(much[n+1]+1)))/2)]
     for n in range(len(much)-1)   # [0-2]
     for i in range(much[n])       # [0-3] [0-1] [0-2] # basla
     for j in range(much[n+1])     # [0-1] [0-2] [0-0] # bit
    ] 
    # Labels


cizdir([3, 5, 5, 3, 2])



mywindow.mainloop()