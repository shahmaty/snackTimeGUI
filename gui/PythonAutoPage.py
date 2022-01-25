import tkinter as tk

# Static Configuration Variables
HEIGHT = 700
WIDTH = 800

# Other Variables
champPool = []


# Button Functions
def add_to_pool(entry):
    champPool.append(entry)
    print("Added '", entry, "' to champ pool: ", champPool)
    label['text'] = champPool
    enterChamp.delete(0, 'end')


root = tk.Tk()
root.title("SnackTime PRE-RELEASE")
root.configure(background="#1B2839")
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='../Images/backgrounds/guiMainBg.png'))

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, background="#1B2839", highlightthickness=0)
canvas.pack()

header = tk.Frame(root, background="#1B2839")
header.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

enterChampText = tk.Label(header, text="Add Champions:", background="#1B2839", foreground="#FFFFFF")
enterChampText.pack(side='left', fill='both', padx=10)

frame = tk.Frame(root, background="#1B2839")
frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6)

label = tk.Label(frame, background="#1B2839", foreground="#7D8790")
label.pack(side='left')

enterChamp = tk.Entry(header, background="#1B2839", foreground="#FFFFFF")
enterChamp.bind("<Return>", lambda x: add_to_pool(enterChamp.get()))
enterChamp.pack(side='left', fill='both', expand=True, padx=10)

findCounterButton = tk.Button(header, background="#F55755", foreground="#FFFFFF", border=0, text="Add to Pool", command=lambda: add_to_pool(enterChamp.get()))
findCounterButton.pack(side='right', fill='both', padx=10)


root.mainloop()