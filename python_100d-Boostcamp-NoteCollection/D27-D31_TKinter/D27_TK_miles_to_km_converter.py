from tkinter import *

def action():
    mile = entry_box.get()
    km = round(float(mile) * 1.609344 , 2)
    label_3.config(text=f'{km}')


window = Tk()
window.title('Mile to Kilometer Converter')
# window.minsize(width=500, height=300)  --不设定，自适应且居中


entry_box = Entry(width=5, justify='center')  ## input text centered
entry_box.insert(END, string='0')
entry_box.grid(column=1,row=0)

label_1 = Label(text='Miles')
label_1.grid(column=2, row=0)

label_2 = Label(text='equal to')
label_2.grid(column=0, row=1)

label_3 = Label(text='0')
label_3.grid(column=1, row=1)

label_4 = Label(text='Km')
label_4.grid(column=2, row=1)


button = Button(text='Convert', command=action)
button.grid(column=1,row=2)

window.config(padx=20, pady=20)
window.mainloop()
