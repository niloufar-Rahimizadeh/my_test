import tkinter as tk
from tkinter import ttk

############

def press():
    if n.get() == ' January':
        l1.configure(bg='red')

# Creating tkinter window
window = tk.Tk()
window.title('Combobox')
window.geometry('500x250')


l1 = tk.Label(window, text = "GFG Combobox Widget", 
          background = 'green', foreground ="white", 
          font = ("Times New Roman", 15))
l1.grid(row = 0, column = 1)


ttk.Label(window, text = "Select the Month :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)
  
n = tk.StringVar()
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n)

monthchoosen['values'] = (' January', 
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')

b1 = tk.Button(window, text="Button", command= press)
b1.grid(row=6, column=0, columnspan=2, sticky='we')

monthchoosen.grid(column=1, row=5)
window.mainloop()