from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
root=Tk()
root.title("Stock Scraper")
root.geometry('400x400')
root.anchor('center')
topFrame=Frame(root)
topFrame.pack(pady=20,)
bottmFrame=Frame(root)
bottmFrame.pack(side='bottom',fill=Y, pady=30)
Label(topFrame, text='Company Name:').grid(column=0,row=0, sticky=E, pady=15) 
Label(topFrame, text='Profit period:').grid(column=0,row=1, sticky=E, pady=5) 

combo= Combobox(topFrame)
#combo.current(1)
combo.grid(column=1,row=0, pady=15)
#combo.get()


chk_3m = BooleanVar()
chk_3months = Checkbutton(topFrame, text='3 months', var=chk_3m) 
chk_3months.grid(column=1, row=1,sticky=W, pady=5)
chk_6m = BooleanVar()
chk_6months = Checkbutton(topFrame, text='6 months', var=chk_6m) 
chk_6months.grid(column=1, row=2,sticky=W, pady=5)
chk_1y = BooleanVar()
chk_1year = Checkbutton(topFrame, text='1 year', var=chk_1y) 
chk_1year.grid(column=1, row=3,sticky=W, pady=5)

rad_Gainer = Radiobutton(topFrame,text='Top Gainer')
rad_Gainer.grid(column=1,row=4,sticky=W, pady=5)
rad_Loser = Radiobutton(topFrame,text='Top Gainer')
rad_Loser.grid(column=2,row=4,sticky=W, pady=5)

txt = Text(bottmFrame,width=40,height=50)
 
txt.grid(row=5,columnspan=5)

root.mainloop() 
