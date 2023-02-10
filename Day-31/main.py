from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash card app")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file = r"C:\Users\Leader Maharshi\Desktop\python_100_days\Day-31\images\card_front.png")
canvas.create_image(400, 263, image=card_front_image)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


#buttons
cross_image = PhotoImage(r'C:\Users\Leader Maharshi\Desktop\python_100_days\Day-31\images\wrong.png')
unknown_button = Button(image=cross_image)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(r'C:\Users\Leader Maharshi\Desktop\python_100_days\Day-31\images\right.png')
known_button = Button(image=check_image)
known_button.grid(column=1, row=1)

window.mainloop()