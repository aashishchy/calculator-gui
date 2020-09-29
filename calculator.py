import tkinter as tk


def click(number):
    global operator
    operator= operator + str(number)
    variable.set(operator)

def clearbtn():
    global operator
    operator=''
    variable.set(operator) 
def equal():
    global operator
    operator = str(eval(operator))
    variable.set(operator)

operator=''
root =tk.Tk()
root.title('calculator')
variable=tk.StringVar()
display=tk.Entry(root,font=('courier',20),textvariable=variable,bd=30,justify='left')
display.grid(columnspan=6)

btn9=tk.Button(root,text=9,font=('courier',20),bd=9,padx=3,pady=5,command=lambda:click(9))
btn9.grid(row=1,column=0)
btn8=tk.Button(root,text=8,font=('courier',20),bd=9,padx=3,pady=5,command=lambda:click(8))
btn8.grid(row=1,column=1)
btn7=tk.Button(root,text=7,font=('courier',20),bd=9,padx=3,pady=5,command=lambda:click(7))
btn7.grid(row=1,column=2)
btnaddition=tk.Button(root,text='+',font=('courier',20),bd=9,padx=3,pady=5,command=lambda:click('+'))
btnaddition.grid(row=1,column=3)

btn6=tk.Button(root,text=6,font=('courier',20),bd=9,padx=3,pady=5,command=lambda:click(6))
btn6.grid(row=2,column=0)
btn5=tk.Button(root,text=5,font=('courier',20),bd=9,padx=3,pady=5,command=lambda:click(5))
btn5.grid(row=2,column=1)
btn4=tk.Button(root,text=4,font=('courier',20),bd=9,padx=3,pady=5,command=lambda:click(4))
btn4.grid(row=2,column=2)
btnsub=tk.Button(root,text='-',font=('courier',20),bd=9,padx=3,pady=5,command=lambda:click('-'))
btnsub.grid(row=2,column=3)

btn3=tk.Button(root,text=3,font=('courier',20),bd=9,padx=3,pady=5, command=lambda:click(3))
btn3.grid(row=3,column=0)
btn2=tk.Button(root,text=2,font=('courier',20),bd=9,padx=3,pady=5,command=lambda:click(2) )
btn2.grid(row=3,column=1)
btn1=tk.Button(root,text=1,font=('courier',20),bd=9,padx=3,pady=5, command=lambda:click(1))
btn1.grid(row=3,column=2)
btnmulti=tk.Button(root,text='*',font=('courier',20),bd=9,padx=3,pady=5, command=lambda:click('*'))
btnmulti.grid(row=3,column=3)

btnclear=tk.Button(root,text='C',font=('courier',20),bd=9,padx=3,pady=5,command=lambda:clearbtn())
btnclear.grid(row=4,column=0)
btn0=tk.Button(root,text=0,font=('courier',20),bd=9,padx=3,pady=5,command=lambda:click(0))
btn0.grid(row=4,column=1)
btnpoint=tk.Button(root,text='.',font=('courier',20),bd=9,padx=3,pady=5,command=lambda:click('.'))
btnpoint.grid(row=4,column=2)
btndiv=tk.Button(root,text='/',font=('courier',20),bd=9,padx=3,pady=5,command=lambda:click('/') )
btndiv.grid(row=4,column=3)

btnequal=tk.Button(root,text='=',font=('courier',20,'bold'),bd=9,padx=100,command=lambda:equal(),)
btnequal.grid(row=5,columnspan=6)



root.mainloop()
