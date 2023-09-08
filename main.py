import numpy as np
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sympy import sympify, sin, cos, sqrt, exp
from sympy import Symbol,diff,lambdify
from sympy.solvers import solve
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
import statistics
global expr
global f
x = Symbol('x')
expr = " "
def close_window():
    print("Τερματισμος")
    root.destroy()
# Δημιουργία βασικού παραθύρου
root = Tk()
root.title("Παράθυρο Tkinter")
new_text=""
def new_function():
    root7=Tk()
    text=Entry(root7,font=("Arial black",12))
    text.grid(padx=5,pady=10)
    text.pack()

    def sss():
        global expr
        global f
        new_text=sympify(text.get())
        expr=new_text
        f = lambdify(x, expr)
        print("Η καινουργια συναρτηση επιλογης ειναι η f(x)= "+str(expr))


    button = Button(root7, text="εκτελεση", command=sss)


    button.pack()
def new_root():
    root2 = Tk()
    a1 = 0
    a2 = 0
    label1 = Label(root2, text="Επιλογη οριων ολοκληρωσης")
    a = Entry(root2, font=("Arial black", 12))
    b = Entry(root2, font=("Arial black", 12))
    labela=Label(root2, text="Κατω οριο ολοκληρωσης a:")
    labelb=Label(root2, text="Πανω οριο ολοκληρωσης b:")
    label1.grid(column=1,row=0)
    a.grid(column=2,row=1)
    b.grid(column=2,row=2)
    labela.grid(column=0,row=1)
    labelb.grid(column=0,row=2)
    def value():
        a1 = 0
        a2 = 0
        try:
            a1 = float(a.get())
            a2 = float(b.get())
        except ValueError:
            print("δειτε αν εχετε ορισει σωστα τηγ συναρτηση και Προσεξε τις εκφρασεις που βαζεις στα κενα δεχεται ακεραιους και δεκαδικους")
        sum = 0
        step = (a2 - a1 )/ 10000
        for i in range(0 ,10000):
            i=float(i)

            sum = sum + expr.subs('x',a1+(i + 0.5)*step)*step
        sum = round(sum, 3)
        print("H ολοκληρωση της f(x) απο "+str(a1)+" εως το "+str(a2)+" ισουται με "+str(sum))

    button2 = Button(root2, text="εκτελεση", command=value)
    button2.grid(column=2,row=3)
def derivative_root():
    root3=Tk()
    label=Label(root3, text="Επιλογη σημειου παραγωγισης")
    a = Entry(root3, font=("Arial black", 12))

    label.pack()
    a.pack()
    def value():
        try:
            a1=float(a.get())
        except ValueError:
            print("Δεν εχεις ορισει συναρτηση η πρεπει να προσεξεις τα κενα που συμπληρωνεις")
        total=diff(expr,'x')
        print("Η πρωτη παραγωγος της f(x) στο "+str(a1)+" ισουται με: "+str(total.subs('x',a1)))
    button2 = Button(root3, text="εκτελεση", command=value)
    button2.pack()
#επιλυση εξισωσης
def function():

    print("Oι λυσεις της εξισωσης f(x)=0 ειναι :")
    print(solve(expr,x))
#υπολογισμος συναρτησης σε σημειο
def calculate():
    root4 = Tk()
    label = Label(root4, text="Επιλογη σημειου υπολογισμου")
    a = Entry(root4, font=("Arial black", 12))

    label.pack()
    a.pack()
    def value():
        try:
            a1=float(a.get())
        except ValueError:
            print("ok")
        print("Το αποτελεσμα υπολογισμου ειναι f("+str(a1)+")="+str(expr.subs('x',a1)))


    button2 = Button(root4, text="εκτελεση", command=value)
    button2.pack()
