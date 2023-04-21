import tkinter as tk
a=0
tabla = [[".",".","."],
         [".",".","."],
         [".",".","."]]

#win status

def disable():
    myButton['state'] = 'disabled'
    myButton2['state'] = 'disabled'
    myButton3['state'] = 'disabled'
    myButton4['state'] = 'disabled'
    myButton5['state'] = 'disabled'
    myButton6['state'] = 'disabled'
    myButton7['state'] = 'disabled'
    myButton8['state'] = 'disabled'
    myButton9['state'] = 'disabled'


def Check():
#diagonala1
    if tabla[0][0] == "x" and tabla[1][1] == "x" and tabla[2][2] == "x":
        if a%2==0:
            masterWindow.title('X a castigat')
            disable()
        else:
            masterWindow.title('0 a castigat')
            disable()
    if tabla[0][0] == "0" and tabla[1][1] == "0" and tabla[2][2] == "0":
        if a%2==0:
            masterWindow.title('X a castigat')
            disable()
        else:
            masterWindow.title('0 a castigat')
            disable()
#diagonala2
    if tabla[0][2] == "x" and tabla[1][1] == "x" and tabla[2][0] == "x":
        if a%2==0:
            masterWindow.title('X a castigat')
            disable()
        else:
            masterWindow.title('0 a castigat')
            disable()
    if tabla[0][2] == "0" and tabla[1][1] == "0" and tabla[2][0] == "0":
        if a%2==0:
            masterWindow.title('X a castigat')
            disable()
        else:
            masterWindow.title('0 a castigat')
            disable()
#rand 1
    if tabla[0][0] == "x" and tabla[1][0] == "x" and tabla[2][0] == "x":
        if a%2==0:
            masterWindow.title('X a castigat')
            disable()
        else:
            masterWindow.title('0 a castigat')
            disable()
    if tabla[0][0] == "0" and tabla[1][0] == "0" and tabla[2][0] == "0":
        if a%2==0:
            masterWindow.title('X a castigat')
            disable()
        else:
            masterWindow.title('0 a castigat')
            disable()
#rand 2
    if tabla[0][1] == "x" and tabla[1][1] == "x" and tabla[2][1] == "x":
        if a%2==0:
            masterWindow.title('X a castigat')
            disable()
        else:
            masterWindow.title('0 a castigat')
            disable()
    if tabla[0][1] == "0" and tabla[1][1] == "0" and tabla[2][1] == "0":
        if a%2==0:
            masterWindow.title('X a castigat')
            disable()
        else:
            masterWindow.title('0 a castigat')
            disable()
#rand 3
    if tabla[0][2] == "x" and tabla[1][2] == "x" and tabla[2][2] == "x":
        if a%2==0:
            masterWindow.title('X a castigat')
            disable()
        else:
            masterWindow.title('0 a castigat')
            disable()
    if tabla[0][2] == "0" and tabla[1][2] == "0" and tabla[2][2] == "0":
        if a%2==0:
            masterWindow.title('X a castigat')
            disable()
        else:
            masterWindow.title('0 a castigat')
            disable()
#coloana 1
    if tabla[0][0] == "x" and tabla[0][1] == "x" and tabla[0][2] == "x":
        if a%2==0:
            masterWindow.title('X a castigat')
            disable()
        else:
            masterWindow.title('0 a castigat')
    if tabla[0][0] == "0" and tabla[0][1] == "0" and tabla[0][2] == "0":
        if a%2==0:
            masterWindow.title('X a castigat')
            disable()
        else:
            masterWindow.title('0 a castigat')
            disable()
#coloana 2
    if tabla[1][0] == "x" and tabla[1][1] == "x" and tabla[1][2] == "x":
        if a%2==0:
            masterWindow.title('X a castigat')
            disable()
        else:
            masterWindow.title('0 a castigat')
    if tabla[1][0] == "0" and tabla[1][1] == "0" and tabla[1][2] == "0":
        if a%2==0:
            masterWindow.title('X a castigat')
            disable()
        else:
            masterWindow.title('0 a castigat')
            disable()
#coloana 3
    if tabla[2][0] == "x" and tabla[2][1] == "x" and tabla[2][2] == "x":
        if a%2==0:
            masterWindow.title('X a castigat')
            disable()
        else:
            masterWindow.title('0 a castigat')
            disable()
    if tabla[2][0] == "0" and tabla[2][1] == "0" and tabla[2][2] == "0":
        if a%2==0:
            masterWindow.title('X a castigat')
            disable()
        else:
            masterWindow.title('0 a castigat')
            disable()

    if tabla[0][0]!="." and tabla[0][1]!="." and tabla[0][2]!="." and tabla[1][0]!="." and tabla[1][1]!="." and tabla[1][2]!="." and tabla[2][0]!="." and tabla[2][1]!="." and tabla[2][2]!=".":
        masterWindow.title("Remiza")

