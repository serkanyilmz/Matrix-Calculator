from tkinter import *
from algorithms import *
from fractions import Fraction


settings = {"font": ("times new roman", 16), "weight": 3,
            "add_delete_font": ("times new roman", 12),
            "button_font": ("helvetica", 10),
            "max_size": 5, "def_row": 4, "def_column": 4,
            "button_width":22,
            "bg_color_1": "#535657",
            "bg_color_2": "#4F646F",
            "bg_color_3": "#B7ADCF",
            "font_color_1":"#F4FAFF",
            "font_color_2":"#DEE7E7", 
            "font_color_3":"black"}


class OPERATION_BUTTON:
    def __init__(self,window,tex,comm=(),type=1,def_val=0,lis=[]):
        if type==1:
            self.butt = Button(window, font=settings["button_font"],text=tex, width=settings["button_width"], padx=10,bg= settings["bg_color_3"], fg=settings["font_color_3"],cursor="hand2",
                               command=comm)
            self.butt.pack(anchor="w", fill="x")
        elif type==2:
            self.fram = Frame(window,bg= settings["bg_color_2"])
            self.fram.pack(anchor="w", fill="x")
            self.butt = Button(self.fram, font=settings["button_font"],bg= settings["bg_color_3"], fg=settings["font_color_3"],cursor="hand2",
                                        text=tex, padx=10, width=settings["button_width"],
                                        command=comm)# width=14
            self.butt.grid(row=0, column=0)
            self.ent = Entry(self.fram, font=settings["button_font"], width=settings["weight"]+1,bg= settings["bg_color_3"], fg=settings["font_color_3"],
                                    justify="center",borderwidth=0)
            self.ent.insert(0,def_val)
            self.ent.grid(row=0, column=1, ipady=4)
        elif type==3:
            self.fram = Frame(window,highlightbackground="grey", highlightthickness=0.5,bg= settings["bg_color_3"])
            self.fram.pack(anchor="center", fill="x")
            self.ent1 = Entry(self.fram, font=settings["button_font"], width=4,bg= settings["bg_color_3"], fg=settings["font_color_3"],
                                            justify="center")
            self.ent1.insert(0, str(lis[0]))
            self.ent1.grid(row=0, column=0, ipady=4)
            self.label1 = Label(self.fram, font=settings["button_font"],width=4,bg= settings["bg_color_3"], fg=settings["font_color_3"],
                                                    text=lis[1])
            self.label1.grid(row=0, column=1, ipady=2)
            self.button=Button(self.fram, font=settings["button_font"],padx=15,bg= settings["bg_color_3"], fg=settings["font_color_3"],cursor="hand2",
                                                    text=tex,width=4)
            self.button.grid(row=0, column=2)
            if len(lis)==3:
                self.ent2 = Entry(self.fram, font=settings["button_font"],width=10,bg= settings["bg_color_3"], fg=settings["font_color_3"],
                                                        justify="center")
                self.ent2.insert(0, str(lis[2]))
                self.ent2.grid(row=0, column=3, ipady=4)
            elif len(lis)==4:
                self.ent2 = Entry(self.fram, font=settings["button_font"],width=4,bg= settings["bg_color_3"], fg=settings["font_color_3"],
                                                        justify="center")
                self.ent2.insert(0, str(lis[2]))
                self.ent2.grid(row=0, column=3, ipady=4)
                self.label2 = Label(self.fram, font=settings["button_font"],width=4,bg= settings["bg_color_3"], fg=settings["font_color_3"],
                                                        text=lis[3])#,highlightbackground="grey", highlightthickness=1)
                self.label2.grid(row=0, column=4, ipady=2)


class CELL:
    def __init__(self, window, ro, co):
        self.r = ro
        self.c = co
        self.ent = Entry(window, font=settings["font"], width=settings["weight"],bg= settings["bg_color_2"],fg=settings["font_color_2"])
        self.ent.grid(row=self.r, column=self.c, pady=1, padx=1)


