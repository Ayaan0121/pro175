# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 11:04:44 2023

@author: riddh
"""
from tkinter import *
from PIL import ImageTk , Image
from tkinter import ttk
import matplotlib.pyplot as plt
import psutil as ps
root=Tk()
root.title("Task Manager")
root.config(bg="indianred")
lbl1=Label(root , text="Task Manager" , font=("monospace" , 20 , "bold" , "italic") , fg="blue" ,bg="indianred")
lbl1.place(relx=0.5 , rely=0.1 , anchor=CENTER)
lbl2=Label(root , text="Applications" , font=("monospace" , 15 , "bold" , "italic") , fg="orange",bg="indianred")
lbl2.place(relx=0.2 , rely=0.2 , anchor=CENTER)
lbl2=Label(root , text="CPU Usage" , font=("monospace" , 15 , "bold" , "italic") , fg="red",bg="indianred")
lbl2.place(relx=0.8 , rely=0.2 , anchor=CENTER)
#label Apps
lblA1=Label(root  , font=("monospace" , 15 , "bold" , "italic") , fg="green",bg="indianred")
lblA1.place(relx=0.2 , rely=0.4 , anchor=CENTER)
lblA2=Label(root  , font=("monospace" , 15 , "bold" , "italic") , fg="purple",bg="indianred")
lblA2.place(relx=0.2 , rely=0.5 , anchor=CENTER)
lblA3=Label(root  , font=("monospace" , 15 , "bold" , "italic") , fg="yellow",bg="indianred")
lblA3.place(relx=0.2 , rely=0.6 , anchor=CENTER)
lblA4=Label(root  , font=("monospace" , 15 , "bold" , "italic") , fg="pink",bg="indianred")
lblA4.place(relx=0.2 , rely=0.7 , anchor=CENTER)
#label Cpu
lblP1=Label(root  , font=("monospace" , 15 , "bold" , "italic") , fg="green",bg="indianred")
lblP1.place(relx=0.8 , rely=0.4 , anchor=CENTER)
lblP2=Label(root  , font=("monospace" , 15 , "bold" , "italic") , fg="purple",bg="indianred")
lblP2.place(relx=0.8 , rely=0.5 , anchor=CENTER)
lblP3=Label(root  , font=("monospace" , 15 , "bold" , "italic") , fg="yellow",bg="indianred")
lblP3.place(relx=0.8 , rely=0.6 , anchor=CENTER)
lblP4=Label(root  , font=("monospace" , 15 , "bold" , "italic") , fg="pink",bg="indianred")
lblP4.place(relx=0.8 , rely=0.7 , anchor=CENTER)
root.geometry("1000x550")
pList=[]
tpList=[]
c=0
for i in ps.process_iter():
    c+=1
    if c <= 6:
        name1=i.name()
        cu=ps.cpu_percent()
        print("Process Name:" , str(name1) , "\n CPU Usage:" , str(cu))
        pList.append(name1)
        tpList.append(cu)
plt.figure(figsize=(15,7))
plt.xlabel("Applications names →" )
plt.xlabel("CPU Usage →" )
plt.bar(pList, tpList,width=0.6 , color=("red" , "blue" , "orange" , "yellow" , "green" ,"purple"))
plt.show()

lblA1["text"]=str(pList[0])
lblA2["text"]=str(pList[1])
lblA3["text"]=str(pList[2])
lblA4["text"]=str(pList[3])
lblP1["text"]=str(tpList[0]),"%"
lblP2["text"]=str(tpList[1]),"%"
lblP3["text"]=str(tpList[2]),"%"
lblP4["text"]=str(tpList[3]),"%"
def lol():
 pList=[]
 tpList=[]
 c=0
 for i in ps.process_iter():
     c+=1
     if c <= 6:
         name1=i.name()
         cu=ps.cpu_percent()
         print("Process Name:" , str(name1) , "\n CPU Usage:" , str(cu))
         pList.append(name1)
         tpList.append(cu)
 plt.figure(figsize=(15,7))
 plt.xlabel("Applications names →" )
 plt.xlabel("CPU Usage →" )
 plt.bar(pList, tpList,width=0.6 , color=("red" , "blue" , "orange" , "yellow" , "green" ,"purple"))
 plt.show()

 lblA1["text"]=str(pList[0])
 lblA2["text"]=str(pList[1])
 lblA3["text"]=str(pList[2])
 lblA4["text"]=str(pList[3])
 lblP1["text"]=str(tpList[0]),"%"
 lblP2["text"]=str(tpList[1]),"%"
 lblP3["text"]=str(tpList[2]),"%"
 lblP4["text"]=str(tpList[3]),"%"
btn=Button(root , text="Refresh Results" , bg="azure" , command=lol)
btn.place(relx=0.5 , rely=0.9 , anchor=CENTER)
root.mainloop()