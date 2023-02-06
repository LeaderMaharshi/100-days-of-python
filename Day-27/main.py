from tkinter import *

window = Tk()
window.title("My first GUI window")
window.minsize(width=500, height=300)

#label

my_label = Label(text="I'm a Label", font=("Arial",24,"bold"))
my_label.pack()

my_label["text"] = "New text"
my_label.config(text = "New text")

#button

def button_clicked():
    print("HEY MAN")
    new_text = input.get()
    my_label.config(text = new_text)


button = Button(text = "click me", command=button_clicked)
button.pack()

#Entry

input = Entry()
input.pack()
input.get()


window.mainloop()