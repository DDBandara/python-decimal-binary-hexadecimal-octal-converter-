from tkinter import*

def fromin(num):
    global inp
    inp = num
    e2.delete(0 , END)
    e2.insert(0 ,str(inp))

def fromout(num1):
    global x
    x = num1
    e3.delete(0 , END)
    e3.insert(0 ,str(x))


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

root.configure(bg='#2b2c2c')

e1 = Entry(font=('calibri' , 15 , 'italic')  , width=33  , borderwidth=2)

bconvert = Button(text="convert" ,font=('calibri', 15 ) , padx=2 , pady=72 , command=convert , borderwidth=2 , bg='#363636' , fg='white')

b10 = Button(text="10" , font=('calibri' , 15 , 'bold') , borderwidth=2 , padx=10 , pady=10 ,bg='#202121',fg='white', command=lambda: fromin(10))
b16 = Button(text="16" , font=('calibri' , 15 , 'bold') , borderwidth=2 , padx=10 , pady=10 ,bg='#202121',fg='white', command=lambda: fromin(16))
b8 = Button(text="8" , font=('calibri' , 15 , 'bold') , borderwidth=2 , padx=13 , pady=10 ,bg='#202121',fg='white', command=lambda: fromin(8))
b2 = Button(text="2" , font=('calibri' , 15 , 'bold') , borderwidth=2 , padx=13 , pady=10 ,bg='#202121',fg='white', command=lambda: fromin(2))
b = Button(text=" ;-)" ,font=('calibri', 15 ) ,borderwidth=2 ,  padx=10 , pady=10 , bg='#242b39' , fg='white')

l1 = Label(text="TO" ,font=('calibri', 12 ) , bg='#2b2c2c',fg='white')

e2 = Entry(font=('calibri' , 30 , 'bold')  , width=2  , borderwidth=2)

e3 = Entry(font=('calibri' , 30 , 'bold')  , width=2 ,  borderwidth=2)

b10_2 = Button(text="10" , font=('calibri' , 15 , 'bold') , borderwidth=2 , padx=10 , pady=10 ,bg='#202121',fg='white', command=lambda: fromout(10))
b16_2 = Button(text="16" , font=('calibri' , 15 , 'bold') , borderwidth=2 , padx=10 , pady=10 ,bg='#202121',fg='white', command=lambda: fromout(16))
b8_2 = Button(text="8" , font=('calibri' , 15 , 'bold') , borderwidth=2 , padx=13 , pady=10 ,bg='#202121',fg='white', command=lambda: fromout(8))
b2_2 = Button(text="2" , font=('calibri' , 15 , 'bold') , borderwidth=2 , padx=13 , pady=10 ,bg='#202121',fg='white', command=lambda: fromout(2))
b1 = Button(text=":-D" ,font=('calibri', 15 ) , padx=10 , pady=10 , borderwidth=2 , bg='#242b39' , fg='white')

l2 = Label(text="(  Answer  Here  )" ,font=('calibri', 12 ) , bg='#2b2c2c',fg='white')

e1.grid(row=0 , column=0 , columnspan=6)

bconvert.grid(row=2 , column=5 , rowspan=3)

b10.grid(row=2 , column=0)
b16.grid(row=2 , column=1)
b8.grid(row=2 , column=2)
b2.grid(row=2 , column=3)

b.grid(row=2 , column=4)

b10_2.grid(row=4 , column=0)
b16_2.grid(row=4 , column=1)
b8_2.grid(row=4 , column=2)
b2_2.grid(row=4 , column=3)

b1.grid(row=4 , column=4)

e2.grid(row=3 , column=0 , columnspan=2)
l1.grid(row=3 , column=2)
e3.grid(row=3 , column=3 , columnspan=2)

l2.grid(row=5 , column=0 , columnspan=5)

global l3
l3 = Label(text=("answer is: ") , font=('calibri' , 20 , 'italic') , bg='#2b2c2c',fg='white')
l3.grid(row=6 , column=0 , columnspan=6)

mainloop()