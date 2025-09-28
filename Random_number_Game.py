import random
import tkinter as tk
d = 0
a = random.randint(0,100)
def random_gameLogic():
 global d
 d+=1
 c=True
 b = int(Enter.get())
 #print("-------------------------")
 #b=input("Enter your number:")
 step.config(text=f"Steps:{d}")
 if a==int(b):
   #print("You are winner")
   result.config(text="You are winner")
   #c=False
 elif int(b)>a:
    #print("Enter small number")
    result.config(text="Enter small number")
 else:
    #print("Enter the big number")
    result.config(text="Enter the big number")


Window = tk.Tk()
Window.title("Random number game")
Window.geometry("500x200")
Window.resizable(True,True)
Enter_N= tk.Label(master=Window,text="Enter the number:",font=("Arial",12))
tital = tk.Label(master=Window,text="Enter the number bettween 0-100",font=("Arial",10))
Enter = tk.Entry(master=Window,width=20)
Button = tk.Button(master=Window,text="Enter",font=("Arial",10),command=random_gameLogic)
result= tk.Label(master=Window,font=("Arial",12))
step = tk.Label(master=Window,font=("Arial",10))
tital.grid(row=0,column=0)
Enter_N.grid(row=6,column=0)
Enter.grid(row=6,column=6,padx=5,pady=25)
Button.grid(row=6,column=10)
result.grid(row=15,column=0)
step.grid(row=18,column=0)
Window.mainloop()