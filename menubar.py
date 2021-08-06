from tkinter import Toplevel, Button, Tk, Menu

top = Tk()
menubar = Menu(top)
Run = Menu(menubar, tearoff=0)
Run.add_command(label="Run 'menubar' ")
Run.add_command(label="Debug 'menubar'")
Run.add_command(label="Run")
Run.add_command(label="Attach to progress")
Run.add_command(label="Edit configuration")
Run.add_command(label="Stop")
Run.add_command(label="Stop Background Process")
Run.add_command(label="Show Running List")

Run.add_separator()

Run.add_command(label="Exit", command=top.quit)

menubar.add_cascade(label="Run", menu=Run)

top.config(menu=menubar)
top.mainloop()