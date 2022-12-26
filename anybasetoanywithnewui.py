from tkinter import*
from tkinter import ttk
from tkinter import font
from turtle import color
from webbrowser import BackgroundBrowser

def fromin(num):
    e2.configure(state=NORMAL)
    global inp
    inp = num
    e2.delete(0 , END)
    e2.insert(0 ,str(inp))
    e2.configure(state=DISABLED)

def fromout(num1):
    e3.configure(state=NORMAL)
    global x
    x = num1
    e3.delete(0 , END)
    e3.insert(0 ,str(x))
    e3.configure(state=DISABLED)


def convert():
    
    i_num = str(e1.get())

    num = []

    for i in i_num:
        num.append(i)
    num.reverse()

    total = 0
    A = 0
    if inp == 2:
        for i in num:
            total += int(i)*(2**A)
            A += 1
        d_num = total

    if inp == 8:
        for i in num:
            total += int(i)*(8**A)
            A += 1
        d_num = total

    sixteenletters = [10,11,12,13,14,15]
    if inp == 16:
        for i in num:
            if str(i).upper() == "A":
                num[num.index(i)] = 10
            if str(i).upper() == "B":
                num[num.index(i)] = 11
            if str(i).upper() == "C":
                num[num.index(i)] = 12
            if str(i).upper() == "D":
                num[num.index(i)] = 13
            if str(i).upper() == "E":
                num[num.index(i)] = 14
            if str(i).upper() == "F":
                num[num.index(i)] = 15
            
        for i in num:
            total += int(i)*(16**A)
            A += 1
        d_num = total
        
    if inp == 10:
        d_num = int(i_num)


    if x == 10:
        print(d_num)
        l3.configure(text=(d_num))
    else:
        out_num  = []
        while d_num != 0:
            out_num.append(d_num % x)
            d_num //= x

        out_num.reverse()
        sixteenletters = ['A','B','C','D','E','F']
        B = 0
        if x == 16:
            for i in out_num:
                if i == 10 or i == 11 or i == 12 or i == 13 or i == 14 or i == 15:
                    out_num[out_num.index(i)] = sixteenletters[i-10]

        ans = "".join(str(d)for d in out_num)
        print(ans)
        l3.configure(text=ans)
        
    
    



root  = Tk()
root.title("Number Convertion")

style  = ttk.Style()

e1 = ttk.Entry(font=('calibri' , 20 , 'italic')  , width=25)

bconvert = ttk.Button(text="convert" , padding=(120,20),style="big.TButton",command=convert )

b10 = ttk.Button(text="10"   , padding=(5,20),style="big.TButton",command=lambda: fromin(10))
b16 = ttk.Button(text="16"   , padding=(5,20),style="big.TButton",command=lambda: fromin(16))
b8 = ttk.Button(text="8"   , padding=(5,20),style="big.TButton",command=lambda: fromin(8))
b2 = ttk.Button(text="2"   , padding=(5,20),style="big.TButton",command=lambda: fromin(2) )

l1 = Label(text="> CONVERT THIS  TO >" ,font=('calibri', 15 , 'bold' ) )

e2 = ttk.Entry(font=('calibri' , 30 , 'bold')  , width=3 )

e3 = ttk.Entry(font=('calibri' , 30 , 'bold')  , width=3 )

b10_2 = ttk.Button(text="10" , padding=(5,20),style="big.TButton",command=lambda: fromout(10))
b16_2 = ttk.Button(text="16" , padding=(5,20),style="big.TButton",command=lambda: fromout(16))
b8_2 = ttk.Button(text="8"   , padding=(5,20),style="big.TButton",command=lambda: fromout(8) )
b2_2 = ttk.Button(text="2"   , padding=(5,20),style="big.TButton",command=lambda: fromout(2) )

style.configure('big.TButton', font=(None, 10))


l2 = Label(text="(  Answer  Here  )" )

e1.grid(row=0 , column=0 , columnspan=6)

bconvert.grid(row=7 , column=0 , columnspan=5 )

b10.grid(row=2 , column=0)
b16.grid(row=2 , column=1)
b8.grid(row=2 , column=2)
b2.grid(row=2 , column=3)

b10_2.grid(row=4 , column=0)
b16_2.grid(row=4 , column=1)
b8_2.grid(row=4 , column=2)
b2_2.grid(row=4 , column=3)


e2.grid(row=3 , column=0 )
e2.insert(0,"🔢")
e2.configure(state=DISABLED)
l1.grid(row=3 , column=1 , columnspan=2)
e3.grid(row=3 , column=3 )
e3.insert(0,"🔢")
e3.configure(state=DISABLED)

l2.grid(row=5 , column=0 , columnspan=5)

global l3
l3 = Label(text=("answer is: "), font=('calibri'  , 20 , 'bold') )
l3.grid(row=6 , column=0 , columnspan=6 )

mainloop()