def graph():
    root5=Tk()
    label=Label(root5,text="Επιλογη διαστηματος απεικονισης")
    a=Entry(root5,font=("Arial black",12))
    b=Entry(root5,font=("Arial black",12))
    labela=Label(root5, text="Κατω οριο απεικονισης στον αξονα x a:")
    labelb=Label(root5, text="Πανω οριο απεικονισης στον αξονα x b:")
    label.grid(column=1,row=0)
    a.grid(column=2,row=1)
    b.grid(column=2,row=2)
    labela.grid(column=0,row=1)
    labelb.grid(column=0,row=2)
    def value():
        try:
            a1=float(a.get())
            a2=float(b.get())
        except ValueError:
            print("δες αν ορισες σωστα την συναρτηση η εβαλες ορια που ειναι ακεραιοι η δεκαδικοι")
        t=np.arange(a1,a2,0.01)
        if a1<0:
            i=a1
      #  elif a1>0:
      #      i=a1+0.01
        fun=[]
        for t2 in t:
            fun.append(f(t2))
        plt.plot(t,fun)
        plt.grid(True)
        plt.ylabel('f(t)')
        plt.xlabel('t')

        plt.show()



    button2 = Button(root5, text="εκτελεση", command=value)
    button2.grid(column=2,row=3)
    #plt.savefig('Figure_1.png',dpi=200)
    #plt.savefig('foo.pdf')
def system1():
    root6=Tk()
    label=Label(root6,text="Eισαγωγη στοιχειων πινακα").grid(column=0,row=0)
    en=[]

    A=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(0,9):
        if i<3:
            a=Entry(root6,font=("Arial black",12))
            a.grid(column=i+1,row=1)

            en.append(a)
        elif i>=3 and i<6:
            a = Entry(root6, font=("Arial black", 12))
            a.grid(column=i + 1-3, row=2)

            en.append(a)
        elif i>=6 and i<9:
            a = Entry(root6, font=("Arial black", 12))
            a.grid(column=i + 1 - 6, row=3)

            en.append(a)
    label1=Label(root6,text="Εισαγωγη αριστερου μελους συστηματος")
    label1.grid(column=6,row=0)
    en2=[]
    for i in range(0,3):
        a = Entry(root6, font=("Arial black", 12))
        a.grid(column=14, row=i+1)
        en2.append(a)
    b=np.matrix(np.zeros((3,1)))
    def sumbit():
        k=0
        for i in range(0, 3):
            for j in range(0, 3):

               try:
                   A[i][j]=float(en[k].get())
               except ValueError:
                   print("ok")
               k=k+1
        for i in range(0,3):
            try:
                b[i]=float(en2[i].get())
            except ValueError:
                print("ok")
        #print(A)
        #print(b)
        print("Λυση εξισωσης")
        x=np.linalg.inv(A)*b
        print("(x,y,z)="+str(x))
        #print(x)
    button=Button(root6,text="εκτελεση",command=sumbit).grid(column=5,row=5)
def system2():
    root6 = Tk()
    label = Label(root6, text="Eισαγωγη στοιχειων πινακα").grid(column=0, row=0)
    en = []

    A = [[0, 0], [0, 0]]
    for i in range(0, 4):
        if i < 2:
            a = Entry(root6, font=("Arial black", 12))
            a.grid(column=i + 1, row=1)

            en.append(a)
        elif i >=2 and i <4:
            a = Entry(root6, font=("Arial black", 12))
            a.grid(column=i + 1 -2, row=2)

            en.append(a)

    label1 = Label(root6, text="Εισαγωγη αριστερου μελους συστηματος")
    label1.grid(column=6, row=0)
    en2 = []
    for i in range(0, 2):
        a = Entry(root6, font=("Arial black", 12))
        a.grid(column=10, row=i + 1)
        en2.append(a)
    b = np.matrix(np.zeros((2, 1)))

    def sumbit():
        k = 0
        for i in range(0, 2):
            for j in range(0, 2):

                try:
                    A[i][j] = float(en[k].get())
                except ValueError:
                    print("ok")
                k = k + 1
        for i in range(0, 2):
            try:
                b[i] = float(en2[i].get())
            except ValueError:
                print("ok")
        # print(A)
        # print(b)
        print("Λυση εξισωσης")
        x = np.linalg.inv(A) * b
        print("(x,y)="+str(x))
        #print(x)

    button = Button(root6, text="εκτελεση", command=sumbit).grid(column=5, row=5)
