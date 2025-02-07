#TKINTER COOK BOOK

window_obj = tkinter.TK()
label_obj = tkinter.Label()
window.mainloop()

# NOTE Tkinter module is ported from another language (non-pythonic moduel) call Tk
## Tk has a very different syntax from Python
## So to work Tk in Python, Tk commands are turned into **kwargs/**kw


# keyword attributes
## bg = background color
## fg = foreground color



#-------------UI WINDOW-------------#

from tkinter import * 

# create a window
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300) ## the minimum size of the window -- 非必：如不写则自动适配


# ADDING PADDING

window.config(padx=20, pady=20,bg='color OR #hex_color_code')
## add more space around all 4 edges

label.config(padx=20, pady=20)
## add more space around a widget

## add padding to LAYOUT managers (see below)




#-------------UI CANVAS------------#
# TkDos: https://tkdocs.com/tutorial/canvas.html

canvas = Canvas(witdh=, height=, bg='#hex code', hilightthickness=0 )
pic = PhotoImage(file='name' )
canvas_pic=canvas.create_image (x*args , y*args , image=name/varible)
    # i.e. canvas.create_image(100, 112, image=tomato)  x/y均和图片大小一致
    # from upper-left corner, x=100, y=112 -- x=canvas.width/2; y=height/2
canvas.pack()


# INSERT/DISPLAY an image at a certain position in the canvas
canvas.create_image(50, 10, image=gif1, anchor=NW) 
    ## --Pic's upper-left corner (NW) on the canvas is at x=50 y=10
PhotaImage(file='./file_path/name') 
    ## It is a Class: Read through a file, and to get hold of a particluar image at a particular file location
    ## if not in the same fold, you should provide file path to get there
    ## IMPORTANT: PhotoImage objects should not be created inside a function. Otherwise, it will not work.


# CREATE TEXT
text = canvas.create_text(x, y, text='xx', fill="color", width=250, font=(FONT_NAME, FONT_SIZE, 'bold') ) ##width=position

# CHANGE TEXT ON CANVAS
canvas.itemconfig(item_to_change, text=text_to_change_into)

#去白边
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
# OR
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
    ## highlightthickness=0: get rid of the white frame around the canvas between the window, if changing the bg color of the canvas
    ## 又加入bg去白边


# ADDING PADDING TO CANVAS (SAME TO OTHER WIDGETS)
canvas.pack(padx=0, pady=0)
#OR
canvas.grid(column=1, row=0, padx=0, pady=0)




#------------UI WIDGETS--------------#

# LABEL OBJECT
my_label = tkinter.Label(text='I Am a Label', font=('Arial',24,'bold'), fg='#', bg='#')
my_label.pack()    ##display the Label

## change the text
label = Label(text="This is old text")
label.config(text="This is new text")

    ## NOTE how to change/update component's properties -- 3 ways
    ## 1. using keywords arguments: my_label = tkinter.Label(text='I Am a Label', font=('Arial',24,'bold'))
    ## 2. after object created, treating the option name like a dict index
    ## 3. label.config(fg='red', bg='blue')


# BUTTON
##create a button event: fun
def action():
    print("Do something")

#calls action() when pressed
button = tkinter.Button(text='Click Me非必', width=num非必, image=image_name非必, command=button_clicked，highlightthickness=0)  ##command = name_of_fun, not calling the fun()
button.pack()

##PREVENT the buttons from activated 使button不可再点击
button_name.config(state='disabled')


# NOTE BUTTON其他样式
    ## --按下样式变扁平
    button_name = Button(etc, relief="flat") 

    ## --去白边 -remove all kinds of small borders around a BUTTON
    button_name = tk.Button(image=true_image,highlightthickness=0, borderwidth=0) #--创建时直接写
    #OR
    button_name.config(highlightthickness=0, borderwidth=0)




# ENTRY: input box
entry = Entry(width=30)

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

## about END
## The tab_id can be either an index value or it can be string literal like "end", which will append it to the end.
## tk.get(): The function get on a text widget requires two values: a starting position and an ending position.




# TEXT
text = Text(height=5, width=30)

#Insert some text to begin with.
text.insert(0, "Example of multi-line text entry.")

# 1.0 = Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()




# SPINBOX
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()



# SCALE
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()



# CHECKBUTTON
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())

#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()  #Class -> obj
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

## IntVar(): a class, tracking the value of the checkbox using 0 and 1 (0 for ON, 1 for OFF) -- we create an object to get hold of the varible



# RADIOBUTTON
def radio_used():
    print(radio_state.get())

#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()



# LISTBOX
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)   ## to call/bind the fun above to the listbox
listbox.pack()




# STANDARD DIALOG: pop-up windows

from tkinter import messagebox
messagebox.showinfo(title=' ', message = ' ') #--only yes
messagebox.askxxx( title=' ' , message = f ' These are {input}, yes or no ') #--ask with more buttons
# messagebox is not a class, but another a moduel of code. Check: right click -> go to -> implementation




