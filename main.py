from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT="timer"
current_card = {}
to_learn={}

try:
    data =pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    orginal_data = pandas.read_csv("data/french_words.csv")
    to_learn = orginal_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_word():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)

    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_text, text=current_card["French"],fill="black")
    canvas.itemconfig(card_backgrountd, image=card_front_image)
    flip_timer = window.after(3000, flip_card)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_word()

def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_text, text=current_card["English"],fill="white")
    canvas.itemconfig(card_backgrountd,image=card_back_image)


window = Tk()
window.title("French learning")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,flip_card)

canvas = Canvas(width=800,height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_backgrountd = canvas.create_image(400,263, image=card_front_image)
card_title = canvas.create_text(400,120,text="", font=(FONT,40,"italic"))
card_text = canvas.create_text(400,240,text="", font=(FONT,60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row = 0,columnspan=2)

cross_image=PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0, command=next_word)
unknown_button.grid(column=0,row = 1)

check_image=PhotoImage(file="images/right.png")
know_button = Button(image=check_image,highlightthickness=0, command=is_known)
know_button.grid(column=1,row = 1)
next_word()

window.mainloop()