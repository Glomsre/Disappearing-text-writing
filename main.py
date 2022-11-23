from tkinter import *
import time

t = 10

def start_timer():
    global t

    while t:
        time.sleep(1)
        t -= 1
        label_time.config(text=f'Time: {t}')
        window.update()
        if t == 0:
            text_window.delete('1.0', END)
            label_time.config(text='')
            label_info.config(text='Timeout! Press RESTART ->')
            window.update()


def typing(event):
    global t
    label_info.config(text='')
    t = 10


def restart():
    global t
    label_info.config(text='')
    text_window.delete('1.0', END)
    t = 10
    start_timer()


window = Tk()
window.title("Disappearing Text Writing App")
window.config(padx=10, pady=10)

label_title = Label(font=('Helvetica', 20), text="If you stop writing, all your progress will be lost")
label_title.grid(column=1, row=0, columnspan=7)

label_time = Label(text=f'Time: {t}')
label_time.grid(column=1, row=1, pady=10)

label_info = Label(text='')
label_info.grid(column=2, row=1, columnspan=5, pady=10)

button_restart = Button(window, text="Restart", command=restart)
button_restart.grid(row=1, column=7)

text_window = Text(window, font=('Helvetica', 15), height=25, width=100)
text_window.bind("<KeyRelease>", typing)
text_window.grid(column=1, row=2, columnspan=8, pady=10)

start_timer()

window.mainloop()
