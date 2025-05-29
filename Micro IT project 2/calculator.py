import tkinter as tk

def click(button_text):
    current = display.get()
    if button_text == "C":
        display.set("")
    elif button_text == "=":
        try:
            result = eval(current)
            display.set(str(result))
        except Exception:
            display.set("Error")
    else:
        display.set(current + button_text)

root = tk.Tk()
root.title("Simple GUI Calculator")

display = tk.StringVar()

# Display Entry (read-only)
entry = tk.Entry(root, textvariable=display, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Buttons Layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Create buttons dynamically
row = 1
col = 0
for b in buttons:
    action = lambda x=b: click(x)
    button = tk.Button(root, text=b, command=action, font=("Arial", 18), bd=5, relief=tk.RAISED)
    button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Make buttons expand evenly
for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(row+1):
    root.rowconfigure(i, weight=1)

root.mainloop()
