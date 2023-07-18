#Importing all the necessary libraries to form the alarm clock:
from tkinter import *
import datetime
import time
import winsound

#Defining functions
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

#Creating overall layout
clock = Tk()
clock.title("Alarm Clock")
clock.geometry("500x200")
time_format=Label(clock, text= "Enter time in 24 hour format!",font="Arial").place(x=200,y=120)
name_format=Label(clock, text= "Sonam's alarm clock",fg="navy blue",font=("Arial",25,"bold")).place(x=85,y=150)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 200)
setYourAlarm = Label(clock,text = "Set time here",relief = "solid",font=("Helevetica",15,"bold")).place(x=50, y=30)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 10).place(x=200,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 10).place(x=250,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 10).place(x=300,y=30)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",width = 15,command = actual_time).place(x =200,y=70)

clock.mainloop()
#Execution of the window.