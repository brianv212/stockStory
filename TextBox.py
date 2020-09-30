import tkinter as tk

def text_box():
    root = tk.Tk()
    root.title("Begin Your Stock Story")

    tk.Label(root, text = "Provide us a story: ").grid(row = 0)

    input = tk.Entry(root, width = 100)
    input.grid(row = 0, column = 1)


    tk.Button(root,
              text = 'Enter',
              command = root.quit).grid(row = 3,
                                        column = 1)
    root.mainloop()
    return input.get()
