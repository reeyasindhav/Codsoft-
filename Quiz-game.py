import tkinter as tk
from tkinter import messagebox
import random

class QuizGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")
        self.master.geometry("400x300")
        self.master.configure(bg="#e6e6e6")

        self.questions = [
            {"question": "What is the capital of Japan?", "options": ["Beijing", "Tokyo", "Seoul", "Bangkok"], "correct_option": "Tokyo"},
            {"question": "Which country is known as the Land of the Rising Sun?", "options": ["China", "Japan", "Korea", "Thailand"], "correct_option": "Japan"},
            {"question": "Who is the author of the Harry Potter book series?", "options": ["J.R.R. Tolkien", "J.K. Rowling", "George R.R. Martin", "Stephen King"], "correct_option": "J.K. Rowling"},
        ]

        self.current_question_index = 0
        self.score = 0

        self.label_question = tk.Label(self.master, text="", font=("Arial", 12), bg="#e6e6e6")
        self.label_question.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.radio_var.set("")

        self.radio_buttons = []
        for i in range(4):
            radio_btn = tk.Radiobutton(self.master, text="", variable=self.radio_var, value="", bg="#e6e6e6")
            radio_btn.pack(anchor="w", padx=20)
            self.radio_buttons.append(radio_btn)

        self.next_button = tk.Button(self.master, text="Next", command=self.next_question, bg="#4CAF50", fg="white", activebackground="#45a049", activeforeground="white")
        self.next_button.pack(pady=10)

        self.load_question()

    def load_question(self):
        self.radio_var.set("")
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.label_question.config(text=question_data["question"])

            options = question_data["options"]
            random.shuffle(options)
            for i in range(4):
                self.radio_buttons[i].config(text=options[i], value=options[i])

        else:
            self.show_result()

    def select_option(self):
        selected_option = self.radio_var.get()
        correct_option = self.questions[self.current_question_index]["correct_option"]

        if selected_option == correct_option:
            self.score += 1

    def next_question(self):
        if self.radio_var.get():
            self.select_option()
            self.current_question_index += 1
            if self.current_question_index < len(self.questions):
                self.load_question()
            else:
                self.show_result()
        else:
            messagebox.showwarning("Warning", "Please select an option before proceeding to the next question.")

    def show_result(self):
        messagebox.showinfo("Quiz Result", f"Your Score: {self.score}/{len(self.questions)}")
        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if play_again:
            self.current_question_index = 0
            self.score = 0
            self.load_question()
        else:
            self.master.destroy()

def main():
    root_quiz = tk.Tk()
    quiz_game = QuizGame(root_quiz)
    root_quiz.mainloop()

if __name__ == "__main__":
    main()
