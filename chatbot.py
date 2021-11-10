from tkinter import *
from chatbot_rec import pairs
import subprocess
from nltk.chat.util import Chat, reflections
from nltk.corpus import stopwords

root = Tk()
root.config(bg="#C8BFE7")
user_input = StringVar()
user_input.set("Type a message:")
uni_font = ("Caliri Black", 20)
inex = 0

chat = Chat(pairs, reflections)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

l = Listbox(root, font=uni_font, yscrollcommand=scrollbar.set, bg="#880115", fg="white")
l.pack(side="top", fill=BOTH, expand=1, padx=20, pady=20)

def res(t):
    global user_input

    user_input.set("")

    for sym in ["+","-","*","/","%"]:
        anw = f"{t}".lower()
        if sym in anw:
            unwanted = list(stopwords.words('english'))
            unwanted.extend([" ","="])
            for i in unwanted:
                anw = anw.replace(i,"") 
            return eval(anw)

    else:
        anw = chat.respond(f"{t}".lower())
        if anw == None:
            subprocess.Popen([r'C:\Program Files\Google\Chrome\Application\chrome.exe', f"{t}".lower()]).wait()
            return ""

        else:
            return anw

def send(tmp):
    global inex
    l.insert(inex, f"You: {user_input.get()} ")
    inex += 1
    l.insert(inex, f"""Hat: {res(user_input.get())} """)
    inex += 1


l.insert(inex, "Hat: Hey There I am a Chatbot!!! ")
inex += 1

e = Entry(root, width=60, font=uni_font, textvariable=user_input, background="#3F48CC")
e.pack(side="left", expand=1, padx=20, pady=20)
Button(
    root, text="Send", width=10, font=uni_font, command=lambda: send(""), bg="#ED1C24"
).pack(side="left", expand=1, padx=20, pady=20)

root.bind("<Return>", send)
e.bind("<Button-1>", lambda x: user_input.set(""))

root.mainloop()