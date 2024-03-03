# 
#! Calculator Application
#
import tkinter as tk

root=tk.Tk()
root.geometry("420x480")
root.title("Calculator Application")

display=tk.Label(root,font=("Consolas",15),height=2,width=3,bg="white")
display.pack(fill="x",pady=10)
#
frame=tk.Frame(root)
frame.pack()
#
btn7=tk.Button(frame,text="7",font=("Arial",30))
btn7.grid(row=0,column=0,padx=20)
#
btn8=tk.Button(frame,text="8",font=("Arial",30),)
btn8.grid(row=0,column=1,padx=20)
#
btn9=tk.Button(frame,text="9",font=("Arial",30))
btn9.grid(row=0,column=2,padx=20)
#
# btn_divide=tk.Button(frame,text="/")
# btn_divide.pack()
# #
# btn4=tk.Button(frame,text="4")
# btn4.pack()
# #
# btn5=tk.Button(frame,text="5")
# btn5.pack()
# #
# btn6=tk.Button(frame,text="6")
# btn6.pack()
# #
# btn_multiply=tk.Button(frame,text="X")
# btn_multiply.pack()
# #
# btn1=tk.Button(frame,text="1")
# btn1.pack()
# #
# btn2=tk.Button(frame,text="2")
# btn2.pack()
# #
# btn3=tk.Button(frame,text="3")
# btn3.pack()
#
# btn9=tk.Button(frame,text="3")
# btn9.pack()
# #
# btn9=tk.Button(frame,text="3")
# btn9.pack()
# #
# btn9=tk.Button(frame,text="3")
# btn9.pack()
#
root.mainloop()