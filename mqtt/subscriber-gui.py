import tkinter as tk
import pandas as pd
from pandastable import Table, TableModel
from threading import Thread
import time
import datetime
#import mqtt_cloud_rec
#import tkintermqtt

prevframe = pd.read_csv('mqttresult.csv')


class App():
    def __init__(self,interval=5000):
        self.__interval=interval
        self.was_filtered=False
        self.root = createTable() 
        self.update_data(self.check_for_data())
        self.update_clock()
        self.root.master.title('Real Time Ticker - ' + pricingSpec) 
        self.root.mainloop()

    def update_data(self,data_list,snapshot=False):
        if not snapshot and self.root.table.filtered and not self.was_filtered:
            self.was_filtered=True
        if not snapshot and not self.root.table.filtered and self.was_filtered:
            self.was_filtered=False
            self.root.table.model.df=self.root.dataframe
            self.root.table.redraw()
         for el in data_list:
             self.root.append(el,snapshot)
        
    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.update_data(self.check_for_data())
        self.root.after(self.__interval, self.update_clock)

    def check_for_data(self):
        pass
        #This checks for data from your source and returns a list of dictionaries
		
		
class createTable(tk.Frame): 
    def __init__(self, master=None,cpty=False):
        tk.Frame.__init__(self, master)
        #########################################
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid(sticky=tk.NW+tk.SE)
        #########################################
        self.F = tk.Frame(self)
        self.F.grid(row=0, column=0, sticky=tk.NW+tk.SE)

    def append(self,data,snapshot=False):
        self.dataframe.loc[len(self.dataframe)]=data
        self.table.model.df['Theo']=self.dataframe['Theo'].astype('float64')
        self.table.model.df['Edge']=self.dataframe['Edge'].astype('float64')
        self.table.model.df['UnderBid']=self.dataframe['UnderBid'].astype('float64')
        self.table.model.df['UnderAsk']=self.dataframe['UnderAsk'].astype('float64')
        if self.table.filtered:
            self.table.dataframe=self.dataframe.copy()
            self.table.qframe.query()
        else:
            self.table.model.df=self.dataframe
        self.table.redraw()



class TestApp(tk.Frame):
        """Basic test frame for the table"""
        def __init__(self, parent=None):
            self.parent = parent
            tk.Frame.__init__(self)
            self.main = self.master
            self.main.geometry('800x600+200+100')
            self.main.title('Mqtt Result Table')
            f = tk.Frame(self.main)
            f.pack(fill=tk.BOTH,expand=1)
            #df = TableModel.getSampleData(rows=5)
            self.table = pt = Table(f, dataframe=prevframe, showtoolbar=True )
            pt.show()
            self.startbutton = tk.Button(self.main,text='START',command=self.start)
            self.startbutton.pack(side=tk.TOP,fill=tk.X)
            self.stopbutton = tk.Button(self.main,text='STOP',command=self.stop)
            self.stopbutton.pack(side=tk.TOP,fill=tk.X)
      #      self.table.showPlotViewer()            
            return
        

        def update(self):
            
            
            table=self.table              
            #plotter = table.pf
            #opts = plotter.mplopts
            #plotter.setOption('linewidth',3)
            #plotter.setOption('kind','line')
            #opts.widgets['linewidth'].set(3)
            #opts.widgets['kind'].set('line')
            data=[1,2,3,4,5,6,7]
            date_today=str(datetime.date.today())
            time_today=time.strftime("%H:%M:%S")
            datalist=[date_today,time_today]+data
           
            table.model.df = datalist               
            table.multiplecollist=range(0,10)
            table.redraw()
            table.plotSelected()
            time.sleep(.1)
            if self.stop == True:
                return
            return

        def start(self):
            self.stop=False
            t = Thread(target=self.update)
            t.start()            

        def stop(self):
            self.stop = True
            return

app = TestApp()
#launch the app
app.mainloop()