#--------------LAYOUT MANAGER------------#
# TKINTER LAYOUT MANAGER: pack(); place(); grid()

obj.pack(side='left') 
my_label.pack(side='top', expand = 0) # i.e.
    ## vague position -- too vague
    ## The packer is a geometry-management mechanisms -- a way to layout the components you're building


obj.pack(padx, pady)  # == grid(column, row)
    # add padding to pack()
    ## In pack(padx, pady) method, we add padding on one side (either top/bottom or left/right) of a particular widget

b3= Button(win, text= "Button3", font= ('Poppins bold', 15))
b3.pack(padx=50, pady=50) #Create two buttons; Add padding in x and y axis



obj.place(x=0, y=0) 
    ## percise postion, starting from the top left corner -- too specific



obj.grid(column = 0, row = 0)  
    ## you can divide the screen into any numbers of row and columns you want to 
    ## starting at the top left: obj.grid(column = 0, row = 0)  

frame.grid(row=x, column=y padx=10 pady=10)
    ## add padding to grid()

email_entry.grid(column=1, row=2, columnspan=2, sticky=EW)
    ## span the widget position

## NB: YOU CANNOT MIX grid and pack in the same program



#------------ALIGN INSIDE A WIDGET--------------#
##justify : If the text contains multiple lines, this option controls how the text is justified: CENTER, LEFT, or RIGHT. 



#------------STRETCH THE SIZE--------------#

STRETCH Label (into 2 rows) -- 主要用于inputbox尺寸

b = Label (bg='blue', width = 20, height =20)
b.grid (row=2, column =0)

vs.
b = Label (bg='blue', width = 40, height =20)
b.grid (row=2, column =0)
## 会增加整个column_0的宽度 -- 同样影响column_0中其他Labels相对位置

vs. 
b = Label (bg='blue', width = 20, height =20)
b.grid (row=2, column =0, columnspan = num_of_column_to_span)
## column_0宽度不变，b跨越两个column




#--------------ALIGN WIDGETS------------#

# Align widgets under .grid(sticky=): use the sticky keyword argument

window = tk.Tk()
radio = tk.Radiobutton(window, text="I'm a radio")
radio.grid(column=0, row=0, sticky=tk.N+tk.S+tk.W+tk.E)

## use any combination of the N, S, W and E members of the Tkinter module. 
## This parameter will make your widgets stick to the sides of the cell you have specified

sticky=EW
## 两端对齐（填充）：spans the widget to fill the whole width of the grid column/s.
## 对于button,entry有效；Label和canvas好像不太有效





#------------OTHER MTHODES & ACTIONS for widgets--------------#

# METHODS

get()  #Returns the entry’s current text as a string. 
delete()  #Deletes characters from the widget 
insert (index, 'name')  
    ## Inserts string ‘name’ before the character at the given index.
    ## index: where the curser is 




#Puts a default cursorx

widget.focus()


#TEXT pre-pop-up (i.e. for repetative text): adding starting value

widget.insert (index = where to insert (i.e. 0= start at 0th charater), stirng = what to insert )


#END: a tk constant

## END represent the very last charater 
entry.insert (END, string='add at the end') -- inside the entry


#CLEAR OUT original content
widget.delete (first = start of range, last=None (if none, a single charater is removed)
entry.delete (0, END) ## i.e.







#-------------LOOPS------------#
#GUI program is Event Driven:
    ## Remember in the mainloop() you should not create additional delayed loops e.g. with time.sleep() but instead, use window.after()
    ## 原因： other loops (i.e. while loop) doesn's happen. Because it stops to reach the mainloop        

window.after(time_in_milliseconds, fun=do_something, *args_things)
    # checks every millisecond in looping-through, whether some event happens (i.e. user action like clicking the button)
    ## HOW: by putting a window.after() inside a fun, and call the fun inside window.after()
def FUN (*args):
    if xxx:
    window.after(1000, FUN, *args)
    ## *args = input: things that will be passed as inputs to the fun
    ## FUN = call FUN in itself


## TODO ADD LOOPS: window.after() <注意IMPORTANT出的bug!!>
#i.e. 1
window.after(3000,flip_card)

#i.e. 2 
def count_down(count):
    if count >= 0:
        canvas.itemconfig(count_display, text=count)
        window.after(1000, count_down, count-1)
count_down(5)


## TODO CANCEL THE ADD
window.after_cancel()
    #to cancel the task assigned window_after()

# TODO IMPORTANT:
## timer = window.after()创建后，will keep waiting（一直后台运行，不会自动重启）；因此每次重启需要先cancel再重启
## i.e. METHOD 1
flip_timer = window.after(3000, change_toback)
def tick_change():
    global flip_timer
    window.after_cancel(flip_timer) ##重启timer：每次取消老timer并开启新timer
    change_tofront()
    # LOOP ---------------#
    flip_timer = window.after(3000, change_toback)


# Keep the window (at the very end) : using loop
window.mainloop()
    ## this is equal to the while loop -- this loop is included inside Tkinter
    # while True: listening









