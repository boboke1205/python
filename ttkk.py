# coding=utf-8

#
# lbl = Label(root, text="Input Name")
# lbl.pack()
#
# txt = Entry(root)
# txt.pack()
#
#
# btn = Button(root, text="Input")
# btn.pack()
#
# root,mainloop()


# lbl = Label(root, text="test")
# lbl.place(x=50, y = 50)
#
# root.mainloop()

# lbl = Label(root, text="Test")
# lbl.pack()
#
# root.mainloop()
#
# lbl = Label(root, text = "Text1")
# lbl.grid(row=0, column=0)
#
#
# lbl2 = Label(root, text = "Text1")
# lbl2.grid(row=1, column=1)
#
# root.mainloop()
#
#

# from Tkinter import *
#
# root = Tk()
#
# lbl = Label(root, text="Name")
# lbl.grid(row=0, colume=0)
# txt = Entry(root)
# txt.grid(row=0, column=1)
# btn = Button(root, text="Input", width=15)
# btn.grid(row=1, column=1)
#
# root.mainloop()
#
#
#
#
# from Tkinter import *
#
# root = Tk()
#
# lbl = Label(root, text="Label")
# lbl.pack()
#
# btn = Button(root, text="Button")
# btn.pack()
#
# chkbtn = Checkbutton(root, text="Check Button")
# chkbtn.pack()
#
# entry = Entry(root, text = "Entry")
# entry.insert(END, "This is a Entry Widget")
# entry.pack()
#
# listBox = Listbox(root)
# listBox.insert(END, "List1") #index 위치, 텍스트
# listBox.insert(END, "List2")
# listBox.insert(1, "List3")
# listBox.pack()
#
# radio = Radiobutton(root, text="Radio Button", value=1)
# radio.pack()
# radio2 = Radiobutton(root, text="Radio Button2", value=2)
# radio2.pack()
# radio3 = Radiobutton(root, text="Radio Button3", value=3)
# radio3.pack()
#
#
# msg = Message(root, text="This is Messge widget")
# msg.pack()
#
# wScale = Scale(root, from_ = 0, to = 200)
# wScale.pack()
#
# wScale = Scale(root, from_ = 0, to = 100, orient = HORIZONTAL)
# wScale.pack()
#
# text = Text(root, height = 10, width = 80)
# text.insert(END, "This is a Text Widget")
# text.pack()
#
# menubar = Menu(root)
# menubar.add_command(label="Hello!", command=root.quit)
# menubar.add_command(label="Quit", command=root.quit)
#
# root.mainloop()


#
# from Tkinter import *
#
# root = Tk()
#
# def hello():
#     print "hello!"
#
#
# menubar = Menu(root)
#
# filemenu = Menu(menubar)
# filemenu.add_command(label = "Open", command=hello)
# filemenu.add_command(label = "Save", command=hello)
# filemenu.add_separator()
# filemenu.add_command(label = "Exit", command=root.quit)
# menubar.add_cascade(label="File", menu=filemenu)
#
# # create more pulldown menus
# editmenu = Menu(menubar)
# editmenu.add_command(label="Cut", command=hello)
# editmenu.add_command(label="Copy", command=hello)
# editmenu.add_command(label="Paste", command=hello)
# menubar.add_cascade(label="Edit", menu=editmenu)
#
# helpmenu = Menu(menubar)
# helpmenu.add_command(label="About", command=hello)
# menubar.add_cascade(label="Help", menu=helpmenu)
#
# # display the menu
# root.config(menu=menubar)
#
# root.mainloop()
#
# from Tkinter import *
#
# root = Tk()
# frame = Frame(root)
# frame.pack()
#
# bottomframe = Frame(root)
# bottomframe.pack( side = BOTTOM )
#
# redbutton = Button(frame, text="Red", fg="red")
# redbutton.pack( side = LEFT)
#
# greenbutton = Button(frame, text="Brown", fg="brown")
# greenbutton.pack( side = LEFT )
#
# bluebutton = Button(frame, text="Blue", fg="blue")
# bluebutton.pack( side = LEFT )
#
# blackbutton = Button(bottomframe, text="Black", fg="black")
# blackbutton.pack( side = BOTTOM)
#
# root.mainloop()

# from Tkinter import *
#
# root = Tk()
# top = Toplevel()
# top.mainloop()

