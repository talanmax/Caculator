import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title("Какулятор")
win.geometry(f"300x270+100+200")
win.resizable(False, False)
win['bg'] = 'orange'


def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc['state'] = tk.NORMAL
    calc.delete(0, 'end')
    calc.insert(0, value + digit)
    calc['state'] = tk.DISABLED


def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+/.':
        value = value[: -1]
    elif value[-1] in '*' and value[-2] in '*':
        value = value[: -1]
    calc['state'] = tk.NORMAL
    calc.delete(0, 'end')
    calc.insert(0, value + operation)
    calc['state'] = tk.DISABLED


def calculate():
    value = calc.get()
    calc['state'] = tk.NORMAL
    calc.delete(0, 'end')
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Увага!', 'Потрібно вводити тільки цифри, ви ввели інші символи')
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Увага!', 'На нуль ділити не можна!')
        calc.insert(0, 0)
    calc['state'] = tk.DISABLED


def clear():
    calc['state'] = tk.NORMAL
    calc.delete(0, 'end')
    calc.insert(0, '0')
    calc['state'] = tk.DISABLED


def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=("Arial", 13), command=lambda: add_digit(digit))


def make_operarion_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red',
                     command=lambda: add_operation(operation))


def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red',
                     command=calculate)


def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red',
                     command=clear)


def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/.':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()
    elif event.char == '\x1b':
        clear()
    elif event.char == '\x08':
        calc['state'] = tk.NORMAL
        a = calc.get()
        b = len(a)
        calc.delete(b - 1)
        if b == 1:
            calc.insert(0, '0')
        calc['state'] = tk.DISABLED


def mod():
    value = calc.get()
    if value[-1] in '*' and value[-2] in '*':
        value = value[: -1]
    else:
        add_operation('**')


def znak():
    add_operation('*-1')
    calculate()


def make_modul_button(operation):
    return tk.Button(text='x²', bd=5, font=('Arial', 13), fg='red',
                     command=mod)


def make_tochka_button(operation):
    return tk.Button(text=',', bd=5, font=('Arial', 13), fg='red',
                     command=lambda: add_operation('.'))


def make_znak_button(operation):
    return tk.Button(text='+/-', bd=5, font=('Arial', 13), fg='red',
                     command=znak)


win.bind('<Key>', press_key)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0, '0')
calc['state'] = tk.DISABLED
calc.grid(row=0, column=0, columnspan=5, stick='we', padx=5)

make_digit_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_digit_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_digit_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

make_operarion_button("+").grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operarion_button("-").grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operarion_button("*").grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operarion_button("/").grid(row=4, column=3, stick='wens', padx=5, pady=5)

make_calc_button("=").grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_clear_button("C").grid(row=4, column=1, stick='wens', padx=5, pady=5)
make_modul_button("^").grid(row=1, column=4, stick='wens', padx=5, pady=5)
make_tochka_button(".").grid(row=2, column=4, stick='wens', padx=5, pady=5)
make_znak_button(".").grid(row=3, column=4, stick='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)
win.grid_columnconfigure(4, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()
