import tkinter as tk
import math
import cmath

canvasWidth=400
canvasHeight=400
labels=['Toggle: R^2', ' Toggle: C ']

def c2xy(event, zoom):
        x=((event.x-canvasWidth/2)/zoom)
        y=((canvasHeight/2 - event.y)/zoom)
        return {'x':x, 'y':y}
def xy2c(x, y, zoom):
        cx=int(zoom*x+canvasWidth/2)
        cy=int(-1*zoom*y+canvasHeight/2)
        return {'cx':cx, 'cy':cy}

#root.title("Complex Plotter")
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Complex Plotter 2")

        self.drawframes=tk.Frame(self.master, relief='sunken', bd=2)
        self.drawframes.pack(side='top')

        self.domain=tk.Frame(self.drawframes, relief='sunken', bd=2)
        self.domain.pack(side='left')
        self.domainLabel=tk.Label(self.domain, text="here's the domain")
        self.domainLabel.pack()
        self.domainCanvas=tk.Canvas(self.domain, width=canvasWidth, height=canvasHeight, background='#FFF9FF')
        self.domainCanvas.pack()
        self.domainDot=self.domainCanvas.create_oval((2,2,2,2), fill='#000010')
        self.domainXAxis=self.domainCanvas.create_line(0, canvasHeight/2,canvasWidth,canvasHeight/2)
        self.domainYAxis=self.domainCanvas.create_line(canvasWidth/2,0,canvasWidth/2,canvasHeight)
        self.domainZoom=tk.Scale(self.domain, from_=1, to=20, tickinterval=0.1, length=0.5*canvasWidth, orient='horizontal', command=self.updateDZTic)
        self.domainZoom.pack(side='right')
        tk.Label(self.domain, text='Zoom: ').pack(side='right')
        self.domainZoomDirection=tk.IntVar()
        self.dZoomBig=tk.Radiobutton(self.domain, text='bigger', variable=self.domainZoomDirection, value=1, indicatoron=0)
        self.dZoomBig.pack(side='left')
        self.dZoomSmall=tk.Radiobutton(self.domain, text='smaller', variable=self.domainZoomDirection, value=-1, indicatoron=0)
        self.dZoomSmall.pack(side='left')
        self.dZTicX=self.domainCanvas.create_text(((canvasWidth/2)*(1.2),(canvasHeight/2)*(0.97)), text='')
        self.dZTicY=self.domainCanvas.create_text(((canvasWidth/2)*(1.06),(canvasHeight/2)*(0.8)), text='')
        self.domainCanvas.create_line((canvasWidth/2)*(1.2), (canvasHeight/2)*(0.98), (canvasWidth/2)*(1.2), (1.02)*(canvasHeight/2), width=2)
        
        self.dTraceLine=self.domainCanvas.create_line(0,0,0,0)

        self.image=tk.Frame(self.drawframes, relief='sunken', bd=2)
        self.image.pack(side='right')
        self.imageLabel=tk.Label(self.image, text="here's the image")
        self.imageLabel.pack()
        self.imageCanvas=tk.Canvas(self.image, width=canvasWidth, height=canvasHeight, background='#F7FFFF')
        self.imageCanvas.pack()
        self.imageDot=self.imageCanvas.create_oval((2,2,2,2), fill='#100000')
        self.imageXAxis=self.imageCanvas.create_line(0, canvasHeight/2,canvasWidth,canvasHeight/2)
        self.imageYAxis=self.imageCanvas.create_line(canvasWidth/2,0,canvasWidth/2,canvasHeight)
        self.imageZoom=tk.Scale(self.image, from_=1, to=20, tickinterval=0.1, length=0.5*canvasWidth, orient='horizontal', command=self.updateIZTic)
        self.imageZoom.pack(side='right')
        tk.Label(self.image, text='Zoom: ').pack(side='right')
        self.imageZoomDirection=tk.IntVar()
        self.iZoomBig=tk.Radiobutton(self.image, text='bigger', variable=self.imageZoomDirection, value=1, indicatoron=0)
        self.iZoomBig.pack(side='left')
        self.iZoomSmall=tk.Radiobutton(self.image, text='smaller', variable=self.imageZoomDirection, value=-1, indicatoron=0)
        self.iZoomSmall.pack(side='left')
        self.iZTicX=self.imageCanvas.create_text(((canvasWidth/2)*(1.2),(canvasHeight/2)*(0.97)), text='')
        self.iZTicY=self.imageCanvas.create_text(((canvasWidth/2)*(1.06),(canvasHeight/2)*(0.8)), text='')
        self.imageCanvas.create_line((canvasWidth/2)*(1.2), (canvasHeight/2)*(0.98), (canvasWidth/2)*(1.2), (1.02)*(canvasHeight/2), width=2)
 
        self.iTraceLine=self.imageCanvas.create_line(0,0,0,0)



        self.HelpButt=tk.Button(self.master, text='Help?', command=self.helpWin)
        self.HelpButt.pack(pady=10)



        self.otherFrame=tk.Frame(self.master, relief='raised', bd=2)
        self.otherFrame.pack()
        '''self.brpad=tk.Frame(self.otherFrame)
        self.brpad.pack(side='right')
        tk.Label(self.brpad, text='some help notes might go here idk').pack(side='right')
'''
        self.funcFrame=tk.Frame(self.otherFrame)
        self.funcFrame.pack(side='left')
        self.trace=tk.IntVar()
        self.traceButt=tk.Checkbutton(self.funcFrame, text=':Trace On', var=self.trace)
        self.traceButt.pack(side='top')
        
        self.whichF=tk.IntVar()
        self.whichFStr=tk.StringVar()
        self.whichFStr.set('Toggle: R^2')
        self.whichF.set(0)
        self.whichFButt=tk.Button(self.funcFrame, text=labels[0], command=self.toggle)
        self.whichFButt.pack()

        self.R2R2Frame=tk.Frame(self.funcFrame, relief='sunken', bd=2)
        self.R2R2Frame.pack(side='left', padx=7)
        self.CCFrame=tk.Frame(self.funcFrame, relief='sunken', bd=2)
        self.CCFrame.pack(side='right', pady=15)
        tk.Label(self.R2R2Frame, text='f : R^2 -> R^2 defined by f(x, y)=').pack(side='top')
        self.RFuncIText=tk.Text(self.R2R2Frame, height=2, width=48)
        self.RFuncIText.pack()
        self.RFuncIText.insert('1.0', 'x')
        tk.Label(self.R2R2Frame, text='+').pack()
        self.RFuncJText=tk.Text(self.R2R2Frame, height=2, width=48)
        self.RFuncJText.pack()
        self.RFuncJText.insert('1.0', 'y')
        #self.RFuncButt=tk.Button(self.R2R2Frame, text='Go!', command=self.function)
        #self.RFuncButt.pack()

        tk.Label(self.CCFrame, text='f : C -> C defined by f(z)=').pack(side='left')
        self.CFuncText=tk.Text(self.CCFrame, height=2, width=30)
        self.CFuncText.pack(padx=5)
        self.CFuncText.insert('1.0','z')


    def updateDZTic(self, value='none'):
        self.domainCanvas.itemconfig(self.dZTicX, text=str(round(canvasWidth/(10*(self.domainZoom.get())**(self.domainZoomDirection.get())), 2)))
        self.domainCanvas.itemconfig(self.dZTicY, text=str(round(canvasWidth/(10*(self.domainZoom.get())**(self.domainZoomDirection.get())), 2)))
    def updateIZTic(self, value='none'):
        self.imageCanvas.itemconfig(self.iZTicX, text=str(round(canvasWidth/(10*(self.imageZoom.get())**(self.imageZoomDirection.get())), 2)))
        self.imageCanvas.itemconfig(self.iZTicY, text=str(round(canvasWidth/(10*(self.imageZoom.get())**(self.imageZoomDirection.get())), 2)))

    def toggle(self):
        self.whichF.set(1-self.whichF.get())
        self.whichFStr.set(labels[1-labels.index(self.whichFStr.get())])
        self.whichFButt.config(text=self.whichFStr.get())

    def R2Function(self):
        fx=self.RFuncIText.get('1.0','end-1c')
        fy=self.RFuncJText.get('1.0','end-1c')
        return {'fx':fx, 'fy':fy}


    def drawDot(self, event):
        if self.whichF.get()==0:
            f=self.R2Function
            zoomD=(self.domainZoom.get())**(self.domainZoomDirection.get())
            zoomI=(self.imageZoom.get())**(self.imageZoomDirection.get())
            x=c2xy(event, zoomD)['x']
            y=c2xy(event, zoomD)['y']
            #print('(x=%d, y=%d)' % (x, y))
            self.domainCanvas.coords(self.domainDot, event.x-3,event.y-3,event.x+3,event.y+3)
            fx=eval(f()['fx'])
            fy=eval(f()['fy'])
            cx=xy2c(int(fx),int(fy),zoomI)['cx']
            cy=xy2c(int(fx),int(fy),zoomI)['cy']
            #print('(cx=%d, cy=%d)' % (cx, cy))
            self.imageCanvas.coords(self.imageDot, cx-3,cy-3,cx+3,cy+3)
            if(self.trace.get()==1):
                self.domainCanvas.coords(self.dTraceLine, canvasWidth/2, canvasHeight/2, event.x, event.y)
                self.imageCanvas.coords(self.iTraceLine, canvasWidth/2, canvasHeight/2, cx, cy)
        
        else:
            f=self.CFuncText.get('1.0','end-1c')
            zoomD=(self.domainZoom.get())**(self.domainZoomDirection.get())
            zoomI=(self.imageZoom.get())**(self.imageZoomDirection.get())
            x=c2xy(event, zoomD)['x']
            y=c2xy(event, zoomD)['y']
            #z=complex(x,y)
            self.domainCanvas.coords(self.domainDot, event.x-3,event.y-3,event.x+3,event.y+3)
            fx=eval(f).real
            fy=eval(f).imag
            cx=xy2c(int(fx),int(fy),zoomI)['cx']
            cy=xy2c(int(fx),int(fy),zoomI)['cy']
            #print('(cx=%d, cy=%d)' % (cx, cy))
            self.imageCanvas.coords(self.imageDot, cx-3,cy-3,cx+3,cy+3)
            if(self.trace.get()==1):
                self.domainCanvas.coords(self.dTraceLine, canvasWidth/2, canvasHeight/2, event.x, event.y)
                self.imageCanvas.coords(self.iTraceLine, canvasWidth/2, canvasHeight/2, cx, cy)

    def helpWin(self):
        newthingy=tk.Toplevel()
        newthingy.title('Help')
        tk.Label(newthingy, text=helpstring).pack(side='left', anchor='w')

helpstring='''hi
-----------------
-Drag around a point on the domain space to have a dot correspondingly move around in the image space, according to the function you set.

-Toggle lets you choose between a vector-valued function of x and y, or a complex valued function of z. Basically, use the former if you want something non-holomorphic I guess.

-Enter valid Pythonic expressions to set the functions, and make sure the Toggle is set right.

-The slider bar sets the scale factor. Choosing 'bigger' makes it zoom in, choosing 'smaller' makes it zoom out, both with the same slider bar.

-'Trace on' connects a line from the dot to the origin, to visualise it as a vector.
--------------------------------
-Have fun please lol'''

def printcoords(event):
        print ("(%d, %d)" % (event.x,event.y))


root = tk.Tk()

thingy=MyFirstGUI(root)

thingy.domainCanvas.bind("<B1-Motion>", printcoords)
thingy.domainCanvas.bind("<B1-Motion>", thingy.drawDot)

root.mainloop()