# HIGHLIGHTS
## global var: to set, to change and to use it in different local funs

from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

rep_round = 1

timer = None
## Will define it later in fun, here just bring to a Global var which more than 1 funs can use
## for window.after() and window.after_cancel()

# ---------------------------- TIMER RESET ------------------------------- #
# RESET everything
# most important: to stop the count_down
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(count_display, text='00:00')
    label_timer.config(text='Timer', fg=GREEN)
    label_tick.config(text='')
    global rep_round
    rep_round = 1

# ---------------------------- TIMER MECHANISM ------------------------------- # 
# pomoroto TIME RULES:
## round 1,3,5,7 rounds: 25min work
## round 2,4,6: 5min Break
## round 8th: 20min Break -- END

def start_timer():
    global rep_round

    if rep_round % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        label_timer.config(text='Long-Break', fg=RED)
        ## window_after (LONG_BREAK_MIN * 1000, start_timer()) -- my note: 见def count_down()
    elif rep_round % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        label_timer.config(text='Short-Break', fg=GREEN)
    else:
        count_down(WORK_MIN*60)
        label_timer.config(text='On-Work', fg=PINK)

    check_ticks()
    rep_round += 1




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count_sec):
    """counting down using window.after() + Recursion in fun"""

    ## reform countdown into '00:00' format
    min = math.floor(count_sec / 60)  ## 将x向下舍入到最接近的整数
    sec = count_sec % 60
    if min < 10:
        min = f'0{min}'
    if sec < 10:
        sec = f'0{sec}'

    ## loop_1: count_down
    canvas.itemconfig(count_display, text=(f'{min}:{sec}'))

    if count_sec > 0:
        global timer
        timer = window.after(1000, count_down, count_sec - 1)
        ## 每1000 millisecond, listen and run the fun once
        ## The use of global timer: 为了window.after.cancel() in fun Reset

    ## loop 2: rounds
    else:
        start_timer()
        ## 每当一轮count_down=0 (结束)，触发第二轮
        ## 这里也放在start_timer()里：using window.after(start_timer)
        ## -- TEST发现：如放start_timer()里触发每次会开头少一秒(timer won't hit 5, but starts from 4)；放在这里触发，每次结尾会少一秒（timer won't hit 0, but starts a new round)

def button_start_click():
    start_timer()

def button_reset_click():
    reset_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('pomoroto')
window.config(padx=100, pady=50,bg=YELLOW)## window to be bigger than the canvas, when every time resizing itself to fit the pic.

canvas = Canvas(width=200, height=240, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato)  ## from upper-left corner, x=100, y=112 -- x=canvas.width/2; y=height/2
count_display = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(column=1, row=1)



label_timer = Label(text='Timer',font=(FONT_NAME, 40, 'bold'),fg=GREEN, bg=YELLOW, justify='center')
label_timer.grid(column=1, row=0)

label_tick = Label(fg=GREEN, bg=YELLOW)
label_tick.grid(column=1, row=3)

button_start=Button(text='Start',bg='white', highlightthickness=0, command=button_start_click)
button_start.grid(column=0, row=2)

button_reset=Button(text='Reset',bg='white', highlightthickness=0, command=button_reset_click)
button_reset.grid(column=2, row=2)

def check_ticks():
    global rep_round
    if rep_round > 8:
        round = rep_round % 8
    else:
        round = rep_round
    tick_amount = int(round / 2)
    label_tick.config(text='✔' * tick_amount, font=(FONT_NAME, 20, 'bold'))

    ## text='✔' * tick_amount
    ## tick += '✔'  -- 二者相等


window.mainloop()
