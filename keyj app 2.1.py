import sys
import time
from tkinter import*
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Button

def bA_click():
     label.config(text = 'password вернитесь в консоль')
     
def bl_click():
     label.config(text = 'ваш код 5467 вернитесь в консоль')

print("ведите start что бы запустить")
x = input("")
while x != "start":
      print("please try again laeter")
      x =input("")
print('loading.', end="")
print('\r', end='')
time.sleep(1)
print('loading..', end="")
print('\r', end='')
time.sleep(0.50)
print('loading...', end="")
print('\r', end='')
time.sleep(0.50)
print('loading:  :', end="")
print('\r', end='')
time.sleep(0.50)
print('loading/ /', end="")
print('\r', end='')
time.sleep(0.50)
print('loading\/:', end="")
print('\r', end='')
time.sleep(0.50)
print('loading ', end="")
print('\r', end='')
print("войти? YES or NO  ")
x = input("")
while x != "YES":
      print("error")
      x = input("")
    
import tkinter

root = Tk()
root.title('key.j app')
root.geometry('500x500')

label = Label(root, text = 'hello user', font = 'arial 18', width = '50')
label.place(x = 60, y = 100)

label.pack()

bA = Button(root, text = "im keyj", width = 20, command = bA_click)
bA.place(x = 130, y = 120)

bl = Button(root, text = 'im guest', width = 20, command = bl_click)
bl.place(x = 280, y = 120)

root.mainloop

print('нажмите enter')
input('')
print("введите код или пароль")
c = 1
a = int(input())
b = int(5467)
while a != b:
    print("access denied")
    print("special thanks for:Alex and Ivan") 
    print("ctrl+d for exit")
if a == b:
   print("доступ  разрешон")
   print("введите имя")
   name = input("")
   print("what are you nead",name)
   print("google:")
   x = input("")
   if x == "keyj":
     print("wiki: keyj its youtouber and musicman he make this program")
     print("special thanks for:Alex and Ivan")
   while x != "keyj":
       print("one moment")
       print('loading.', end="")
       print('\r', end='')
       time.sleep(1)
       print('loading..', end="")
       print('\r', end='')
       time.sleep(0.50)
       print('loading...', end="")
       print('\r', end='')
       time.sleep(0.50)
       print('loading:  :', end="")
       print('\r', end='')
       time.sleep(0.50)
       print('loading/ /', end="")
       print('\r', end='')
       time.sleep(0.50)
       print('loading\/:', end="")
       print('\r', end='')
       time.sleep(0.50)
       print('loading ', end="")
       print('\r', end='')
       print("мы обработаем ваш запрос")
       print('\\;\\/:', end="")
       print('\r', end='')
       print("мы обработаем ваш запрос спасибо что вы с нами")
       x = input("")
if x == "keyj":
    print("wiki: keyj its youtouber and musicman he make this program")       
print("its all")
print("special thanks for:Alex and Ivan")
if a != b:
   print("access denied")
   print("special thanks for:Alex and Ivan") 
   print("ctrl+d for exit")
   root.mainloop()
root.mainloop() 
time.sleep(2)
sys.exit(1)


 





