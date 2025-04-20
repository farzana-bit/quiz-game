import tkinter as tk
from tkinter import messagebox
import json
import random

# Load questions from JSON file
with open('questions.json', 'r') as f:
    questions = json.load(f)

random.shuffle(questions)


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game with Timer")
        self.root.geometry("500x400")

        self.question_index = 0
        self.score = 0
        self.time_left = 30  # seconds per question

        self.question_label = tk.Label(
            root, text="", font=("Arial", 14), wraplength=400)
        self.question_label.pack(pady=20)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", font=("Arial", 12),
                            width=30, command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.timer_label = tk.Label(
            root, text="Time left: 30s", font=("Arial", 12))
        self.timer_label.pack(pady=20)

        self.display_question()
        self.update_timer()

    def display_question(self):
        self.time_left = 30
        current_q = questions[self.question_index]
        self.question_label.config(text=current_q["question"])
        options = current_q["options"]
        random.shuffle(options)
        for i in range(4):
            self.buttons[i].config(text=options[i])

    def check_answer(self, index):
        selected = self.buttons[index].cget("text")
        correct = questions[self.question_index]["answer"]
        if selected == correct:
            self.score += 1
        self.next_question()

    def next_question(self):
        self.question_index += 1
        if self.question_index < len(questions):
            self.display_question()
        else:
            self.end_quiz()

    def update_timer(self):
        self.timer_label.config(text=f"Time left: {self.time_left}s")
        if self.time_left > 0:
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.next_question()

    def end_quiz(self):
        messagebox.showinfo(
            "Quiz Finished", f"Your score: {self.score} / {len(questions)}")
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
