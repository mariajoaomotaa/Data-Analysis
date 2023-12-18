
import threading
import time
import datetime

from interface import GUI

import serial

windowIsOpen = True

mean_10 = []
temperature = []
h= []
lux= []
t = []
ldr_value = []

def update():   
  while windowIsOpen:
    line = ser.readline().decode().strip() #o decode transforma os bytes em strings, o strip tira espaços e carateres de controlo
    print(line)
    values = line.split(",") #cria uma lista de valores
    print(values)
    
    if len(values) == 5: #para evitar bugs
    
        try:
            values = [float (i) for i in values] #transforma os valores em floats
            #GRAFICO TEMP
            gui.timePlot1.update([values[0],values[1],values[4]])   
            
            #GRAFICO LUX
            gui.timePlot2.update([values[3]]) 
            
            #PROGRESS BAR
            gui.pb['value']=[values[2]]
            
            
            
            if gui.pb['value'] <= 10:
                gui.pbl['fg'] = 'red'
                print ('Distância curta!')
                gui.luzlabel.config(image=gui.nluz)
                
               
                   
            else:
                gui.pbl['fg'] = '#003152'
                gui.luzlabel.config(image=gui.luz)
                
                
            #PROGRESS BAR HUMIDADE
            gui.update_progress(values[3])
            
            
            gui.currentValue.config(text= "T = {:.5} M = {:.5} S = {:.5} D ={:.5} L={:.5} ".format(values[0], values[1], values[2], values[3], values[4]))
               
        except:
            pass
        
      
    time.sleep(.1)
    
    
if __name__ == "__main__":
    gui = GUI( "OOP example 2", ["TMP36", "Média", "DHT11"])
    
    ser=serial.Serial("COM7" , 9600)
    
    updateThread = threading.Thread(target=update)
    updateThread.start()
    
    gui.mainloop()
    windowIsOpen = False
    ser.close()