
import tkinter as tk
from tkinter import *
from tkinter import ttk, PhotoImage
import time
import datetime
from tkinter.scrolledtext import ScrolledText

from timePlots import TimePlot

class GUI (tk.Tk):
          def __init__ (self, title, legends):
            super().__init__()
            self.geometry('1153x497')
            self.title('Data Analysis')
            self.resizable(False,False)
            
            self.fundo = PhotoImage(file= 'apagado1.png')
            self.fundolabel = tk.Label(self, image= self.fundo)
            self.fundolabel.place(x=0, y=0)
            
            #FAZER O GRAFICO TEMPERATURA
            self.tp1l = tk.Label(self, text= 'Temperature Analysis',fg="#003152", bg='white', font='Helvetica 10 bold')
            self.tp1l.place(x= 150, y=126)
            
            self.timePlot1 = TimePlot(self, legends, time_window = 40)
            self.timePlot1.canvas.get_tk_widget().place(x= 100, y=145, width=250, height=260)
            
            #FAZER O GRAFICO HUMIDADE
            self.tp2l = tk.Label(self, text= 'Light Analysis',fg="#003152", bg='white', font='Helvetica 10 bold')
            self.tp2l.place(x= 855, y=126)
            
            self.timePlot2 = TimePlot(self, ['LDR'], time_window = 40)
            self.timePlot2.canvas.get_tk_widget().place(x= 775, y=145, width=280, height=260)
            
            #PROGRESS BAR DISTANCIA
            self.pbl = tk.Label(self, text= 'Distance Analysis',fg="#003152", bg='white', font='Helvetica 10 bold')
            self.pbl.place(x= 475, y=140)
            self.pb = ttk.Progressbar(self, orient='horizontal', mode='determinate',maximum = 100, length=280)
            self.pb.place(x= 400, y=170)

            #PROGRESS BAR HUMIDADE
            self.pbh = tk.Label(self, text= 'Humidity Analysis',fg="#003152", bg='white', font='Helvetica 10 bold')
            self.pbh.place(x= 480, y=205)
            self.canvas = tk.Canvas(self, width=150, height=150, bg='white', highlightthickness=0)
            self.canvas.place(x=460, y=235)
            
            self.arc = self.canvas.create_arc(30, 30, 130, 130, start=0, extent=0, style='arc', width=10)
            
            
            #self.info = tk.Button(self, text='More', fg="white", bg='#003152', command=self.open_new_window)
            #self.info.place(x=1070, y=430, width=50)
            
            self.exit = tk.Button(self,command= lambda:self.destroy(), text='Exit', fg="white", bg='#003152')
            self.exit.place(x=1070, y=460, width=50)
            
            self.luz = PhotoImage(file= 'acesas.png')
            self.nluz = PhotoImage(file= 'apagado3.png')

            self.luzlabel = tk.Label(self, image= self.luz, highlightthickness=0, borderwidth=0)
            self.luzlabel.place(x=5, y= 0)
            
            self.label=tk.Label(self, text='Instrumentação e Controlo', font='Helvetica 9 bold', bg='white', fg='#003152')
            self.label.place(x=460, y=380)
            self.autor1=tk.Label(self, text='Filipa Neves, 1211249', font='Helvetica 7 bold', bg='white', fg='#003152')
            self.autor1.place(x=484, y=395)
            self.autor2=tk.Label(self, text='Maria João Mota, 1211044', font='Helvetica 7 bold', bg='white', fg='#003152')
            self.autor2.place(x=478, y=410)
            self.autor2=tk.Label(self, text='2022/2023', font='Helvetica 8 bold', bg='white', fg='#003152')
            self.autor2.place(x=510, y=430)
            
            
           # self.canvas.tk_raise()
            
          def update_progress(self, progress):
            self.canvas.itemconfigure(self.arc, extent=progress/100.*360)
            
            
            #EXTRAS
            
        
    
           
          def update_time(self):
                current_time = datetime.datetime.now().strftime('%H:%M:%S')
                time_label.config(text=current_time)
                time_label.after(1000, update_time)
            
                time_label = tk.Label(self, font='Helvetiva 10', fg='#003152', bg='white')
                time_label.place(x=510, y=420)
            
            
          def hide_label(self):
                gui.luzlabel.pack_forget()
            
              
            
if __name__ == "__main__":
            gui = GUI("Test", ["Legenda"])
            gui.mainloop()
            gui.logfile.flush()
            gui.logfile.close()
            
