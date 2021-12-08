from tkinter import *

root = Tk()
root.title("PyQuiz")
root.geometry("400x400")


class Quiz:
    def __init__(self, master):
        self.main_frame = Frame(master)
        self.main_frame.pack()

        self.title = Label(self.main_frame, text="Welcome to PyQuiz")
        self.title.grid(row=0, column=0)

        self.start_quiz = Button(self.main_frame, text="Start", command=self.start)
        self.edit_quiz = Button(self.main_frame, text="Edit quiz", command=self.edit)

        self.start_quiz.grid(row=1, column=0)
        self.edit_quiz.grid(row=1, column=1)

    def start(self):
        pass

    def edit(self):
        top = Toplevel()
        top.title("Questions")
        top.geometry("500x400")

        def save():
            status.config(text="Saved     ")
            write_file = open("questions.txt", 'w')
            write_file.write(txt.get(1.0, END))
            write_file.close()

        main_frame = Frame(top)
        main_frame.pack(pady=5)

        # scroll bar
        text_scroll = Scrollbar(main_frame)
        text_scroll.pack(side=RIGHT, fill=Y)

        # text box
        txt = Text(main_frame, width=50, height=15, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
        txt.pack(padx=5)

        # config scrollbar
        text_scroll.config(command=txt.yview)

        # menus
        notepad_menu = Menu(top)
        top.config(menu=notepad_menu)

        file_menu = Menu(notepad_menu, tearoff=False)
        notepad_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save", command=save)
        file_menu.add_separator()
        file_menu.add_command(label="Exit quiz", command=top.quit)

        # status bar
        status = Label(top, text="blooped     ", anchor=E)
        status.pack(fill=X, side=BOTTOM, ipady=5)

        # opening questions.txt
        text_file = open("questions.txt", 'r')
        text_inside = text_file.read()
        # adding stuff from questions.txt to our text box
        txt.insert(END, text_inside)
        # close file
        text_file.close()


q1 = Quiz(root)
root.mainloop()