def inequation():
    new_root=Tk()
    roots=[]
    label=Label(new_root,text="Επιλυση ανισωσης πολυωνυμου")
    label.grid(column=0,row=0)
    roots=solve(expr,x)
    values=[]
    for root1 in roots:
        if "I" not in str(root1):
            value = root1
            values.append(value)
    #print(roots)
    #print(values)
    k=0
    labels=[]
    values.sort()
    for value in values:
        a=Label(new_root,text=str(value))

        a.grid(column=k+2,row=2)
        k = k + 3
        labels.append(a)
    j=1
    for i in range(0,len(values)):

        if expr.subs('x',values[i]-0.01)>0:
            label4=Label(new_root,text="+")
            label4.grid(column=j,row=3)
            if i==len(values)-1:
                if expr.subs('x',values[i]+0.01) > 0:
                    label3=Label(new_root,text="+")
                    label3.grid(column=j+2 , row=3)
                elif expr.subs('x',values[i]+0.01) < 0:
                    label3 = Label(new_root, text="-")
                    label3.grid(column=j +2, row=3)

        elif expr.subs('x',values[i]-0.01) <0:
            label4 = Label(new_root, text="-")
            label4.grid(column=j , row=3)
            if i==len(values)-1:
                if  expr.subs('x',values[i]+0.01)> 0:
                    label3 = Label(new_root, text="+")
                    label3.grid(column=j +2, row=3)
                elif  expr.subs('x',values[i]+0.01)< 0:
                    label3 = Label(new_root, text="-")
                    label3.grid(column=j +2, row=3)
        j=j+3
