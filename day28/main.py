
from tkinter import *
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 5
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    label1.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        label.config(text="Break", fg=GREEN)
    else:
        count_down(WORK_MIN)
        label.config(text="Work", fg=PINK)

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
        label1.config(text=mark)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

window = Tk()
window.title("pomodoma")
window.config(padx=100, pady=50, bg=YELLOW)
label = Label(text="Timer", font=(FONT_NAME, 50), background=YELLOW, fg=GREEN)
label.grid(row=0, column=1)
label1 = Label(background=YELLOW, fg=GREEN)
label1.grid(row=2, column=1)
canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 110, text="00.00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)
button = Button(text="start", command=start_timer)
button.grid(row=2, column=0)
button1 = Button(text="Reset", command=reset_timer)
button1.grid(row=2, column=2)


window.mainloop()
