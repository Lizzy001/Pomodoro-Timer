import tkinter
import math

# ------------------------ CONSTANTS --------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ------------------------ TIMER RESET -------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, "00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")

# ------------------------ TIMER MECHANISM -------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK )
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ------------------------ COUNTDOWN MECHANISM ------------------------ #


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
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)


# ------------------------ UI SETUP ----------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=200, pady=150, bg=YELLOW)



title_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = tkinter.Canvas(width=1024, height=1024, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='C:\\Users\\Elizabeth\\Downloads\\bg-tomatoes.gif')
canvas.create_image(512, 512, image="tomato_img")
timer_text = canvas.create_text(512, 512, text="00:00", file="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2, highlightthickness=0)

check_marks = tkinter.Label(fg=GREEN,bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
