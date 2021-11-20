from tkinter import *
root = Tk()
root.title("Chatbot")
def send():
    send = "You -> "+e.get()
    txt.insert(END, "n"+send)
    user = e.get().lower()
    if(user == "hello"):
        txt.insert(END, "n" + "Bot -> Hi")
    elif(user == "hi" or user == "hii" or user == "hi"):
        txt.insert(END, "n" + "Bot -> Hello")
    elif(e.get() == "how are you"):
        txt.insert(END, "n" + "Bot -> fine! and you")
    elif(user == "fine" or user == "i am good" or user == "i am doing good"):
        txt.insert(END, "n" + "Bot -> Great! how can I help you.")
    elif (user == "What is your name" or user == "your name" or user == "i didn't recognice you"):
        txt.insert(END, "n" + "Bot -> my name is taj. and your's")
    elif (user == "where you live" or user == "where are you from" or user == "where do you belong from"):
        txt.insert(END, "n" + "Bot -> in your ram")
    elif (user == "help" or user == "help me" or user == "do me fevour"):
        txt.insert(END, "n" + "Bot -> Tell me, what can I do for you?")
    elif (
            user == "find me best shampoo for men" or user == "best shampoo" or user == "men's shampoo" or user == "shampoo"):
        txt.insert(END, "n" + "Bot -> i don't know buddy. find on your own")
    elif (user == "what is your fevourite car" or user == "fevourite car" or user == "beautiful car"):
        txt.insert(END, "n" + "Bot -> mustang")
    elif(user == "car model" or user == "fevourite car modle" or user == "fevourite car of mustang"):
        txt.insert(END, "n" + "Bot -> 1969 Ford Mustaang mach 1")

    else:
        txt.insert(END, "n" + "Bot -> Sorry! I dind't got you")
    e.delete(0, END)
txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
e.grid(row=1, column=0)
send = Button(root, text="Send", command=send).grid(row=1, column=1)
root.mainloop()