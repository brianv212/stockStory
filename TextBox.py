import tkinter as tk

def text_box():
    root = tk.Tk()
    root.title("Begin Your Stock Story")
    root.geometry("640x640")


    input = tk.Text(root,width=40,height=20)
    input.pack(pady=20)


    button_frame = tk.Frame(root)
    button_frame.pack()
    
    tk.Button(button_frame,
              text = 'Enter',
              command = root.quit).grid(row = 3,
                                        column = 1)
    root.mainloop()
    return input.get(1.0,tk.END)