class MATRIX:
    def __init__(self, name, x, y, r=settings["def_row"], c=settings["def_column"]):
        self.name = name
        self.x = x
        self.y = y
        self.r = r
        self.c = c
        self.cells = []
        self.frame = Frame(root, padx=20, pady=20,bg=settings["bg_color_1"])
        self.frame.place(x=self.x, y=self.y)
        self.header=Frame(self.frame,bg=settings["bg_color_1"])
        self.header.pack(anchor="w")
        self.clear_button = Button(self.header, font=settings["button_font"], text=f"\U0001F9F9", padx=10,bg=settings["bg_color_1"],
                                   fg= settings["font_color_1"],command=self.clear_matrix,relief="flat")
        self.clear_button.grid(row=0,column=1)
        self.name_label = Label(self.header, text=f"Matrix {self.name}", font=settings["font"],bg=settings["bg_color_1"],fg= settings["font_color_1"])
        self.name_label.grid(row=0,column=0)
        self.with_equipments = Frame(self.frame,bg=settings["bg_color_1"])
        self.with_equipments.pack(anchor="w")  # place(x=0, y=0)
        self.box = Frame(self.with_equipments,bg=settings["bg_color_1"])
        self.box.grid(row=0, column=0)
        for xx in range(self.r):
            new_row = []
            for yy in range(self.c):
                new_row.append(CELL(self.box, xx, yy))
            self.cells.append(new_row)
        self.for_col = Frame(self.with_equipments)
        self.for_col.grid(row=0, column=1, sticky="n")
        self.add_column_button = Button(self.for_col, text="+", width=1, relief="flat",
                                        font=settings["add_delete_font"],bg=settings["bg_color_1"],fg= settings["font_color_1"],
                                        command=self.add_column)
        self.add_column_button.grid(row=0, column=2)
        self.delete_column_button = Button(self.for_col, text="-", width=1, relief="flat",
                                           font=settings["add_delete_font"],bg=settings["bg_color_1"],fg= settings["font_color_1"],
                                           command=self.del_column)
        self.delete_column_button.grid(row=0, column=1)
        self.for_row = Frame(self.with_equipments)
        self.for_row.grid(row=1, column=0, sticky="w")
        self.add_row_button = Button(self.for_row, text="+", width=1, relief="flat", font=settings["add_delete_font"],bg=settings["bg_color_1"],fg= settings["font_color_1"],
                                     command=self.add_row)
        self.add_row_button.grid(row=0, column=2)
        self.delete_row_button = Button(self.for_row, text="-", width=1, relief="flat",
                                        font=settings["add_delete_font"],bg=settings["bg_color_1"],fg= settings["font_color_1"],
                                        command=self.del_row)
        self.delete_row_button.grid(row=0, column=1)
        self.for_both = Frame(self.with_equipments)
        self.for_both.grid(row=1, column=1, sticky="w")
        self.add_both_button = Button(self.for_both, text="+", width=1, relief="flat", font=settings["add_delete_font"],bg=settings["bg_color_1"],
                                      fg= settings["font_color_1"],command=lambda: [self.add_column(), self.add_row()])
        self.add_both_button.grid(row=0, column=2)
        self.delete_both_button = Button(self.for_both, text="-", width=1, relief="flat",
                                         font=settings["add_delete_font"],bg=settings["bg_color_1"],fg= settings["font_color_1"],
                                         command=lambda: [self.del_row(), self.del_column()])
        self.delete_both_button.grid(row=0, column=1)

        self.operation_buttons = Frame(self.frame, pady=10,bg=settings["bg_color_1"])
        self.operation_buttons.pack(anchor="w")  # place(x=self.x, y=self.y+200)

        OPERATION_BUTTON(self.operation_buttons, f"Transpose  {self.name}\u1D40",
                         (lambda: answer_transpose(self.get_matrix(), self.name)))
        OPERATION_BUTTON(self.operation_buttons, f"Determinant  det({self.name})  |{self.name}|",
                         (lambda: answer_determinant(self.get_matrix(), self.name)))
        OPERATION_BUTTON(self.operation_buttons, f"Inverse  {self.name}\u207B\u00B9",
                         (lambda: answer_inverse(self.get_matrix(), self.name)))
        OPERATION_BUTTON(self.operation_buttons, f"Trace  Tr({self.name})",
                         (lambda: answer_trace(self.get_matrix(), self.name)))
        add_up_with_but=OPERATION_BUTTON(self.operation_buttons, f"Add up with",
                        type=2,def_val="1")
        add_up_with_but.butt["command"]=(lambda: answer_add_up_with(self.get_matrix(),Fraction(add_up_with_but.ent.get()),self.name))
        multiply_by_but=OPERATION_BUTTON(self.operation_buttons, f"Multiply by",
                        type=2,def_val="2")
        multiply_by_but.butt["command"]=(lambda: answer_multiply_by(self.get_matrix(),Fraction(multiply_by_but.ent.get()),self.name))
        power_to_but=OPERATION_BUTTON(self.operation_buttons, f"Raise to the power of",
                        type=2,def_val="2")
        power_to_but.butt["command"]=(lambda: answer_to_the_power(self.get_matrix(),Fraction(power_to_but.ent.get()),self.name))
        
        
    def tab_arrange(self):
        for x in self.cells:
            for y in x:
                y.ent.lift()

    def add_column(self):
        if self.c < settings["max_size"]:
            self.c += 1
            for x in range(self.r):
                self.cells[x].append(CELL(self.box, x, self.c - 1))
                self.tab_arrange()

    def del_column(self):
        if self.c > 1:
            for x in range(self.r):
                self.cells[x][self.c - 1].ent.destroy()
                self.cells[x].pop(-1)
            self.c -= 1
            self.tab_arrange()

    def add_row(self):
        if self.r < settings["max_size"]:
            self.r += 1
            new_row = []
            for x in range(self.c):
                new_row.append(CELL(self.box, self.r - 1, x))
            self.cells.append(new_row)
            self.tab_arrange()

    def del_row(self):
        if self.r > 1:
            for x in self.cells[-1]:
                x.ent.destroy()
            self.cells.pop(-1)
            self.r -= 1
            self.tab_arrange()

    def get_matrix(self):
        matrix = []
        for x in self.cells:
            new_row = []
            for y in x:
                imp = y.ent.get()  # here if statements
                if imp == "":
                    imp = "0"
                    y.ent.insert(0, "0")
                new_row.append(Fraction(imp))
            matrix.append(new_row)
        return matrix

    def clear_matrix(self):
        for x in self.cells:
            for y in x:
                y.ent.delete(0, END)

    def reorganize(self,matrix):
        self.clear_matrix()
        new_r=len(matrix)
        new_c=len(matrix[0])
        while new_r!=self.r or new_c!=self.c:
            if new_r>self.r:
                self.add_row()
            elif new_r<self.r:
                self.del_row()
            if new_c>self.c:
                self.add_column()
            elif new_c<self.c:
                self.del_column()
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                self.cells[x][y].ent.delete(0, END)
                self.cells[x][y].ent.insert(0, matrix[x][y])