def distribution():
    new_root=Tk()
    label2=Label(new_root,text="Επιλογη κατανομης:")
    label2.grid(column=0,row=0)
    label3=Label(new_root,text="Διωνυμικη:")
    label3.grid(column=0,row=1)
    label4=Label(new_root,text="Poison   :")
    label4.grid(column=0,row=2)
    label5=Label(new_root,text="Κανονικη :")
    label5.grid(column=0,row=3)

    def binary():
        new_root1=Tk()
        label3 = Label(new_root1, text="Επιλεξε υπολογισμο")
        label3.grid(column=0, row=0)
        labelx=Label(new_root1,text="Υπολογισμος για x επιτυχιες          ")
        labelx.grid(column=0,row=2)
        labelx_sum=Label(new_root1,text="Yπολογισμος μεχρι και x επιτυχιες")
        labelx_sum.grid(column=0,row=4)
        def valueX():

            label4=Label(new_root1, text="Εισαγωγη μεταβλητων")
            label4.grid(column=20,row=2)
            labelp = Label(new_root1, text="Εισαγωγη Πιθανοτητας      p:")
            labelp.grid(column=20, row=3)
            labeln = Label(new_root1, text="Εισαγωγη Δοκιμων          n:")
            labeln.grid(column=20, row=4)
            labelk = Label(new_root1, text="Εισαγωγη   Επιτυχιων                        k:")
            labelk.grid(column=20, row=5)
            labeld=Label(new_root1,text="                                                                     ")
            labeld.grid(column=20, row=6)
            labele=Label(new_root1,text="                                                           ")
            labele.grid(column=100,row=6)
            p=Entry(new_root1,font=("Arial black",10))
            n=Entry(new_root1,font=("Arial black",10))
            k=Entry(new_root1,font=("Arial black",10))

            p.grid(column=100,row= 3)
            n.grid(column=100,row= 4)
            k.grid(column=100,row= 5)
            def evaluate():
                try :
                    p1=float(p.get())
                    n1=int(n.get())
                    k1=int(k.get())
                except ValueError:
                    print("δες αν συμπληρωσες σωστα τα κενα η επελεξες λαθος εκτελεση")
                num=math.factorial(n1)/(math.factorial(n1-k1)*math.factorial(k1))*pow(p1,k1)*pow(1-p1,n1-k1)
                print("Το αποτελεσμα της διωνυμικης κατανομης ειναι P="+str(round(num,4)))

            button1=Button(new_root1,text="Εκτελεσε για x επιτυχιες",command=evaluate)
            button1.grid(column=8,row=6)

        def value_sum():
            label4 = Label(new_root1, text="Εισαγωγη μεταβλητων")
            label4.grid(column=20, row=2)
            labelp = Label(new_root1, text="Εισαγωγη Πιθανοτητας      p:")
            labelp.grid(column=20, row=3)
            labeln = Label(new_root1, text="Εισαγωγη Δοκιμων          n:")
            labeln.grid(column=20, row=4)
            labelx1 = Label(new_root1, text="Εισαγωγη κατω οριου επιτυχιων   x1:")
            labelx1.grid(column=20, row=5)
            labelx2 = Label(new_root1, text="Εισαγωγη πανω οριου επιτυχιων   x2:")
            labelx2.grid(column=20, row=6)
            p = Entry(new_root1, font=("Arial black", 10))
            n = Entry(new_root1, font=("Arial black", 10))
            x1 = Entry(new_root1, font=("Arial black", 10))
            x2 = Entry(new_root1, font=("Arial black", 10))
            p.grid(column=100, row=3)
            n.grid(column=100, row=4)
            x1.grid(column=100, row=5)
            x2.grid(column=100, row=6)
            def evaluate_sum():
                try:
                    p1 = float(p.get())
                    n1 = int(n.get())
                    k1 = int(x1.get())
                    k2=  int(x2.get())
                except ValueError:
                    print("ok")
                sum=0
                for i in range(k1,k2+1):
                    sum = sum+math.factorial(n1) / (math.factorial(n1 - i) * math.factorial(i)) * pow(p1,i) * pow(1 - p1, n1 - i)
                print("Η αθροιστικη συναρτηση κατανομης στο ("+str(k1)+","+str(k2)+") δινει συνολικη πιθανοτητα P="+str(round(sum,4)))

            button5 = Button(new_root1, text="Εκτελεσε μεχρι x επιτυχιες", command=evaluate_sum)
            button5.grid(column=8,  row=7)


        button6 = Button(new_root1, text="Εκτελεσε", command=value_sum)
        button6.grid(column=8, row=4)
        button2 = Button(new_root1, text="Εκτελεσε", command=valueX)
        button2.grid(column=8, row=2)
    def poison():
        new_root1 = Tk()
        label3 = Label(new_root1, text="Επιλεξε υπολογισμο")
        label3.grid(column=0, row=0)
        labelx = Label(new_root1, text="Υπολογισμος για x επιτυχιες          ")
        labelx.grid(column=0, row=2)
        labelx_sum = Label(new_root1, text="Yπολογισμος μεχρι και x επιτυχιες")
        labelx_sum.grid(column=0, row=3)

        def valueX():

            label4 = Label(new_root1, text="Εισαγωγη μεταβλητων")
            label4.grid(column=20, row=2)
            labelp = Label(new_root1, text="Εισαγωγη μεσης τιμης              λ:")
            labelp.grid(column=20, row=3)
            labeln = Label(new_root1, text="Εισαγωγη χρονικου διστηματος      t:")
            labeln.grid(column=20, row=4)
            labelk = Label(new_root1, text="Εισαγωγη  τυχαιας μεταβλητης      x:")
            labelk.grid(column=20, row=5)

            labeld=Label(new_root1,text="                                                                     ")
            labeld.grid(column=20, row=6)
            labele=Label(new_root1,text="                                                           ")
            labele.grid(column=100,row=6)
            p = Entry(new_root1, font=("Arial black", 10))
            n = Entry(new_root1, font=("Arial black", 10))
            k = Entry(new_root1, font=("Arial black", 10))

            p.grid(column=100, row=3)
            n.grid(column=100, row=4)
            k.grid(column=100, row=5)

            def evaluate():
                try:
                    l = float(p.get())
                    t = float(n.get())
                    x = int(k.get())
                except ValueError:
                    print("οκ")
                num=exp(-l*t)*pow(l*t,x)/math.factorial(x)
                print("Το αποτελεσμα της poison κατανομης ειναι P=" + str(round(num, 4)))
            button1 = Button(new_root1, text="Εκτελεσε για x επιτυχιες", command=evaluate)
            button1.grid(column=8, row=6)
        def value_sum():
            label4 = Label(new_root1, text="Εισαγωγη μεταβλητων")
            label4.grid(column=20, row=2)
            labelp = Label(new_root1, text="Εισαγωγη μεσης τιμης             λ:")
            labelp.grid(column=20, row=3)
            labeln = Label(new_root1, text="Εισαγωγη χρνικου διαστηματος     t:")
            labeln.grid(column=20, row=4)
            labelx1 = Label(new_root1, text="Εισαγωγη κατω οριου επιτυχιων   x1:")
            labelx1.grid(column=20, row=5)
            labelx2 = Label(new_root1, text="Εισαγωγη πανω οριου επιτυχιων   x2:")
            labelx2.grid(column=20, row=6)
            p = Entry(new_root1, font=("Arial black", 10))
            n = Entry(new_root1, font=("Arial black", 10))
            x1 = Entry(new_root1, font=("Arial black", 10))
            x2 = Entry(new_root1, font=("Arial black", 10))
            p.grid(column=100, row=3)
            n.grid(column=100, row=4)
            x1.grid(column=100, row=5)
            x2.grid(column=100, row=6)

            def evaluate_sum():
                try:
                    l = float(p.get())
                    t = float(n.get())
                    k1 = int(x1.get())
                    k2 = int(x2.get())
                except ValueError:
                    print("ok")
                sum = 0
                for i in range(k1, k2 + 1):
                    sum=sum+exp(-l * t) * pow(l * t, i) / math.factorial(i)
                print(str(sum))
                print("Η αθροιστικη συναρτηση poison κατανομης στο (" + str(k1) + "," + str(k2) + ") δινει συνολικη πιθανοτητα P=" + str(round(sum, 4)))


            button5 = Button(new_root1, text="Εκτελεσε μεχρι x επιτυχιες", command=evaluate_sum)
            button5.grid(column=8, row=7)


