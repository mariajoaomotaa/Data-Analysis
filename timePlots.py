
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import datetime
import numpy as np

class TimePlot():
  def __init__ (self, root, label, time_window = 20):
    self.time_window = time_window
    self.fig = Figure( dpi=100)
    self.ax = self.fig.add_subplot()
    self.ax.set_xlabel('')
    self.label = label
    
    self.x = []
    self.y = []
    #self.line = self.ax.plot(self.x,self.y)
    self.canvas = FigureCanvasTkAgg(self.fig, master=root)
    self.canvas.draw()

    self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
  
  def update(self, new_val):
    t = datetime.datetime.now()
    
    self.x.append( t )    
    self.y.append( new_val )

    if len(self.y) == 1:
      self.line = self.ax.plot(self.x,self.y)
      self.ax.legend(self.line, self.label, loc='upper left')
    else:
      if type(self.line) == list:
        for l, y in zip( self.line, np.array(self.y).T ):
          l.set_data(self.x, y)
        
      #self.line.set_data(self.x, self.y)
      
    self.ax.set_xlim(t-datetime.timedelta(seconds=self.time_window), t)
    if len(self.y) > 1:
      maximum = np.array(self.y).max()
      minimum = np.array(self.y).min()
      v_padding = (maximum - minimum)*.1    
      self.ax.set_ylim(minimum-v_padding, maximum + v_padding)
    self.fig.autofmt_xdate()    
    self.canvas.draw()