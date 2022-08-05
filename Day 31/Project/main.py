import pandas
import tkinter as tki
import random

BACKGROUND_COLOR = "#B1DDC6"
WAIT_TIME = 3000
word = None
french_or_english = "french"


def correct():
    if french_or_english == "french":
        pass
    elif french_or_english == "english":
        global word_pool
        word_pool.remove(word)
        display_word_french(word_pool, dictionary)


def incorrect():
    if french_or_english == "french":
        pass
    elif french_or_english == "english":
        display_word_french(word_pool, dictionary)


def display_word_french(words_left, dictionary):
    global french_or_english
    french_or_english = "french"
    canvas_flash_card.itemconfig(image, image=flash_card_front)
    canvas_flash_card.itemconfig(which_language, text="French")
    global word
    word = random.choice(words_left)
    canvas_flash_card.itemconfig(word_text, text=word)
    window.after(WAIT_TIME, display_word_english, words_left, dictionary, word)


def display_word_english(words_left, dictionary, word):
    global french_or_english
    french_or_english = "english"
    canvas_flash_card.itemconfig(image, image=flash_card_back)
    canvas_flash_card.itemconfig(which_language, text="English")
    english_word = dictionary[word]
    canvas_flash_card.itemconfig(word_text, text=english_word)


frequent_words = pandas.read_csv("data/french_words.csv")
dictionary = {row["French"]: row["English"] for index, row in frequent_words.iterrows()}
word_pool = [french for french in dictionary]

window = tki.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas_flash_card = tki.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_flash_card.grid(row=0, column=0, columnspan=7)

flash_card_front = tki.PhotoImage(file="images/card_front.png")
flash_card_back = tki.PhotoImage(file="images/card_back.png")
image = canvas_flash_card.create_image(400, 263, image=flash_card_front)

which_language = canvas_flash_card.create_text(400, 150, text="", fill="black", font=("Arial", 25, "italic"))
word_text = canvas_flash_card.create_text(400, 250, text="", fill="black", font=("Arial", 30, "bold"))

incorrect_image = tki.PhotoImage(file="images/wrong.png")
incorrect_button = tki.Button(width=100, height=100, bg=BACKGROUND_COLOR, command=incorrect, image=incorrect_image)
incorrect_button.grid(row=1, column=1)

correct_image = tki.PhotoImage(file="images/right.png")
correct_button = tki.Button(bg=BACKGROUND_COLOR, command=correct, image=correct_image)
correct_button.grid(row=1, column=5)

window.after(1000, display_word_french, word_pool, dictionary)

window.mainloop()