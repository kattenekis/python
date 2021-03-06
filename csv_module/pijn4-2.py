#! /usr/bin/env python3
#  -*- coding:utf-8 -*-

from tkinter import * # module om gui te maken
import csv # module om csv files te kunnen handelen
# from tkinter import ttk
# import datetime
import time
import tkinter as tk
import pandas as pd # voor het inlezen van de csv file
from pandas import DataFrame
from pandas.computation import align

t =  time.strftime("%x  %X") # gemakkelijkere manier


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.inlezen()  #functie inlezen en aanroepen
        self.output()

    def inlezen(self):
        df = pd.read_csv('pijn.csv', names=['Tijd', 'Pijn']) #names= om namen aan de colomen toe te voegen
        print(df)  #gewoon om een uitprint in terminal te zien
        lezen1 = Label(self, text='De laatste 10 ingevoerde waarden zijn:')  #laatste 10st ingevoerd tonen
        lezen1.grid(row=3, column=0, padx=5, pady=3)  #op deze plaats laten verschijnen
        lezen = Label(self, text=df.tail(10))  # laatste 10st ingevoerd tonen
        lezen.grid(row=4, column=0, padx=5, pady=3)  # op deze plaats laten verschijnen

    def output(self):
        # tekst en textveld datum
        datum = Label(self, text= str(t))
        datum.grid(row=1, column=0, padx=5, pady=3)

        pijn = Label(self, text='pijn-ervaring:')
        pijn.grid(row=1, column=2, padx=5, pady=3)
        self.e1 = Entry(self, width=50)
        self.e1.grid(row=1, column=3, padx=5, pady=3)
        self.e1.focus_set() # deze regel is voor de cursor te plaatsen
        self.e1.bind("<Return>", self.writeToFile) # laat Enter key een functie uit te voeren
        # aanmaak van button sla op

        self.b = Button(root, text='Sla op of druk Enter', command=self.writeToFile)
        self.b.grid(row=0, column=4, padx=5, pady=3)

        self.b1 = Button(root, text='Nieuwe invoer ',font = ('times', 14, 'bold'), bg ='#dddddd', command=self.output)
        self.b1.grid(row=2, column=0, columnspan=3, ipady=4, padx=5,pady=5)

        self.b2 = Button(root, text='AFSLUITEN ',font = ('times', 12, 'bold'),bg = '#dddddd',  command=self.Afsluiten)
        self.b2.grid(row=2, column=1 ,columnspan=3,sticky=tk.W + tk.E, ipady=10, padx=5,pady=5)

        # schrijven naar csv file

    def writeToFile(self, k=None):
        t = time.strftime("%x  %X")
        with open('pijn.csv', 'a') as f: # de 'a' staat voor append (toevoegen)
                w=csv.writer(f, delimiter=',')
                w.writerow([t, self.e1.get()])

    def Afsluiten(self):
        self.destroy()
        exit()


if __name__ == "__main__":
        root=Tk()
        root.title('Pijn Logger') # dit is de titel
        root.geometry('1000x300') # groote van het kader
        app=App(master=root) # het aanroepen van de class App
        app.mainloop() # runnen van de applicatie
        root.mainloop() # loop programma
