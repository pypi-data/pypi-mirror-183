import time
from tkinter import *
import tkinter.messagebox
import datetime
import os
import random
import turtle



class Operator():
    class Other():
        class _Find_Numb_Of_Square_Root():
            def Window(x):
                t = Tk()
                t.title("Square Root")
                t.geometry("500x500")

                
                send = x ** 2


                Lab = Label(t, text=send).pack()



                t.mainloop()
            def Basic(x):
                xy = x
                R = int(xy ** 2)
                return f"The anwser of your question : is : {str(R)}"
        class Find_Square_Root():
            def Window(x):
                t = Tk()
                t.title("Square Root")
                t.geometry("500x500")

                
                res = x ** 0.5


                Lab = Label(t, text=f"Rep : {res}").pack()



                t.mainloop()
            def Basic(Base):
                n = Base
                res = n**0.5
                return f"The result is : {str(res)}"
        class Pourcentage():


            def returner(PercentOf, What,  OriginalValue):
                SO = float( OriginalValue ) 


                Minus_DATA_Val = ( int(PercentOf) / int(What) ) * SO

                res = SO - Minus_DATA_Val


                return "You saved : " + str(Minus_DATA_Val) + " and your total is : " + str(res)



        class PowerNumber():
            def Gui():
                W = Tk()
                W.title("Soustraction - 2023-2024yrs ")
                W.geometry("500x500")
                LET1 = Label(W, text="The First value").pack()
                talone = Entry(W)
                talone.pack()
                LET2 = Label(W, text="The second value").pack()
                taltwo = Entry(W)
                taltwo.pack()
                

                def MessRes():
                    tkinter.messagebox.showinfo("Results", int(talone.get()) ** int(taltwo.get()))

                ButtonSend = Button(W, text="Send and add '[T1 ** T2]' VALUE",command=MessRes)
                ButtonSend.pack()


                W.mainloop()
            def Terminal():
                ValueN1 = int(input("Enter first arguments(value) : "))
                ValueN2 = int(input("Enter second arguments(value) : "))
                def Play(x,y):
                    return x ** y
                QSD = input("See the result : ")
                if QSD == "yes" or QSD == "Yes":
                    print(Play(ValueN1, ValueN2))
    class Adition():
        def Gui():
            W = Tk()
            W.title("Addition - 2023-2024yrs ")
            W.geometry("500x500")
            LET1 = Label(W, text="The First value").pack()
            talone = Entry(W)
            talone.pack()
            LET2 = Label(W, text="The second value").pack()
            taltwo = Entry(W)
            taltwo.pack()
            
            def MessRes():
                tkinter.messagebox.showinfo("Results", int(talone.get()) + int(taltwo.get()))

            ButtonSend = Button(W, text="Send and add '[T1 + T2]' VALUE",command=MessRes)
            ButtonSend.pack()


                    

            



            



            

           



            W.mainloop()
            def GuiError():
                import tkinter.messagebox
                tkinter.messageboxmessagebox.showerror(
                        "Error in the program", 
                        "The error is to find, but the rules dont be accept if you dont write the good code or you dont use the good number (exemple: you use charcter and not number...)")
                W = Tk()
                W.title("Error")



                W.mainloop()
        def Terminal():
            ValueN1 = int(input("Enter first arguments(value) : "))
            ValueN2 = int(input("Enter second arguments(value) : "))
            def Play(x,y):
                return x + y
            QSD = input("See the result : ")
            if QSD == "yes" or QSD == "Yes":
                print(Play(ValueN1, ValueN2))
    class Soustraction():
        def Gui():
            W = Tk()
            W.title("Soustraction - 2023-2024yrs ")
            W.geometry("500x500")
            LET1 = Label(W, text="The First value").pack()
            talone = Entry(W)
            talone.pack()
            LET2 = Label(W, text="The second value").pack()
            taltwo = Entry(W)
            taltwo.pack()
            
            def MessRes():
                tkinter.messagebox.showinfo("Results", int(talone.get()) - int(taltwo.get()))

            ButtonSend = Button(W, text="Send and add '[T1 - T2]' VALUE",command=MessRes)
            ButtonSend.pack()


            W.mainloop()
        def Terminal():
            ValueN1 = int(input("Enter first arguments(value) : "))
            ValueN2 = int(input("Enter second arguments(value) : "))
            def Play(x,y):
                return x - y
            QSD = input("See the result : ")
            if QSD == "yes" or QSD == "Yes":
                print(Play(ValueN1, ValueN2))
    class Multiplication():
        def Gui():
            W = Tk()
            W.title("Multiplication - 2023-2024yrs ")
            W.geometry("500x500")
            LET1 = Label(W, text="The First value").pack()
            talone = Entry(W)
            talone.pack()
            LET2 = Label(W, text="The second value").pack()
            taltwo = Entry(W)
            taltwo.pack()
            
            def MessRes():
                    tkinter.messagebox.showinfo("Results", int(talone.get()) * int(taltwo.get()))

            ButtonSend = Button(W, text="Send and add '[T1 * T2]' VALUE",command=MessRes)
            ButtonSend.pack()

            W.mainloop()
        def Terminal():
            ValueN1 = int(input("Enter first arguments(value) : "))
            ValueN2 = int(input("Enter second arguments(value) : "))
            def Play(x,y):
                return x * y
            QSD = input("See the result : ")
            if QSD == "yes" or QSD == "Yes":
                print(Play(ValueN1, ValueN2))
    class Division():
        def Gui():
            W = Tk()
            W.title("Division - 2023-2024yrs ")
            W.geometry("500x500")
            LET1 = Label(W, text="The First value").pack()
            talone = Entry(W)
            talone.pack()
            LET2 = Label(W, text="The second value").pack()
            taltwo = Entry(W)
            taltwo.pack()
            
            def dATA_():
                NW = Tk()
                NW.title("Result of dATA_TYPES")
                NW.geometry("500x300")
            def MessRes():
                    tkinter.messagebox.showinfo("Results", int(talone.get()) / int(taltwo.get()))

            ButtonSend = Button(W, text="Send and add '[T1 / T2]' VALUE",command=MessRes)
            ButtonSend.pack()


            W.mainloop()
        def Terminal():
            ValueN1 = int(input("Enter first arguments(value) : "))
            ValueN2 = int(input("Enter second arguments(value) : "))
            def Play(x,y):
                return x / y
            QSD = input("See the result : ")
            if QSD == "yes" or QSD == "Yes":
                print(Play(ValueN1, ValueN2))

