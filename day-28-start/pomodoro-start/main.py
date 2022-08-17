
import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 0.5
LONG_BREAK_MIN = 1
reps = 0 
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    for n in range (0,8):
        if n == 8:
            count_down(long_break_sec)
        elif n % 2  == 0:
            count_down(short_break_sec)
        else:
            count_down(work_sec)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec <=9:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(100, count_down, count - 1)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(fg=GREEN, bg=YELLOW, text='Timer',font=(FONT_NAME,45))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
png = PhotoImage(file='day-28-start/pomodoro-start/tomato.png')
canvas.create_image(100, 112, image=png)
timer_text = canvas.create_text(100,130, text='00:00', fill='white', font=(FONT_NAME,35,'bold'))
canvas.grid(column=1, row=1)

start_button = Button(text='Start', highlightthickness=0)
start_button.grid(column=0, row=2)
start_button.config(command=start_timer)
reset_button = Button(text='Reset', highlightthickness=0)
reset_button.grid(column=2, row=2)

check_label = Label(fg=GREEN, bg=YELLOW, text='✓',font=(FONT_NAME,30))
check_label.grid(column=1, row=3)

window.mainloop()
