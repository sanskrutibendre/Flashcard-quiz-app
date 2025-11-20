import tkinter as tk

# ---------------- Flashcard Data ---------------- #
flashcards = [
    {"question": "Capital of France?", "answer": "Paris"},
    {"question": "2 + 2 = ?", "answer": "4"},
    {"question": "Largest planet?", "answer": "Jupiter"}
]

# ---------------- App Logic ---------------- #
current_index = 0
showing_answer = False

def update_card():
    global showing_answer
    showing_answer = False
    card_text.set(flashcards[current_index]["question"])
    progress_text.set(f"{current_index + 1} / {len(flashcards)}")

def flip_card():
    global showing_answer
    if showing_answer:
        card_text.set(flashcards[current_index]["question"])
    else:
        card_text.set(flashcards[current_index]["answer"])
    showing_answer = not showing_answer

def next_card():
    global current_index
    current_index = (current_index + 1) % len(flashcards)
    update_card()

def prev_card():
    global current_index
    current_index = (current_index - 1) % len(flashcards)
    update_card()


# ---------------- UI Setup ---------------- #
root = tk.Tk()
root.title("Flashcard Quiz")
root.geometry("400x300")
root.configure(bg="#f5f5f5")

card_text = tk.StringVar()
progress_text = tk.StringVar()

# Card area
card_frame = tk.Frame(root, bg="white", width=300, height=150, relief="groove", borderwidth=2)
card_frame.pack(pady=20)

card_label = tk.Label(card_frame, textvariable=card_text, font=("Arial", 20), bg="white", wraplength=250)
card_label.place(relx=0.5, rely=0.5, anchor="center")

# Click to flip
card_frame.bind("<Button-1>", lambda e: flip_card())
card_label.bind("<Button-1>", lambda e: flip_card())

# Navigation buttons
btn_frame = tk.Frame(root, bg="#f5f5f5")
btn_frame.pack()

prev_btn = tk.Button(btn_frame, text="Previous", command=prev_card)
prev_btn.grid(row=0, column=0, padx=10)

progress_label = tk.Label(btn_frame, textvariable=progress_text, bg="#f5f5f5")
progress_label.grid(row=0, column=1)

next_btn = tk.Button(btn_frame, text="Next", command=next_card)
next_btn.grid(row=0, column=2, padx=10)

# Initialize first card
update_card()

root.mainloop()