def get_matrices():
    first_matrix = a.get_matrix()
    second_matrix = b.get_matrix()
    return first_matrix, second_matrix

def clear_answer_frame():
    for widget in answer_window.winfo_children():
        widget.destroy()

class show_matrix:
    def __init__(self,matrix, r, c):
        self.matrix_frame = Frame(answer_window,bg=settings["bg_color_1"])
        self.matrix_frame.grid(row=r, column=c)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                cell = Label(self.matrix_frame, text=str(matrix[i][j]), font=settings["button_font"], width=3,bg= settings["bg_color_2"],
                             fg=settings["font_color_2"], highlightbackground="black", highlightthickness=1)
                cell.grid(row=i, column=j)
        self.copy_frame=Frame(self.matrix_frame)
        self.copy_frame.grid(row=len(matrix), column=len(matrix[0]))
        self.copy_to_a_button=Button(self.copy_frame, text="A",command=lambda: self.copy(matrix,"A"),width=1, relief="flat",fg=settings["font_color_1"],
                                        font=settings["add_delete_font"],bg=settings["bg_color_1"])
        self.copy_to_a_button.grid(row=0, column=0)
        self.copy_to_b_button=Button(self.copy_frame, text="B",command=lambda: self.copy(matrix,"B"),width=1, relief="flat",fg=settings["font_color_1"],
                                        font=settings["add_delete_font"],bg=settings["bg_color_1"])
        self.copy_to_b_button.grid(row=0, column=1)
    def copy(self,matrix,name):
        if name=="A":
            a.reorganize(matrix)
        if name=="B":
            b.reorganize(matrix)

def show_label(text,r,c):
    label = Label(answer_window, text=text, font=settings["font"],bg=settings["bg_color_1"],fg=settings["font_color_2"])
    label.grid(row=r, column=c)

def answer_transpose(matrix, name):
    clear_answer_frame()
    show_label(f"If  {name}  =  ",0,0)
    show_matrix(matrix, 0, 1)
    show_label(f"   ,   {name}\u1D40  =  ",0,2)
    show_matrix(transpose(matrix), 0, 3)

def answer_determinant(matrix, name):
    clear_answer_frame()
    determinant_of_matrix = determinant(matrix)
    if determinant_of_matrix == "not_square_error":
        show_label(f"For finding determinant, Matrix {name} must be square.",0,0)
        return 0
    show_label(f"If  {name}  =  ",0,0)
    show_matrix(matrix, 0, 1)
    show_label(f"   ,   det({name})  =  {determinant_of_matrix}",0,2)

