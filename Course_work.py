from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from tkinter.ttk import *
from random import randint
from math import *
from convertor import Convertor
from algoritms import *
from file_saving import *
import time


class Window:
    def __init__(self, window):
        self.window = window
        self.size = 0
        self.reversed_matrix = []
        self.interface()
        self.button()
        self.enter_matr()
        self.generate_matr()
        self.calc_button()
        self.matr_size()
        self.default_place()
        self.methods()

    """Function for set value, when user press OK during chosing matrix size"""

    def set_size(self, value):
        self.size = value

    """Function that generate nums of matrix"""

    def random_values(self):
        self.matr = [randint(1, self.size * 3) for i in range(self.size**2)]

    """Function that convert array of  numbers to matrix arrays"""

    def convert_to_matr(self):
        self.sequence_converted = []
        for i in range(self.size):
            self.sequence_converted.append([])
            for j in range(self.size):
                self.sequence_converted[i].append(self.matr[j])
            self.matr = self.matr[j + 1:]

    """Main window with size and lable. Window is not resizable"""

    def interface(self):
        self.window.maxsize(width=720, height=540)
        self.window.title('Калькулятор оберненої матриці')
        self.window.geometry('720x540+350+150')
        self.window['bg'] = '#818281'
        lb = Label(self.window, text='Выбери размер матрицы',
                   foreground='#eee', background='#333',
                   font='Calibri 14 bold', justify=CENTER).place(y=13, x=255, height=40)

    """Function that works when user press Ok and we get the size which user chose"""

    def get_size(self):
        self.set_size(int(self.combo.get()[0]))
        print(type(self.size), self.size)

    """Get elements of matrix, try to convert them.In case of mistake, show error"""

    def get_elements(self):
        self.elements = Convertor.convert(self.entry.get('1.0', END))
        if self.elements == False:
            showerror(title='Error',
                      message=f"Введите правильное количество символов '{self.size**2}' и убедитесь в правильности ввода!")
        elif len(self.elements) != self.size**2:
            showerror(title='Error',
                      message=f"Введите правильное количество символов '{self.size**2}' и убедитесь в правильности ввода!")
        else:
            self.matr = self.elements
            self.convert_to_matr()
        # print(self.sequence_converted)

    """Combox for choosing matrix size"""

    def matr_size(self):
        self.combo = Combobox(self.window,
                              font=('Calibri', 12, 'bold'),
                              justify=CENTER)
        self.combo['values'] = ('2x2', '3x3', '4x4',
                                '5x5', '6x6', '7x7', '8x8')
        self.combo.current(0)
        self.combo.place(y=64, x=225, height=27, width=175)

    """Just button. Chosse the matrix size, then press button"""

    def button(self):
        btn = Button(self.window, text='OK', command=self.get_size)
        btn.place(y=65, x=413)

    """//////////////////////////////////////////////////////////////////////"""

    def enter_matr(self):
        self.enter_btn = Button(
            self.window, text='Ввести матрицу', command=self.user_entry_place)
        self.enter_btn.place(y=155, x=10, width=170, height=40)

    # buttons for choosing

    def generate_matr(self):
        self.enter_gener = Button(
            self.window, text='Сгенирировать матрицу', command=self.entry_space_gener)
        self.enter_gener.place(y=155, x=192, width=170, height=40)
    """//////////////////////////////////////////////////////////////////////"""

    """Press button and you'll see the result of calculations"""

    def calc_button(self):
        self.calc_btn = Button(
            self.window, text="Посчитать", command=self.output_result)
        self.calc_btn.place(y=485, x=10, width=150, height=40)

    def button_to_get_input(self):
        self.to_get_btn = Button(
            self.window, text="OK!", command=self.get_elements)
        self.to_get_btn.place(y=462, x=564, width=150, height=40)

    def warning_box(self):
        txt = f"Введите числа матрицы, как в премере ниже!\nПример: 1, 6, 2, 9, 2, 1..."
        self.warning = Label(self.window, text=txt, background='#fc0303',
                             foreground='white', font='Calibri 12 bold')
        self.warning.place(x=385, y=154)

    """Another one window, that we'll see after calculations"""

    def output_result(self):
        showinfo(
            title='Info', message="Результат будет сохранёт в файл, просмотрите вашу директорию!")
        saving = Saving()
        saving.save(self.reversed_matrix)
        time.sleep(1)
        size = self.size
        new_window = Tk()
        new_window.title("Обернена мариця")
        new_window.geometry('+1100+200')
        for i in range(size):
            for j in range(size):
                matr = ttk.Button(new_window, text=str(float("{:.4f}".format(self.reversed_matrix[j][i]))),
                                  width=10)
                matr.grid(column=i, row=j)
        new_window.mainloop()

    """///////////////////////////////////////////////////////////////"""
    # Show generated matrix on the black sheet

    def entry_space_gener(self):
        self.random_values()
        self.convert_to_matr()
        entry_space = Text(self.window)
        entry_space.insert(1.0, "Сгенерированая матрица\n\n")
        entry_space.tag_add('title', 1.0, "1.end")
        entry_space.tag_config('title', font=(
            'Arial', 13, 'bold'), justify=CENTER)
        for i in self.sequence_converted:
            print(i)
        for i in self.sequence_converted[::-1]:
            entry_space.insert(3.0, str(i) + '\n')
            entry_space.tag_add('matr', 3.0, f"{str(self.size+2)}.end")
            entry_space.tag_config('matr', font=(
                'Calibri', 11, 'bold'))
        entry_space.place(x=385, y=154, height=301, width=329)

    # Blank sheet for entry matrix elements
    def user_entry_place(self):
        self.warning_box()
        self.button_to_get_input()
        self.entry = Text(self.window, font='Calibri 11 bold')
        self.entry.place(x=385, y=195, height=265, width=329)

    """///////////////////////////////////////////////////////////////"""

    """Placeholder"""

    def default_place(self):
        def_place = Text(self.window)
        def_place.insert(1.0, "Место для ввода элементов матрици")
        def_place.tag_add('title', 1.0, '1.end')
        def_place.tag_config('title', font=(
            "Calibri", 14, 'bold'), justify=CENTER)
        def_place.place(x=385, y=155, height=300, width=329)

    def calculation_ending(self):
        ending = Edging(self.sequence_converted)
        if any(ending.check_on_zero()) == False:
            showerror(title='Error',
                      message=f"Алгоритм не может посчитать данную матрицу!")
        else:
            self.reversed_matrix = ending.check_on_zero()

    def calculation_blocks(self):
        blocks = Blockwise(self.sequence_converted)
        blocks.check_size()
        if any(blocks.check_size()) == False:
            showerror(title='Error',
                      message=f"Алгоритм не может посчитать данную матрицу!")
        else:
            self.reversed_matrix = array(blocks.reverse)

    """Methods and descriptions"""

    def methods(self):
        # Frame
        method = Frame(self.window, width=350, height=240)
        method.place(x=10, y=215)

        # First description
        burr_des = Text(method, width=20, height=6,
                        bg="red", fg="white", wrap=WORD)
        scroll_1 = Scrollbar(method, command=burr_des.yview)
        scroll_1.place(x=165, y=1, height=100)
        burr_des.config(yscrollcommand=scroll_1.set)

        burr_des.insert(1.0, "Внимание\n")
        burr_des.tag_add('title', 1.0, '1.end')
        burr_des.tag_config('title', font=(
            "Calibri", 13, 'bold'), justify=CENTER)
        burr_des.insert(
            2.0, "Данный алгоритм можно применять к квадратной матрице любой размерности f nff ervs svtb sbrs aaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaa aaaaaaaaaaaaa")
        burr_des.tag_add('text', 2.0, '2.end')
        burr_des.tag_config('text', font=(
            "Arial", 10, 'bold'), justify=LEFT)
        burr_des.place(x=1, y=1)

        # First button
        burr_btn = Button(method, text="Окаймление",
                          command=self.calculation_ending)
        burr_btn.place(x=199, y=13, width=150, height=60)

        # Second sescription
        sep_des = Text(method, width=20, height=6,
                       bg="red", fg="white", wrap=WORD)
        scroll_2 = Scrollbar(method, command=sep_des.yview)
        scroll_2.place(x=165, y=140, height=100)
        sep_des.config(yscrollcommand=scroll_2.set)

        sep_des.insert(1.0, "Внимание\n")
        sep_des.tag_add('title', 1.0, '1.end')
        sep_des.tag_config('title', font=(
            "Calibri", 13, 'bold'), justify=CENTER)
        sep_des.insert(
            2.0, "Данный алгоритм можно применять к квадратной матрице размерности 4х4, 8х8, bvelyjb, qfwv,wvgwvwv wevvvvvvv wegv www fvvvvvvvvvvvvvvvvvw wwwwwwwwwww")
        sep_des.tag_add('text', 2.0, '2.end')
        sep_des.tag_config('text', font=(
            "Arial", 10, 'bold'), justify=LEFT)
        sep_des.place(x=1, y=139)

        # Second button
        sep_btn = Button(method, text="Разбиение на клетки",
                         command=self.calculation_blocks)
        sep_btn.place(x=199, y=164, width=150, height=60)


tk = Tk()
root = Window(tk)
tk.mainloop()