## Βαλε εδω για αθροιστικη

        button2 = Button(new_root1, text="Εκτελεσε", command=valueX)
        button2.grid(column=10, row=2)
        buttonz=Button(new_root1, text="Εκτελεσε", command=value_sum)
        buttonz.grid(column=10, row=3)
    def normal():
        new_root1=Tk()
        label4 = Label(new_root1, text="Εισαγωγη μεταβλητων")
        label4.grid(column=20, row=2)
        labelp = Label(new_root1, text="Εισαγωγη μεσης τιμης          μ:")
        labelp.grid(column=20, row=3)
        labeln = Label(new_root1, text="Εισαγωγη τυπικης απολισης σ^(2):")
        labeln.grid(column=20, row=4)
        labelx=Label(new_root1, text=  "Εισαγωγη τυχαιας μεταβλητης    x:")
        labelx.grid(column=20, row=5)
        p = Entry(new_root1, font=("Arial black", 10))
        n = Entry(new_root1, font=("Arial black", 10))
        x= Entry(new_root1,font=("Arial black",10))
        p.grid(column=100, row=3)
        n.grid(column=100, row=4)
        x.grid(column=100,row=5)

        def evaluate():
            try:
                m = float(p.get())
                s = float(n.get())
                x1=float(x.get())
            except ValueError:
                print("ok")
            print("H συνολικη πιθανοτητα ειναι P(X<"+str(x1)+")="+str(statistics.NormalDist(mu=m,sigma=s).cdf(x1)))
        button12=Button(new_root1,text="Εκτελεσε",command=evaluate)
        button12.grid(column=100,row=6)

    button3 = Button(new_root, text="Εκτελεσε", command=binary)
    button3.grid(column=10, row=1)
    button7=Button(new_root, text="Εκτελεσε", command=poison)
    button7.grid(column=10, row=2)
    button9 =Button(new_root,text="Εκτελεσε",command=normal)
    button9.grid(column=10,row=3)
# Δημιουργία ετικέτας
label = Label(root, text="Καλώς ήρθατε στο tmath!")
label.pack()
buttons = []
# Δημιουργία κουμπιού
buttons.append(Button(root, text="Κλείσιμο", command=close_window))
buttons.append(Button(root, text="ολοκληρωση", command=new_root))
buttons.append(Button(root, text="παραγωγιση",command=derivative_root))
buttons.append(Button(root, text="επιλυση εξισωσης πολυωνυμου",command=function))
buttons.append(Button(root, text="επιλυση ανισωσης πολυωνυμου",command=inequation))
buttons.append(Button(root, text="γραφικη παρασταση",command=graph))
buttons.append(Button(root, text="υπολογισμος σε σημειο",command=calculate))
buttons.append(Button(root, text="επιλυση συστηματος_3x3",command=system1))
buttons.append(Button(root, text="επιλυση συστηματος_2x2",command=system2))
buttons.append(Button(root, text="ορισμος συναρτησης",command=new_function))
buttons.append(Button(root, text="Κατανομες",command=distribution))
for butt in buttons:
    butt.pack()
# Ξεκίνηση της κύριας βρόχου εκτέλεσης του παραθύρου
root.mainloop()