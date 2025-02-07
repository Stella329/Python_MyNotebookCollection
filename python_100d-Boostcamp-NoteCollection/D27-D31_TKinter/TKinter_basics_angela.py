#TKINTER COOK BOOK

# window_obj = tkinter.Tk()
# label_obj = tkinter.Label()
# window.mainloop()

# Tkinter module is ported from another language (non-pythonic moduel) call Tk
# Tk has a very different syntax from Python
# So to work Tk in Python, Tk commands are turned into **kwargs/**kw



from tkinter import * 

# create a window
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300) ## the minimum size of the window



# Label object
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

my_label = tkinter.Label(text='I Am a Label', font=('Arial',24,'bold'))
my_label.pack()    ##display the Label

## my_label.pack(side='top', expand = 0)
## The packer is a geometry-management mechanisms -- a way to layout the components you're building

## how to change/update component's properties
## 3 ways
## 1. using keywords arguments: my_label = tkinter.Label(text='I Am a Label', font=('Arial',24,'bold'))
## 2. after object created, treating the option name like a dict index
## 3. label.config(fg='red', bg='blue')


# Button
##create a button event: fun
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

##i.e.
button = tkinter.Button(text='Click Me', command=button_clicked)  ##command = name_of_fun, not calling the fun()
button.pack()



# Entries: input box

entry = Entry(width=30, justify='center')
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

## i.e. 
inputbox = tkinter.Entry(width = 10)
inputbox.pack()
## input.get(): return the Entry as string
##NB!! the only way to get that input text, is to use a widget to call a function!! --i.e. with a button: def click_to_show()

## END
## The tab_id can be either an index value or it can be string literal like "end", which will append it to the end.
        ## tk.get(): The function get on a text widget requires two values: a starting position and an ending position.




# Text
text = Text(height=5, width=30)

#Puts cursor in textbox.
text.focus()

#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")

# 1.0 = Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()




# Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()



# Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()



# Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())

#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()  #Class -> obj
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

## IntVar(): a class, tracking the value of the checkbox using 0 and 1 (0 for ON, 1 for OFF) -- we create an object to get hold of the varible



# Radiobutton
def radio_used():
    print(radio_state.get())

#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()



# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)   ## to call/bind the fun above to the listbox
listbox.pack()
window.mainloop()




# Keep the window (at the very end) : using loop
window.mainloop()

## this is equal to the while loop -- this loop is included inside Tkinter
## while True:
##    listening




--------------------------
# TKINTER LAYOUT MANAGER: pack(); place(); grid()

obj.pack(side='left')
## vague position -- too vague

obj.place(x=0, y=0) 
## percise postion, starting from the top left corner -- too specific

obj.grid(column = 0, row = 0)  
## you can divide the screen into any numbers of row and columns you want to 
## starting at the top left: obj.grid(column = 0, row = 0)  

## NB: YOU CANNOT MIX grid and pack in the same program



# ADDING PADDING

window.config(padx=20, pady=20)
## add more space around all 4 edges

label.config(padx=20, pady=20)
## add more space around a widget
