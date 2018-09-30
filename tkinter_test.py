import tkinter as tk
import mpmath

canvasLen = 400
# blockLen = 6表示环境为6X6的大小
blockLen = 7
# buidlingLen是每一个building的边长（px）
buidlingLen = mpmath.floor(canvasLen / blockLen)
# margin是路宽
margin = 10
buidlingLen = buidlingLen - margin

def modeling():
    #canvasLen = 400
    canvas = tk.Canvas(window,width = 3 * canvasLen, height = canvasLen)
    canvas.place(x=50, y=50, anchor = 'nw')

    # blockLen = 6表示环境为6X6的大小
    #blockLen = 12
    # buidlingLen是每一个building的边长（px）
    #buidlingLen = mpmath.floor(canvasLen / blockLen)
    # margin是路宽
    #margin = 10

    #buidlingLen = buidlingLen - margin

    drawMaps(canvas,blockLen,buidlingLen)
    drawMemory(canvas,blockLen,buidlingLen)
    startPos = [buidlingLen + margin , buidlingLen + margin]
    drawAgent(canvas,startPos[0],startPos[1])


def drawMaps(can,size,radius):
    for c in range(1,size+1):
        for r in range(1,size+1):
            rect = can.create_rectangle(10 + (c - 1)*(radius+10) ,10 + (r - 1)*(radius+10), 10 + (c - 1)*(radius+10) + radius, 10 + (r - 1)*(radius+10) + radius,fill = 'yellow')

def drawAgent(can,x,y):
    r = 10
    agent = can.create_oval(x,y,x+r,y+r,fill = 'red')

def drawMemory(can,size,radius):
    for c in range(1,size+1):
        for r in range(1,size+1):
            rect = can.create_rectangle(500 + (c - 1)*radius , 10 + (r - 1)*radius, 500 + (c - 1)*radius + radius, 10 +(r - 1)*radius + radius)




def start():
    a = 1
    print(var.get())
    startBut.destroy()
    r1.destroy()
    r2.destroy()
    modeling()

window = tk.Tk()
window.title('navigation model')
window.geometry('1000x500')

var = tk.StringVar()
r1 = tk.Radiobutton(window,text = 'megellan model original',variable = var, value = 'a')
r2 = tk.Radiobutton(window,text = 'megellan model V2',variable = var, value = 'b')
r1.place(x=100,y = 200,anchor = 'nw')
r2.place(x=300,y = 200,anchor = 'nw')

startBut = tk.Button(window,
                     width = 15,height = 2,
                     text = 'start',
                     command = start) #按钮响应的函数

#startBut.pack(side = 'bottom') #pack是按东西南北定位
startBut.place(x=170,y = 230,anchor = 'nw') #按具体坐标定位


window.mainloop()