#button functions

def Delete1():
    row=0
    column=0
    global a
    if a%2==0:
        text = 'X'
        tabla[row][column] = "x"
        Check()
    else:
        text = '0'
        tabla[row][column] = "0"
        Check()
    a+=1
    myButton['text'] = text
    myButton['state'] = 'disabled'
    

def Delete2():
    row=0
    column=1
    global a
    if a%2==0:
        text='X'
        tabla[row][column] = "x"
        Check()
    else:
        text='0'
        tabla[row][column] = "0"
        Check()
    a+=1
    myButton2['text'] = text
    myButton2['state'] = 'disabled'

def Delete3():
    row=0
    column=2
    global a
    if a%2==0:
        text='X'
        tabla[row][column] = "x"
        Check()
    else:
        text='0'
        tabla[row][column] = "0"
        Check()
    a+=1
    myButton3['text'] = text
    myButton3['state'] = 'disabled'

def Delete4():
    row=1
    column=0
    global a
    if a%2==0:
        text='X'
        tabla[row][column] = "x"
        Check()
    else:
        text='0'
        tabla[row][column] = "0"
        Check()
    a+=1
    myButton4['text'] = text
    myButton4['state'] = 'disabled'

def Delete5():
    row=1
    column=1
    global a
    if a%2==0:
        text='X'
        tabla[row][column] = "x"
        Check()
    else:
        text='0'
        tabla[row][column] = "0"
        Check()
    a+=1
    myButton5['text'] = text
    myButton5['state'] = 'disabled'

def Delete6():
    row=1
    column=2
    global a
    if a%2==0:
        text='X'
        tabla[row][column] = "x"
        Check()
    else:
        text='0'
        tabla[row][column] = "0"
        Check()
    a+=1
    myButton6['text'] = text
    myButton6['state'] = 'disabled'

def Delete7():
    row=2
    column=0
    global a
    if a%2==0:
        text='X'
        tabla[row][column] = "x"
        Check()
    else:
        text='0'
        tabla[row][column] = "0"
        Check()
    a+=1
    myButton7['text'] = text
    myButton7['state'] = 'disabled'

def Delete8():
    row=2
    column=1
    global a
    if a%2==0:
        text='X'
        tabla[row][column] = "x"
        Check()
    else:
        text='0'
        tabla[row][column] = "0"
        Check()
    a+=1
    myButton8['text'] = text
    myButton8['state'] = 'disabled'

def Delete9():
    row=2
    column=2
    global a
    if a%2==0:
        text='X'
        tabla[row][column] = "x"
        Check()
    else:
        text='0'
        tabla[row][column] = "0"
        Check()
    a+=1
    myButton9['text'] = text
    myButton9['state'] = 'disabled'


masterWindow = tk.Tk()

# window title
masterWindow.title("X0 Game")

# window size
masterWindow.minsize(825, 815)
masterWindow.maxsize(825, 815)

#background
masterWindow.configure(bg="Black")

# frame
button_frame = tk.Frame(masterWindow)
button_frame.config(bg='Black')
button_frame.pack(fill=tk.BOTH, expand=True)

# buttons

myButton = tk.Button(button_frame, text="",command=Delete1, width=35, height=16,bg="White")
myButton.grid(row=0, column=0, padx=10, pady=10)


myButton2 = tk.Button(button_frame, text="",command=Delete2, width=35, height=16,bg="White")
myButton2.grid(row=0, column=1, padx=10, pady=10)

row=0
column=2
myButton3 = tk.Button(button_frame, text="",command=Delete3, width=35, height=16,bg="White")
myButton3.grid(row=0, column=2, padx=10, pady=10)

row=1
column=0
myButton4 = tk.Button(button_frame, text="",command=Delete4, width=35, height=16,bg="White")
myButton4.grid(row=1, column=0, padx=10, pady=10)

row=1
column=1
myButton5 = tk.Button(button_frame, text="",command=Delete5, width=35, height=16,bg="White")
myButton5.grid(row=1, column=1, padx=10, pady=10)

row=1
column=2
myButton6 = tk.Button(button_frame, text="",command=Delete6, width=35, height=16,bg="White")
myButton6.grid(row=1, column=2, padx=10, pady=10)

row=2
column=0
myButton7 = tk.Button(button_frame, text="",command=Delete7, width=35, height=16,bg="White")
myButton7.grid(row=2, column=0, padx=10, pady=10)

row=2
column=1
myButton8 = tk.Button(button_frame, text="",command=Delete8, width=35, height=16,bg="White")
myButton8.grid(row=2, column=1, padx=10, pady=10)

row=2
column=2
myButton9 = tk.Button(button_frame, text="",command=Delete9, width=35, height=16,bg="White")
myButton9.grid(row=2, column=2, padx=10, pady=10)


masterWindow.mainloop()
