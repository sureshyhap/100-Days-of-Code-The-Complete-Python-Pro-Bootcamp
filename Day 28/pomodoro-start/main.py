import tkinter as tki
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
is_reset = False

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    timer_label.config(text="Timer", fg=GREEN)
    global is_reset
    is_reset = True

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 2 == 1:
        count_down(WORK_MIN * 60)
        timer_label.config(text="WORK", fg=GREEN)
    elif reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="BREAK", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global is_reset
    if is_reset:
        is_reset = False
        return
    if count > 0:
        minutes = count // 60
        seconds = count % 60
        if minutes < 10:
            minutes = f"0{minutes}"
        if seconds < 10:
            seconds = f"0{seconds}"
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 1:
            check_mark.config(text=f"{check_mark['text']}✔")
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tki.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=75, bg=YELLOW)

timer_label = tki.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 42, "bold"))
timer_label.grid(row=0, column=1)

canvas = tki.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = tki.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 138, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = tki.Button(text="Start")
start_button.config(command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tki.Button(text="Reset")
reset_button["command"] = reset_timer
reset_button.grid(row=2, column=2)

check_mark = tki.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "normal"))
check_mark.grid(row=3, column=1)

window.mainloop()