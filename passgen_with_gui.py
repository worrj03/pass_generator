import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import random

def pass_gen():
    char = 'qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
    amount = int(lb_am_inp.get())
    length = int(lb_num_inp.get())
    password = ''
    
    for i in range(amount):
        for n in range(length):
            password += random.choice(char)
        password += '\n'

    mb.showinfo('Пароль', password)
    file = fd.asksaveasfilename(filetypes=(['Excel file'])) 
    f = open(file, 'w')
    f.write(password)
    f.close()

def show_pass():
    char = 'qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
    amount = int(lb_am_inp.get())
    length = int(lb_num_inp.get())
    password = ''
    
    for i in range(amount):
        for n in range(length):
            password += random.choice(char)
        password += '\n'
    mb.showinfo('Пароль', password)  


window = Tk()
window.title('Password generator')
window.geometry('1000x500')
window.configure(bg='green')


frame = Frame(
    window, #обязательный параметр, кот указывает окно для размещения frame
    padx = 10, # отступ по горизонтали
    pady = 10 # отступ по вертикали
)
frame.pack (expand=True)

#лейблы
lb_am = Label(
    frame,
    text='Введите количество необходимых паролей',
    foreground='red'
)
lb_am.grid(row=3, column=1)

lb_num = Label(
    frame,
    text='Введите длину пароля',
    foreground='red'
)
lb_num.grid(row=4, column=1)

#поле ввода
lb_am_inp = Entry(
    frame
)
lb_am_inp.grid(row=3, column=2)

lb_num_inp = Entry(
    frame
)
lb_num_inp.grid(row=4, column=2)


#кнопки

gen_btn = Button(
    frame,
    text = 'Скачать',
    foreground='black',
    command = pass_gen
)
gen_btn.grid(row = 6, column =2)

show_pass = Button(
    frame,
    text = 'Получить пароль',
    foreground='black',
    command = show_pass
)
show_pass.grid(row = 5, column =2)




window.mainloop()