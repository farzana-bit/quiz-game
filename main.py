import tkinter as tk
from tkinter import messagebox
from quiz_data import quiz_questions
import random
import os

TIME_LIMIT = 15  # seconds per question
HIGHSCORE_FILE = "highscore.txt"


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Master")
        self.root.geometry("700x500")
        self.root.configure(bg="#1e272e")
        self.root.resizable(False, False)

        self.q_index = 0
        self.score = 0
        self.time_left = TIME_LIMIT
        self.selected_answer = tk.StringVar()
        self.timer_id = None

        self.questions = random.sample(quiz_questions, len(quiz_questions))

        self.setup_ui()
        self.load_question()

    def setup_ui(self):
        self.title = tk.Label(self.root, text="🧠 Quiz Master", font=("Helvetica", 28, "bold"),
                              fg="#00cec9", bg="#1e272e")
        self.title.pack(pady=20)

        self.timer_label = tk.Label(self.root, text=f"⏳ Time left: {self.time_left}s",
                                    font=("Helvetica", 14), fg="#fab1a0", bg="#1e272e")
        self.timer_label.pack()

        self.card = tk.Frame(self.root, bg="#2f3640", bd=0,
                             relief="flat", padx=30, pady=20)
        self.card.pack(pady=20, padx=20, fill="both", expand=True)

        self.question_frame = tk.Frame(
            self.card, bg="#353b48", bd=2, relief="ridge")
        self.question_frame.pack(pady=15, fill="x")

        self.question_label = tk.Label(
            self.question_frame,
            text="",
            wraplength=580,
            font=("Helvetica", 17, "bold"),
            fg="#f5f6fa",
            bg="#353b48",
            justify="left",
            anchor="w",
            padx=10,
            pady=10
        )
        self.question_label.pack(fill="both")

        self.radio_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(
                self.card,
                text="",
                variable=self.selected_answer,
                value="",
                font=("Helvetica", 14),
                bg="#2f3640",
                fg="#ffffff",
                selectcolor="#44bd32",
                activebackground="#2f3640",
                activeforeground="#00cec9",
                anchor="w",
                justify="left",
                padx=15
            )
            btn.pack(fill="x", pady=5, padx=10, anchor="w")
            self.radio_buttons.append(btn)

        # ✅ FIXED: Next button moved OUTSIDE the loop
        self.next_button = tk.Button(
            self.root,
            text="Next ➡",
            command=self.next_question,
            font=("Helvetica", 14, "bold"),
            bg="#00cec9",
            fg="#2d3436",
            activebackground="#81ecec",
            activeforeground="#2d3436",
            relief="flat",
            bd=0,
            width=18,
            height=2,
            cursor="hand2",
            highlightthickness=2,
            highlightbackground="#00cec9",
            highlightcolor="#00cec9"
        )
        self.next_button.pack(pady=20)

    def load_question(self):
        if self.q_index < len(self.questions):
            self.time_left = TIME_LIMIT
            self.update_timer()
            q = self.questions[self.q_index]
            self.question_label.config(
                text=f"Q{self.q_index + 1}: {q['question']}")
            self.selected_answer.set("")
            for i, option in enumerate(q["options"]):
                self.radio_buttons[i].config(text=option, value=option)
        else:
            self.finish_quiz()

    def next_question(self):
        selected = self.selected_answer.get()
        if selected == "":
            messagebox.showwarning("Warning", "Please select an answer!")
            return

        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        correct = self.questions[self.q_index]["answer"]
        if selected == correct:
            self.score += 1

        self.q_index += 1
        self.load_question()

    def update_timer(self):
        self.timer_label.config(text=f"⏳ Time left: {self.time_left}s")
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            messagebox.showinfo("Time's Up!", "Moving to the next question.")
            self.q_index += 1
            self.load_question()

    def finish_quiz(self):
        self.save_high_score()
        messagebox.showinfo(
            "Quiz Completed", f"Your score: {self.score}/{len(self.questions)}")
        self.root.destroy()

    def save_high_score(self):
        high_score = 0
        if os.path.exists(HIGHSCORE_FILE):
            with open(HIGHSCORE_FILE, "r") as file:
                try:
                    high_score = int(file.read())
                except ValueError:
                    high_score = 0

        if self.score > high_score:
            with open(HIGHSCORE_FILE, "w") as file:
                file.write(str(self.score))
            messagebox.showinfo(
                "🎉 New High Score!", f"Congratulations! New High Score: {self.score}")
        else:
            messagebox.showinfo(
                "High Score", f"Current High Score: {high_score}")


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