def answer_inverse(matrix, name):
    clear_answer_frame()
    inverse_of_matrix = inverse(matrix)
    if inverse_of_matrix == "not_square_error":
        show_label(f"For finding the inverse, Matrix {name} must be square.",0,0)
        return 0
    if inverse_of_matrix == "determinant_zero":
        show_label(f"Det({name}) = 0 , so there is no inverse.",0,0)
        return 0
    show_label(f"If  {name}  =  ",0,0)
    show_matrix(matrix, 0, 1)
    show_label(f"   ,   {name}\u207B\u00B9  =  ",0,2)
    show_matrix(inverse_of_matrix, 0, 3)

def answer_trace(matrix, name):
    clear_answer_frame()
    trace_of_matrix = trace(matrix)
    if trace_of_matrix == "not_square_error":
        show_label(f"For finding the trace, Matrix {name} must be square.",0,0)
        return 0
    show_label(f"If  {name}  =  ",0,0)
    show_matrix(matrix, 0, 1)
    show_label(f"   ,   Tr({name})  =  {trace_of_matrix}",0,2)

def answer_add_up_with(matrix,num,name):
    clear_answer_frame()
    answer=add_up_with(matrix,num)
    show_label(f"If  {name}  =  ",0,0)
    show_matrix(matrix, 0, 1)
    show_label(f"   ,   {name} + {num}   =  ",0,2)
    show_matrix(answer, 0, 3)

def answer_multiply_by(matrix,num,name):
    clear_answer_frame()
    answer=multiply_by(matrix,num)
    show_label(f"If  {name}  =  ",0,0)
    show_matrix(matrix, 0, 1)
    show_label(f"   ,   {num} x {name}   =  ",0,2)
    show_matrix(answer, 0, 3)

def answer_to_the_power(matrix,num, name):
    clear_answer_frame()
    try:
        num=int(num)
    except:
        show_label(f"Power must be an integer.",0,0)
        return 0
    if len(matrix)!=len(matrix[0]):
        show_label(f"Matrix {name} must be square for finding power.",0,0)
        return 0
    answer=matrix.copy()
    for x in range(num-1):
        answer=matrix_multiplication(answer,matrix)
    show_label(f"If  {name}  =  ",0,0)
    show_matrix(matrix, 0, 1)
    show_label(f"   ,   power to {num}   =  ",0,2)
    show_matrix(answer, 0, 3)

def answer_addition():
    clear_answer_frame()
    first_matrix, second_matrix = get_matrices()
    sum_matrix = matrix_addition(first_matrix, second_matrix)
    if sum_matrix == "size_error":
        show_label(f"For matrix addition, matrix sizes must be same.",0,0)
        return 0
    show_matrix(first_matrix, 0, 0)
    show_label(f"+       ",0,1)
    show_matrix(second_matrix, 0, 2)
    show_label(f"=       ",0,3)
    show_matrix(sum_matrix, 0, 4)

def answer_subtraction():
    clear_answer_frame()
    first_matrix, second_matrix = get_matrices()
    result_matrix = matrix_subtraction(first_matrix, second_matrix)
    if result_matrix == "size_error":
        show_label(f"For matrix subtraction, matrix sizes must be same.",0,0)
        return 0
    show_matrix(first_matrix, 0, 0)
    show_label(f"-       ",0,1)
    show_matrix(second_matrix, 0, 2)
    show_label(f"=       ",0,3)
    show_matrix(result_matrix, 0, 4)

def answer_multiplication(first):
    clear_answer_frame()
    if first == "A":
        first_matrix, second_matrix = get_matrices()
    else:
        second_matrix, first_matrix = get_matrices()

    result_matrix = matrix_multiplication(first_matrix, second_matrix)
    if result_matrix == "row_column_error":
        show_label(f"For matrix multiplication, the number of columns in the first matrix\nmust be equal to the number of rows in the second matrix.",0,0)
        return 0
    show_matrix(first_matrix, 0, 0)
    show_label(f"×       ",0,1)
    show_matrix(second_matrix, 0, 2)
    show_label(f"=       ",0,3)
    show_matrix(result_matrix, 0, 4)

def make_identity(matrix_name):
    matrix=matrix_name.get_matrix()
    if len(matrix)!=len(matrix[0]):
        clear_answer_frame()
        show_label(f"Matrix {matrix_name.name} must be square for finding power.",0,0)
        return 0
    identity_matrix=[[0]*len(matrix) for x in range(len(matrix))]
    for x in range(len(matrix)):
        identity_matrix[x][x]=1 
    matrix_name.reorganize(identity_matrix)

