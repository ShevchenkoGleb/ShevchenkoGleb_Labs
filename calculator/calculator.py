import tkinter as tk
from math import sqrt

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Калькулятор")
        master.geometry("450x600")  # Увеличенный размер окна
        master.configure(bg='#f0f2ff')

        # Стилизация поля ввода
        self.entry = tk.Entry(master, width=18, font=('Arial', 26, 'bold'),
                              justify='right', bd=8, relief='flat', bg='#feffff')
        self.entry.grid(row=0, column=0, columnspan=5, sticky='nsew', padx=15, pady=20)

        # Стили кнопок
        button_style = {
            'font': ('Arial', 18, 'bold'),
            'bd': 4,
            'relief': 'raised',
            'bg': '#fff',
            'activebackground': '#ccd9e8',
            'activeforeground': '#fff'
        }

        operator_style = button_style.copy()
        operator_style.update({'bg': '#ccd9e8', 'activebackground': '#a6d8ed'})

        # Расположение кнопок с отступами
        buttons = [
            ('←', 1, 0, operator_style), ('CE', 1, 1, operator_style),
            ('C', 1, 2, operator_style), ('±', 1, 3, operator_style), ('√', 1, 4, operator_style),
            ('7', 2, 0, button_style), ('8', 2, 1, button_style), ('9', 2, 2, button_style),
            ('/', 2, 3, operator_style), ('%', 2, 4, operator_style),
            ('4', 3, 0, button_style), ('5', 3, 1, button_style), ('6', 3, 2, button_style),
            ('*', 3, 3, operator_style), ('1/x', 3, 4, operator_style),
            ('1', 4, 0, button_style), ('2', 4, 1, button_style), ('3', 4, 2, button_style),
            ('-', 4, 3, operator_style), ('=', 4, 4, operator_style),
            ('0', 5, 0, button_style), ('.', 5, 2, button_style), ('+', 5, 3, operator_style)
        ]

        for (text, row, col, style) in buttons:
            btn = tk.Button(master, text=text, width=3, height=1, **style,
                            command=lambda t=text: self.button_click(t))

            # Эффекты при наведении
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg='#a6d9f0'))
            btn.bind("<Leave>", lambda e, b=btn, c=style['bg']: b.config(bg=c))

            # Добавление отступов между кнопками
            pad_x = 5
            pad_y = 5

            if text == '0':
                btn.grid(row=row, column=col, columnspan=2, sticky='nsew', padx=pad_x, pady=pad_y)
            elif text == '=':
                btn.grid(row=4, column=4, rowspan=2, sticky='nsew', padx=pad_x, pady=pad_y)
            else:
                btn.grid(row=row, column=col, sticky='nsew', padx=pad_x, pady=pad_y)

        # Настройка сетки с увеличенными промежутками
        for i in range(6):
            master.rowconfigure(i, weight=1, minsize=75)  # Увеличенная высота строк
        for i in range(5):
            master.columnconfigure(i, weight=1, minsize=85)  # Увеличенная ширина столбцов

        self.current = ''
        self.reset = False

    def button_click(self, value):
        if value == 'C':
            self.current = ''
            self.entry.delete(0, tk.END)
        elif value == 'CE':
            # Очищаем только текущий ввод
            self.current = ''
            self.entry.delete(0, tk.END)
        elif value == '←':
            # Удаляем последний символ
            if self.current:
                self.current = self.current[:-1]
                self.entry.delete(len(self.entry.get()) - 1, tk.END)
        elif value == '±':
            if self.current:
                self.current = str(-1 * float(self.current))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, self.current)
        elif value == '√':
            try:
                self.current = str(sqrt(float(self.current)))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, self.current)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, 'Ошибка')
        elif value == '%':
            try:
                self.current = str(float(self.current) / 100)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, self.current)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, 'Ошибка')
        elif value == '1/x':
            try:
                self.current = str(1 / float(self.current))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, self.current)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, 'Ошибка')
        elif value == '=':
            try:
                result = str(eval(self.current))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
                self.current = result
                self.reset = True
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, 'Ошибка')
        else:
            if self.reset:
                self.current = ''
                self.reset = False
            self.current += value
            self.entry.insert(tk.END, value)

def on_close():
    root.destroy()  # Уничтожает окно и завершает приложение

root = tk.Tk()
calc = Calculator(root)
root.protocol("WM_DELETE_WINDOW", on_close)  # Обработчик закрытия окна
root.mainloop()