class ProblemRandom():
    class Adition():
        def Gui():
            None
        def Basic():
            None
    class Soustraction():
        def Window():
            None
        def Basic():
            None
        def Gui():
            None
        def Basic():
            None
    class Division():
        def Gui():
            None
        def Basic():
            None



class DrawerPos():


    class DrawerLibrary():
        class Shape():
            def Circle( WindowName, Size, TextColor, Speed, waitTime, BgColor ):
                andS = turtle.Screen()
                andS.title(WindowName)
                t = turtle.Turtle()
                t.color(TextColor)
                t.speed(Speed)
                turtle.bgcolor(BgColor)
                time.sleep(waitTime)
                t.circle(Size)

                turtle.done()
            def Rectangle( SizeOfBlack,VerticalLine, HorizontalLine, Color, speed, BackgroundColor, WindowName ):
                def On_Off():
                    t = turtle.Turtle()
                    Ts = turtle.Screen()
                    Ts.title(WindowName)
                    Ts.bgcolor(BackgroundColor)
                    t.speed(speed)
                    t.width(SizeOfBlack)
                    t.color(Color)

                    t.forward(HorizontalLine/2)
                    t.left(90)
                    t.forward(VerticalLine)
                    t.left(90)
                    t.forward(HorizontalLine)
                    t.left(90)
                    t.forward(VerticalLine)
                    t.left(90)
                    t.forward(HorizontalLine/2)
                    turtle.done()


                On_Off()
                
            def Square(SizeOfBlack, Line,Color, speed, BackgroundColor, WindowName):
                t = turtle.Turtle()
                t.color(Color)
                t.speed(speed)
                t.width(SizeOfBlack)
                Ts = turtle.Screen()
                Ts.bgcolor(BackgroundColor)
                Ts.title(WindowName)

                def On_Play_Classifier():
                    t.forward(Line/2)
                    t.left(90)
                    t.forward(Line)
                    t.left(90)
                    t.forward(Line)
                    t.left(90)
                    t.forward(Line)
                    t.left(90)
                    t.forward(Line/2)

                    turtle.done()
                On_Play_Classifier()
            def Rombhus(Color, speed, BackgroundColor, WindowName):
                print("Will apear in next Update 0.0.4")
            def Pentagone(Color, speed, BackgroundColor, WindowName):
                print("Will apear in next Update 0.0.4")
            def Hexagone(Line, Color, speed, BackgroundColor, WindowName):
                print("Will apear in 0.0.4 Update sorry :(")
            def Octogone(Line,Color, speed, BackgroundColor, WindowName):
                andS = turtle.Screen()
                andS.title(WindowName)
                t = turtle.Turtle()
                LEFTVAMUE = 90/2
                t.color(Color)
                t.speed(speed)
                turtle.bgcolor(BackgroundColor)
                t.forward(Line/2)
                t.left(LEFTVAMUE)
                t.forward(Line)
                t.left(LEFTVAMUE)
                t.forward(Line)
                t.left(LEFTVAMUE)
                t.forward(Line)
                t.left(LEFTVAMUE)
                t.forward(Line)
                t.left(LEFTVAMUE)
                t.forward(Line)
                t.left(LEFTVAMUE)
                t.forward(Line)
                t.left(LEFTVAMUE)
                t.forward(Line)
                t.left(LEFTVAMUE)
                t.forward(Line/2)


                turtle.done()
            def Triangle(SizeLine ,leftFirst, LeftOf2line,Color, speed, BackgroundColor, WindowName):
                andS = turtle.Screen()
                andS.title(WindowName)
                t = turtle.Turtle()
                t.color(Color)
                t.speed(speed)
                turtle.bgcolor(BackgroundColor)
                t.forward(SizeLine/2)
                t.left(leftFirst)
                t.forward(SizeLine)
                t.left(LeftOf2line)
                t.forward(SizeLine)
                t.left(LeftOf2line)
                t.forward(SizeLine/2)

                

                turtle.done()
 
        class PersonOrPeople():
            None 