def answer_cramer():
    clear_answer_frame()
    first_matrix, second_matrix = get_matrices()
    x_matrix=cramer(first_matrix,second_matrix)
    if x_matrix == "not_square_error":
        show_label(f"For using Cramer's rule, Matrix A must be square.",0,0)
        return 0
    if x_matrix == "determinant_zero":
        show_label(f"For using Cramer's rule,  Det(A) must be different from 0.",0,0)
        return 0
    if x_matrix == "size_error":
        show_label(f"For using Cramer's rule, if A is n×n matrix , B must be n×1 matrix.",0,0)
        return 0
    show_matrix(first_matrix, 0, 0)
    show_label(f"×     ",0,1)
    aw=show_matrix([[f"X{t+1}"] for t in range(len(first_matrix))], 0, 2)
    aw.copy_to_a_button["state"]="disabled"
    aw.copy_to_b_button["state"]="disabled"
    show_label(f"=      ",0,3)
    show_matrix(second_matrix, 0, 4)
    show_label(f"   \u21D2           ",0,5)
    sw=show_matrix([[f"X{t+1}"] for t in range(len(first_matrix))], 0, 6)
    sw.copy_to_a_button["state"]="disabled"
    sw.copy_to_b_button["state"]="disabled"
    show_label(f"=      ",0,7)
    show_matrix(x_matrix, 0, 8)

def replace():
    a_m,b_m =get_matrices()
    a.reorganize(b_m)
    b.reorganize(a_m)

def answer_addition_to_multiplied_matrix(no1,matr1,no2):
    clear_answer_frame()
    try:
        answer_matrix=add_up_with(multiply_by(matr1,no1),no2)
    except:
        show_label(f"Error",0,0)
        return 0
    op="+"
    if no2<0:
        op="-"
        no2=-no2
    show_label(f" {no1} ×  ",0,0)
    show_matrix(matr1, 0, 1)
    show_label(f"     {op} {no2}     =      ",0,2)
    show_matrix(answer_matrix, 0, 3)

def answer_addition_of_multiplied_matrices(no1,matr1,no2,matr2):
    clear_answer_frame()
    try:
        answer_matrix=matrix_addition(multiply_by(matr1,no1),multiply_by(matr2,no2))
    except:
        show_label(f"Error",0,0)
        return 0
    if answer_matrix == "size_error":
        show_label(f"For matrix addition, matrix sizes must be same.",0,0)
        return 0
    op="+"
    if no2<0:
        op="-"
        no2=-no2
    show_label(f"{no1}× ",0,0)
    show_matrix(matr1, 0, 1)
    show_label(f"{op}  {no2}× ",0,2)
    show_matrix(matr2, 0, 3)
    show_label(f"=      ",0,4)
    show_matrix(answer_matrix, 0, 5)



root = Tk()
root.title("Matrix Calculator")
root.config(bg=settings["bg_color_1"])
root.geometry("780x680")

a = MATRIX("A", 0, 0)
b = MATRIX("B", 260, 0)

answer_window = Frame(root, padx=20,bg=settings["bg_color_1"])
answer_window.place(x=5, y=490)

buttons = Frame(root, padx=20, pady=20,bg=settings["bg_color_1"])
buttons.place(x=530, y=0)
OPERATION_BUTTON(buttons, "A + B", answer_addition)
OPERATION_BUTTON(buttons, "A - B", answer_subtraction)
OPERATION_BUTTON(buttons, "A × B", lambda: answer_multiplication("A"))
OPERATION_BUTTON(buttons, "B × A", lambda: answer_multiplication("B"))
addition_to_multiplied_matrix=OPERATION_BUTTON(buttons, "+", type=3, lis=[2, "×A", 3])
addition_to_multiplied_matrix.button["command"]=(lambda: answer_addition_to_multiplied_matrix(Fraction(addition_to_multiplied_matrix.ent1.get()),a.get_matrix(),
                                                                                                  Fraction(addition_to_multiplied_matrix.ent2.get())))
addition_of_multiplied_matrices=OPERATION_BUTTON(buttons, "+", type=3, lis=[2, "×A", 3 , "×B"])
addition_of_multiplied_matrices.button["command"]=(lambda: answer_addition_of_multiplied_matrices(Fraction(addition_of_multiplied_matrices.ent1.get()),a.get_matrix(),
                                                                                                  Fraction(addition_of_multiplied_matrices.ent2.get()),b.get_matrix()))
OPERATION_BUTTON(buttons, "A.x = B ⇒ x=?", answer_cramer)
OPERATION_BUTTON(buttons, "Identity A", lambda: make_identity(a))
OPERATION_BUTTON(buttons, "Identity B", lambda: make_identity(b))
OPERATION_BUTTON(buttons, "Replace A and B", replace)
OPERATION_BUTTON(buttons, "Clear Answer", clear_answer_frame)


root.mainloop()
