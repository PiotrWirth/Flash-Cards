from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"



try:
    data = pandas.read_csv("words_to_learn.csv")
except:
    original_data = pandas.read_csv("data/cards.csv")
    words = original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")




def generate_card():

    global card, flip_timer
    window.after_cancel(flip_timer)
    card = random.choice(list(words))
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(language_text, text='german',fill="black")
    canvas.itemconfig(card_text, text=card['german'],fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(language_text, text='english',fill="white")
    canvas.itemconfig(card_text, text=card['english'], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_img)


def is_known():
    words.remove(card)
    pandas.DataFrame(words).to_csv('data/words_to_learn.csv', index=False)
    generate_card()



window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=626,
                highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=1, row=0, columnspan=2)

language_text = canvas.create_text(
    400, 150, text="Title", fill='black', font=("Ariel", 40, "italic"))
card_text = canvas.create_text(
    400, 263, text="Word", fill='black', font=("Ariel", 60, "bold"))

right_image = PhotoImage(file="images/right.png")
right_button = Button(
    image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=2, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(
    image=wrong_image, highlightthickness=0, command=generate_card)
wrong_button.grid(column=1, row=1)

generate_card()


window.mainloop()