# coding=utf-8
# from Tkinter import *
#
# root = Tk()
# root.title('Test') # 타이틀
# root.geometry('300x600+200+100') # 창 크기와 창의 위치
# root.mainloop()
#
# coding=utf-8
# from Tkinter import *
# from tkinter import messagebox
# root = Tk()
#
# # 버튼 클릭 이벤트 핸들러
# def okClick():
#     name = txt.get()
#     messagebox.showinfo("당신의 이름은?", name)
#
#
# lbl = Label(root, text="이름")
# lbl.grid(row=0, column=0)
# txt = Entry(root)
# txt.grid(row=0, column=1)
#
# # 버튼 클릭 이벤트와 핸들러 정의
# btn = Button(root, text="OK", command=okClick)  # 위에서 정의한 함수 onClick
#
# btn.grid(row=1, column=1)
#
# root.mainloop()

# coding=utf-8
# from tkinter import *
#
# root = Tk()
#
# frame = Frame(root, width=300, height=300)
# entry = Entry(root)
# entry.pack()
#
#
# def click(event):
#     # entry.delete(0, END) # 내용을 전부 지우고
#     # entry.insert(0, ('Coordinate : %d, %d' % (event.x, event.y)) ) # 내용을 추가
#     # entry.insert(0, ('Coordinate : %s' % (event.char)) ) # 내용을 추가
#     print event.char
#
# frame.bind("<Key>", click) # 왼쪽 마우스 버튼 바인딩
#
#
# frame.pack()
# root.mainloop()


# from Tkinter import *
#
# root = Tk()
#
# frame = Frame(root, width=300, height=300)
# entry = Entry(root)
# entry.pack()
#
#
# def click(event):
#     entry.delete(0, END)
#     entry.insert(0, ('Coordinate : %d, %d' % (event.x, event.y)))
#
#
# frame.bind("<Button-1>", click)

# frame.pack()
# root.mainloop()


from Tkinter import *

from tkinter import messagebox

calculator = Tk()

calculator.geometry('600x300+300+300')

entry = Entry(calculator)
entry.grid(row=0, column=0, columnspan=12, pady=8)
entry.focus_set()

def entryFormula(arg):
    entry.insert(END, arg)
    temp = entry.get()

    if temp[0] == "0":
        entry.delete(0)
        messagebox.showinfo("오류입니다", "숫자 0으로 시작할 수 없습니다")

def change():
    temp = entry.get()
    temp.replace("÷".decode('utf-8'), '/')
    temp.replace("×".decode('utf-8'), "*")
    return temp


def result():
     try:
         result = eval(entry.get())
         entry.delete(0, END)
         entry.insert(0, result)
     except ZeroDivisionError:
         messagebox.showinfo("오류입니다", "0으로 나누었습니다")
         entry.delete(0, END)


def delete():
    entry.delete(0, END)

Button(calculator, text="1", width=6, command=lambda: entryFormula(1)).grid(row=3, column=0)
Button(calculator, text="2", width=6, command=lambda: entryFormula(2)).grid(row=3, column=1)
button3 = Button(calculator, text="3", width=6, command=lambda: entryFormula(3)).grid(row=3, column=2)
button4 = Button(calculator, text="4", width=6, command=lambda: entryFormula(4)).grid(row=2, column=0)
button5 = Button(calculator, text="5", width=6, command=lambda: entryFormula(5)).grid(row=2, column=1)
button6 = Button(calculator, text="6", width=6, command=lambda: entryFormula(6)).grid(row=2, column=2)
button7 = Button(calculator, text="7", width=6, command=lambda: entryFormula(7)).grid(row=1, column=0)
button8 = Button(calculator, text="8", width=6, command=lambda: entryFormula(8)).grid(row=1, column=1)
button9 = Button(calculator, text="9", width=6, command=lambda: entryFormula(9)).grid(row=1, column=2)
button0 = Button(calculator, text="0", width=6, command=lambda: entryFormula(0)).grid(row=4, column=0)
buttonDivide = Button(calculator, text="/", width=6, command=lambda: entryFormula("/")).grid(row=1, column=3)
buttonMultipy = Button(calculator, text="*", width=6, command=lambda: entryFormula("*")).grid(row=2, column=3)
buttonMinus = Button(calculator, text="-", width=6, command=lambda: entryFormula("-")).grid(row=3, column=3)
buttonPlus = Button(calculator, text="+", width=6, command=lambda: entryFormula("+")).grid(row=4, column=2)
buttonEqul= Button(calculator, text="=", width=6, command=lambda: result()).grid(row=4, column=3)
buttonClear = Button(calculator, text="AC", width=6, command=lambda: delete()).grid(row=4, column=1)

calculator.mainloop()






