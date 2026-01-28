import tkinter as tk
import keyboard

# functie care raspunde la mesaj
def raspunde(event=None):
    mesaj = entry.get().lower()
    entry.delete(0, tk.END)

    chat.config(state=tk.NORMAL)
    chat.insert(tk.END, f"Tu: {mesaj}\n", "user")

    if mesaj == "salut":
        raspuns = "Salut! Sunt chatbotul tau."
    elif mesaj == "ce faci":
        raspuns = "Astept comenzi."
    elif mesaj == "cum te cheama":
        raspuns = "Ma numesc Parzy."
    elif mesaj == "multumesc":
        raspuns = "Cu placere!"
    elif mesaj == "play":
        keyboard.send("play/pause media")
        raspuns = "Play / Pause Spotify."
    elif mesaj == "pause":
        keyboard.send("play/pause media")
        raspuns = "Pause Spotify."
    elif mesaj == "next":
        keyboard.send("next track")
        raspuns = "Urmatoarea piesa."
    elif mesaj == "previous":
        keyboard.send("previous track")
        raspuns = "Piesa anterioara."
    elif mesaj == "volum up":
        keyboard.send("volume up")
        raspuns = "Volum mai mare."
    elif mesaj == "volum down":
        keyboard.send("volume down")
        raspuns = "Volum mai mic."
    elif mesaj == "exit":
        raspuns = "La revedere!"
        chat.insert(tk.END, f"Bot: {raspuns}\n", "bot")
        root.after(1000, root.destroy)
        return
    else:
        raspuns = "Nu inteleg comanda."

    chat.insert(tk.END, f"Bot: {raspuns}\n", "bot")
    chat.config(state=tk.DISABLED)
    chat.yview(tk.END)


# fereastra principala
root = tk.Tk()
root.title("Chatbot Dark Mode")

# culori
bg_color = "#121212"
chat_bg = "#1e1e1e"
fg_color = "#ffffff"
accent_color = "#00ffff"

root.configure(bg=bg_color)

# zona chat
chat = tk.Text(root, height=15, width=50, bg=chat_bg, fg=fg_color,font=("Consolas", 12), bd=0, padx=10, pady=10)
chat.pack(padx=15, pady=15)
chat.config(state=tk.DISABLED)

chat.tag_config("user", foreground=accent_color, font=("Consolas", 12, "bold"))
chat.tag_config("bot", foreground=fg_color)

# zona input
frame = tk.Frame(root, bg=bg_color)
frame.pack(padx=15, pady=(0, 15))

entry = tk.Entry(frame, width=40, bg="#1e1e1e", fg=fg_color,insertbackground=fg_color, font=("Consolas", 12), bd=2, relief=tk.FLAT)
entry.pack(side=tk.LEFT, ipady=6)
entry.focus()
entry.bind("<Return>", raspunde)

buton = tk.Button(frame, text="Trimite", command=raspunde,
                  bg=accent_color, fg=bg_color,
                  font=("Consolas", 12, "bold"),
                  activebackground="#00cccc", bd=0, padx=10, pady=5)
buton.pack(side=tk.RIGHT, padx=(5, 0))

root.mainloop()
