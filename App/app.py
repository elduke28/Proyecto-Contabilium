from tkinter import *
from funciones import leer_archivos, ejecutar


root = Tk()
root.title("ETL - Contabilium")
root.configure(bg='#333333')
root.iconbitmap('icon.ico')

app_width = 350
app_height = 300
screen_widht = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_widht/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)
root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

frame = Frame(bg='#333333')

# Creamos los widgets
label = Label(frame, text = "ETL", font=('Arial', 25), bg='#333333', fg='#FF2569')
label_open = Label(frame, text = "Abrir archivo:", font=('Arial', 14), bg='#333333', fg='#FF2569')
open_button = Button(frame, text="Open", bg="#00C7AF", fg="white", height="2", width="10", relief=RAISED, 
		    borderwidth=3, font=('Arial', 14), command=leer_archivos)
label_excecute = Label(frame, text = "Ejecutar:", font=('Arial', 14), bg='#333333', fg='#FF2569')
excecute_button = Button(frame, text = "Run",bg="#00C7AF", fg="white", height="2", width="10", relief=RAISED, 
			borderwidth=3, font=('Arial', 14), command = ejecutar)


# Posicionamos los widgets
label.grid(row=0, column=0, columnspan=2, sticky='news', pady=25)
label_open.grid(row=1, column=0, padx=10)
open_button.grid(row=1, column=1, padx= 2, pady=10)
label_excecute.grid(row=2, column=0, padx=10)
excecute_button.grid(row=2, column=1, pady=10)
frame.pack()

root.mainloop()