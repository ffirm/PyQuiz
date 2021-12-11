from tkinter import *

root = Tk()
root.title("PyQuiz")
root.geometry("400x300")


def edit():
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
    file_menu.add_command(label="Exit", command=top.destroy)

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


def process_questions():
    # create class Question for each question in questions.txt
    class Question:
        def __init__(self, q, a, b, c, d, ans):
            self.q = q
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.ans = ans

    questions_list = []
    # extract questions from questions.txt into a list of classes
    with open("questions.txt") as f:
        all_text = f.read().split("\n")
        first_question_offset = all_text.index("QUESTION STARTS HERE:") + 2
        count = 0
        for i in range(first_question_offset, len(all_text), 7):
            # count = 0 is question, count = 1 is choice 1. count = 2 is choice 2 and so on
            temp_q = Question(all_text[i], all_text[i+1], all_text[i+2], all_text[i+3], all_text[i+4], all_text[i+5])
            questions_list.append(temp_q)
    # all questions are now processed and stored in questions_list as objects, ready to use.
    return questions_list


class Quiz:
    def __init__(self, master):
        self.main_frame = Frame(master)
        self.main_frame.pack()

        self.title = Label(self.main_frame, text="Welcome to PyQuiz")
        self.title.grid(row=0, column=0)

        self.start_quiz = Button(self.main_frame, text="Start", command=self.start)
        self.edit_quiz = Button(self.main_frame, text="Edit quiz", command=edit)

        self.start_quiz.grid(row=1, column=0)
        self.edit_quiz.grid(row=1, column=1)

    def start(self):
        question = process_questions()
        global current_score
        current_score = 0
        count = 1

        def press_a():
            if correct_ans == '1':
                global current_score
                current_score += 1
            var.set(1)

        def press_b():
            if correct_ans == '2':
                global current_score
                current_score += 1
            var.set(1)

        def press_c():
            if correct_ans == '3':
                global current_score
                current_score += 1
            var.set(1)

        def press_d():
            if correct_ans == '4':
                global current_score
                current_score += 1
            var.set(1)

        # remove main menu frame and start quiz
        self.main_frame.pack_forget()

        # iterate the question in order to progress the quiz
        # create and delete new frame for every iteration (new question)
        for i in question:
            var = IntVar()
            correct_ans = i.ans

            # new frame where the quiz will be operated on
            new_frame = Frame(root)
            new_frame.pack()

            question_label = Label(new_frame, text=i.q, pady=10)
            question_label.grid(row=0, column=0, columnspan=2)

            btn = Button(new_frame, text=i.a, command=press_a)
            btn.grid(row=1, column=0)
            btn = Button(new_frame, text=i.b, command=press_b)
            btn.grid(row=1, column=1)
            btn = Button(new_frame, text=i.c, command=press_c)
            btn.grid(row=2, column=0)
            btn = Button(new_frame, text=i.d, command=press_d)
            btn.grid(row=2, column=1)

            # status bar at the bottom right
            status_frame = Frame(root)
            status_frame.pack()

            status = f"{count} of {len(question)}"
            status_label = Label(status_frame, text=status, anchor=E)
            status_label.pack(fill=X, side=BOTTOM, ipady=5)
            count += 1

            # Pause the code until user chooses an answer
            btn.wait_variable(var)

            new_frame.destroy()
            status_frame.destroy()

        # End of last question

        # forget result_name frame and pack main_frame back
        def return_to_menu():
            result_frame.pack_forget()
            self.main_frame.pack()

        def try_again():
            result_frame.pack_forget()
            new_frame.pack()

        result_frame = Frame(root)
        result_frame.pack()

        result_label = Label(result_frame, text=f"You scored {current_score} out of {len(question)}!")
        result_label.grid(row=0, column=0)

        try_again_btn = Button(result_frame, text="Try again", command=try_again)
        try_again_btn.grid(row=1, column=0)
        main_menu_btn = Button(result_frame, text="Return to main menu", command=return_to_menu)
        main_menu_btn.grid(row=1, column=1)


q1 = Quiz(root)
root.mainloop()
