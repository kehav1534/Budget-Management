from time import sleep 
import os

"""Shows a running Load ascii"""
def loading():
     asci_list = ['\\' , '|' , '/' , '--' ]
     for n in range(3):
               
          for load_ascii in asci_list :
               print(load_ascii)
               sleep(0.15)
               os.system("cls")

