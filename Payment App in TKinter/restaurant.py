from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox


c_operator=''
food_prices = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99]
drinks_prices= [0.25, 0.99, 1.21, 1.54, 1.08, 1.10]
desserts_prices= [1.54, 1.68, 1.32, 1.97, 2.55, 2.14]

def click_btn(num):
    global c_operator
    c_operator= c_operator + num
    calculator_display.delete(0, END)
    calculator_display.insert(END, c_operator)

def clear():
    global c_operator
    c_operator=''
    calculator_display.delete(0, END)

def get_result():
    global c_operator
    result=str(eval(c_operator))
    calculator_display.delete(0, END)
    calculator_display.insert(0, result)
    c_operator=''

def review_check():
    # Dood
    x = 0
    for c in l_food_input:
        if l_food_variables[x].get() == 1:
            l_food_input[x].config(state=NORMAL)
            if l_food_input[x].get()=='0':
                l_food_input[x].delete(0, END)
            l_food_input[x].focus()
        else:
            l_food_input[x].config(state=DISABLED)
            l_food_text[x].set('0')
        x+=1

    # Drinks
    x = 0
    for c in l_drinks_input:
        if l_drinks_variables[x].get() == 1:
            l_drinks_input[x].config(state=NORMAL)
            if l_drinks_input[x].get()=='0':
                l_drinks_input[x].delete(0, END)
            l_drinks_input[x].focus()
        else:
            l_drinks_input[x].config(state=DISABLED)
            l_drinks_text[x].set('0')
        x+=1
    
    # Desserts
    x = 0
    for c in l_desserts_input:
        if l_desserts_variables[x].get() == 1:
            l_desserts_input[x].config(state=NORMAL)
            if l_desserts_input[x].get()=='0':
                l_desserts_input[x].delete(0, END)
            l_desserts_input[x].focus()
        else:
            l_desserts_input[x].config(state=DISABLED)
            l_desserts_text[x].set('0')
        x+=1


def total():
    # Food
    food_subtotal= 0
    p = 0
    for quantity in l_food_text:
        food_subtotal= food_subtotal + (float(quantity.get()) * food_prices[p])
        p+=1

    # Drinks
    drinks_subtotal= 0
    p = 0
    for quantity in l_drinks_text:
        drinks_subtotal= drinks_subtotal + (float(quantity.get()) * drinks_prices[p])
        p+=1

    # Desserts
    desserts_subtotal= 0
    p = 0
    for quantity in l_desserts_text:
        desserts_subtotal= desserts_subtotal + (float(quantity.get()) * desserts_prices[p])
        p+=1
    
    sub_total= food_subtotal + drinks_subtotal + desserts_subtotal
    taxes = sub_total * 0.07
    final_result= sub_total + taxes

    var_food_price.set(f'${round(food_subtotal, 2)}')
    var_drink_price.set(f'${round(drinks_subtotal, 2)}')
    var_desserts_price.set(f'${round(desserts_subtotal, 2)}')
    var_subtotal.set(f'${round(sub_total, 2)}')
    var_taxes.set(f'${round(taxes, 2)}')
    var_total.set(f'${round(final_result, 2)}')


def receipt():

    text_receipt.delete(1.0, END)
    receipt_num= f'N# - {random.randint(1000, 9999)}'
    date = datetime.datetime.now()
    receipt_date = f'{date.day}/{date.month}/{date.year} - {date.hour}:{date.minute}'
    text_receipt.insert(END, f'Data:\t{receipt_num}\t\t{receipt_date}\n')
    text_receipt.insert(END, f'*'*56 + '\n')
    text_receipt.insert(END, 'Items\t\tCant.\tItems Cost\n')
    text_receipt.insert(END, f'-'*67+'\n')

    
    # Food
    x=0
    for food in l_food_text:
        if food.get() != '0':
            text_receipt.insert(END, f'{l_food[x]}\t\t{food.get()}\t${int(food.get()) * food_prices[x]}\n')
        x+=1
    

    # Drinks
    x=0
    for drink in l_drinks_text:
        if drink.get() != '0':
            text_receipt.insert(END, f'{l_drinks[x]}\t\t{drink.get()}\t${int(drink.get()) * drinks_prices[x]}\n')
        x+=1
    

    # Desserts
    x=0
    for dessert in l_desserts_text:
        if dessert.get() != '0':
            text_receipt.insert(END, f'{l_desserts[x]}\t\t{dessert.get()}\t${int(dessert.get()) * desserts_prices[x]}\n')
        x+=1
    
    # Present Resume
    text_receipt.insert(END, f'-'*67+'\n')
    text_receipt.insert(END, f'Food Prices: \t\t\t{var_food_price.get()}\n')
    text_receipt.insert(END, f'Drinks Prices: \t\t\t{var_drink_price.get()}\n')
    text_receipt.insert(END, f'Desserts Prices: \t\t\t{var_desserts_price.get()}\n')

    text_receipt.insert(END, f'-'*67+'\n')

    text_receipt.insert(END, f'Sub-Total: \t\t\t{var_subtotal.get()}\n')
    text_receipt.insert(END, f'Taxes: \t\t\t{var_taxes.get()}\n')
    text_receipt.insert(END, f'Total: \t\t\t{var_total.get()}\n')
    text_receipt.insert(END, f'-'*67+'\n')
    text_receipt.insert(END, 'Come Back Soon')


def save():

    receipt_info= text_receipt.get(1.0, END)
    file= filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    file.write(receipt_info)
    file.close()
    messagebox.showinfo('Information', 'Your receipt has been saved')


def reset():

    text_receipt.delete(0.1, END)

    for text in l_food_text:
        text.set('0')
    for drink in l_drinks_text:
        drink.set('0')
    for dessert in l_desserts_text:
        dessert.set('0')
    
    for input in l_food_input:
        input.config(state=DISABLED)
    for input in l_drinks_input:
        input.config(state=DISABLED)
    for input in l_desserts_input:
        input.config(state=DISABLED)
    
    for v in l_food_variables:
        v.set(0)
    for v in l_drinks_variables:
        v.set(0)
    for v in l_desserts_variables:
        v.set(0)
    
    var_food_price.set('')
    var_drink_price.set('')
    var_desserts_price.set('')
    var_subtotal.set('')
    var_taxes.set('')
    var_total.set('')

# Initiate tkinter
app = Tk()

# App Size
app.geometry('1180x630+0+0')

# Avoid full size window
app.resizable(0, 0)

# General configuration
app.title('My Restaurant - Payment System')
app.config(bg='#F5EFC9')


# Top panel
top_panel = Frame(app,width=1180, height=100, bd=1, relief=RAISED)
top_panel.pack(side=TOP)

title_tag=Label(top_panel, text='Payment System', fg='brown', font=('Dosis', 58), bg='#F5EFC9', width=27)
title_tag.grid(row=0, column=0)
title_tag.place(relx=0.5, rely=0.5, anchor=CENTER)


############# Left-Side Panel #############
left_panel = Frame(app, bd=1, relief=FLAT)
left_panel.pack(side=LEFT)

# Prices Panel
prices_panel = Frame(left_panel, bd=1, relief=FLAT, bg='azure4', padx=55)
prices_panel.pack(side=BOTTOM)

# Food Panel
food_panel = LabelFrame(left_panel, text='Food', font=('Dosis', 19, 'bold') , bd=1, relief=FLAT, fg='brown')
food_panel.pack(side=LEFT)

# Drinks Panel
drinks_panel = LabelFrame(left_panel, text='Drinks', font=('Dosis', 19, 'bold'),bd=1, relief=FLAT, fg='brown')
drinks_panel.pack(side=LEFT)

# Desserts Panel
desserts_panel = LabelFrame(left_panel, text='Desserts', font=('Dosis', 19, 'bold'),bd=1, relief=FLAT, fg='brown')
desserts_panel.pack(side=LEFT)


################ Right-Side Panel #############
right_panel = Frame(app, bd=1, relief= FLAT)
right_panel.pack(side=RIGHT)

# Calculator panel
calculator_panel = Frame(right_panel, bd=1, relief=FLAT, bg='#F5EFC9')
calculator_panel.pack()

# Receipt panel
receipt_panel = Frame(right_panel, bd=1, relief=FLAT, bg='#F5EFC9')
receipt_panel.pack()

# Buttons panel
buttons_panel = Frame(right_panel, bd=1, relief=FLAT, bg='#F5EFC9')
buttons_panel.pack()


# Products' Lists
l_food = ['Chicken', 'Pizza', 'Burger', 'Salmon', 'Pasta', 'Kebab']
l_drinks = ['Water', 'Soda', 'Juice', 'Tea', 'Beer', 'Wine']
l_desserts=['Ice Cream', 'Cake', 'Brownies', 'Mousse', 'Donuts', 'Churros']



# Generate food items
l_food_variables=[]
l_food_input= [] # for input box
l_food_text = [] # to save info of input
counter= 0

for food in l_food:

    # Create CheckButton
    l_food_variables.append('')
    l_food_variables[counter] = IntVar()
    food = Checkbutton(food_panel,
                       text=food.title(),
                       font=('Dosis', 19, 'bold'),
                       onvalue=1, offvalue=0,
                       variable=l_food_variables[counter],
                       command=review_check)
    food.grid(row=counter, column=0, sticky=W)

    # Create input box
    l_food_input.append('')
    l_food_text.append('')
    l_food_text[counter]=StringVar()
    l_food_text[counter].set('0')
    l_food_input[counter] = Entry (food_panel,
                                   font=('Dosis', 18, 'bold'),
                                   bd=1,
                                   width=6,
                                   state=DISABLED,
                                   textvariable= l_food_text[counter])
    l_food_input[counter].grid(row=counter, column=1)

    counter+=1



# Generate drinks items
l_drinks_variables=[]
l_drinks_input= [] # for input box
l_drinks_text = [] # to save info of input
counter= 0

for drink in l_drinks:

    # Create CheckButton
    l_drinks_variables.append('')
    l_drinks_variables[counter] = IntVar()
    drink = Checkbutton(drinks_panel,
                        text=drink.title(),
                        font=('Dosis', 19, 'bold'),
                        onvalue=1,
                        offvalue=0,
                        variable=l_drinks_variables[counter],
                        command=review_check)
    drink.grid(row=counter, column=0, sticky=W)

     # Create input box
    l_drinks_input.append('')
    l_drinks_text.append('')
    l_drinks_text[counter]=StringVar()
    l_drinks_text[counter].set('0')
    l_drinks_input[counter] = Entry (drinks_panel,
                                   font=('Dosis', 18, 'bold'),
                                   bd=1,
                                   width=6,
                                   state=DISABLED,
                                   textvariable= l_drinks_text[counter])
    l_drinks_input[counter].grid(row=counter, column=1)

    counter+=1



# Generate desserts items
l_desserts_variables=[]
l_desserts_input= [] # for input box
l_desserts_text = [] # to save info of input
counter= 0

for dessert in l_desserts:

    # Create CheckButton
    l_desserts_variables.append('')
    l_desserts_variables[counter] = IntVar()
    dessert = Checkbutton(desserts_panel,
                          text=dessert.title(),
                          font=('Dosis', 19, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=l_desserts_variables[counter],
                          command=review_check)
    dessert.grid(row=counter, column=0, sticky=W)

     # Create input box
    l_desserts_input.append('')
    l_desserts_text.append('')
    l_desserts_text[counter]=StringVar()
    l_desserts_text[counter].set('0')
    l_desserts_input[counter] = Entry (desserts_panel,
                                   font=('Dosis', 18, 'bold'),
                                   bd=1,
                                   width=6,
                                   state=DISABLED,
                                   textvariable= l_desserts_text[counter])
    l_desserts_input[counter].grid(row=counter, column=1)

    counter+=1


# Variables
var_food_price=StringVar()
var_drink_price = StringVar()
var_desserts_price = StringVar()
var_subtotal = StringVar()
var_taxes = StringVar()
var_total = StringVar()


# Tags and inputs for FOOD prices
tag_food_prices= Label(prices_panel,
                      text='Food Total',
                      font=('Dosis', 12, 'bold'),
                      bg='azure4',
                      fg='white')

tag_food_prices.grid(row=0, column=0, padx=41)

text_food_price=Entry(prices_panel,
                      font=('Dosis', 12, 'bold'),
                      bd=1,
                      width=10,
                      state='readonly',
                      textvariable=var_food_price)

text_food_price.grid(row=0, column=1, padx=41)



# Tags and inputs for DRINKS prices
tag_drinks_prices= Label(prices_panel,
                      text='Drinks Total',
                      font=('Dosis', 12, 'bold'),
                      bg='azure4',
                      fg='white')

tag_drinks_prices.grid(row=1, column=0)

text_drink_price=Entry(prices_panel,
                      font=('Dosis', 12, 'bold'),
                      bd=1,
                      width=10,
                      state='readonly',
                      textvariable=var_drink_price)

text_drink_price.grid(row=1, column=1, padx=41)



# Tags and inputs for DESSERTS prices
tag_desserts_prices= Label(prices_panel,
                      text='Desserts Cost',
                      font=('Dosis', 12, 'bold'),
                      bg='azure4',
                      fg='white')

tag_desserts_prices.grid(row=2, column=0)

text_desserts_price=Entry(prices_panel,
                      font=('Dosis', 12, 'bold'),
                      bd=1,
                      width=10,
                      state='readonly',
                      textvariable=var_desserts_price)

text_desserts_price.grid(row=2, column=1, padx=41)


# Tags and inputs for SUBTOTAL
tag_subtotal= Label(prices_panel,
                      text='SubTotal',
                      font=('Dosis', 12, 'bold'),
                      bg='azure4',
                      fg='white')

tag_subtotal.grid(row=0, column=2)

text_subtotal=Entry(prices_panel,
                      font=('Dosis', 12, 'bold'),
                      bd=1,
                      width=10,
                      state='readonly',
                      textvariable=var_subtotal)

text_subtotal.grid(row=0, column=3, padx=41)


# Tags and inputs for TAXES
tag_taxes= Label(prices_panel,
                      text='Taxes',
                      font=('Dosis', 12, 'bold'),
                      bg='azure4',
                      fg='white')

tag_taxes.grid(row=1, column=2)

text_taxes=Entry(prices_panel,
                      font=('Dosis', 12, 'bold'),
                      bd=1,
                      width=10,
                      state='readonly',
                      textvariable=var_taxes)

text_taxes.grid(row=1, column=3, padx=41)



# Tags and inputs for TOTAL
tag_total= Label(prices_panel,
                      text='Total',
                      font=('Dosis', 12, 'bold'),
                      bg='azure4',
                      fg='white')

tag_total.grid(row=2, column=2)

text_total=Entry(prices_panel,
                      font=('Dosis', 12, 'bold'),
                      bd=1,
                      width=10,
                      state='readonly',
                      textvariable=var_total)

text_total.grid(row=2, column=3, padx=41)


# Buttons
l_buttons=['total', 'receipt', 'save', 'reset']
l_created_buttons=[]
columns=0

for btn in l_buttons:
    btn= Button(buttons_panel,
                text=btn.title(),
                font=('Dosis', 14, 'bold'),
                fg= 'white',
                bg='azure4',
                bd=1,
                width=9)
    l_created_buttons.append(btn)
    btn.grid(row=0, column=columns)  
    columns += 1       

l_created_buttons[0].config(command=total)
l_created_buttons[1].config(command=receipt)
l_created_buttons[2].config(command=save)
l_created_buttons[3].config(command=reset)


# Receipt area
text_receipt= Text(receipt_panel,
                   font=('Dosis', 12, 'bold'),
                   bd=1,
                   width=50,
                   height=10)
text_receipt.grid(row=0, column=0)
     

# Calculator
calculator_display= Entry(calculator_panel,
                          font=('Dosis', 16, 'bold'),
                          width=37,
                          bd=1)
calculator_display.grid(row=0, column=0, columnspan=4)


l_btn_calculator=['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'x', '=', 'C', '0', '/']
l_save_btns=[]

r=1 # row
col=0 # column
for btn in l_btn_calculator:
    btn=Button(calculator_panel,
               text=btn.title(),
               font=('Dosis', 16, 'bold'),
               fg= 'white',
               bg='azure4',
               bd=1,
               width=8)
    btn.grid(row=r, column=col)

    l_save_btns.append(btn)
    if col==3:
        r+=1
    col+=1
    if col==4:
        col=0

# Button configuration
l_save_btns[0].config(command=lambda:click_btn('7'))
l_save_btns[1].config(command=lambda:click_btn('8'))
l_save_btns[2].config(command=lambda:click_btn('9'))
l_save_btns[3].config(command=lambda:click_btn('+'))
l_save_btns[4].config(command=lambda:click_btn('4'))
l_save_btns[5].config(command=lambda:click_btn('5'))
l_save_btns[6].config(command=lambda:click_btn('6'))
l_save_btns[7].config(command=lambda:click_btn('-'))
l_save_btns[8].config(command=lambda:click_btn('1'))
l_save_btns[9].config(command=lambda:click_btn('2'))
l_save_btns[10].config(command=lambda:click_btn('3'))
l_save_btns[11].config(command=lambda:click_btn('*'))
l_save_btns[12].config(command=get_result)
l_save_btns[13].config(command=clear)
l_save_btns[14].config(command=lambda:click_btn('0'))
l_save_btns[15].config(command=lambda:click_btn('/'))




app.mainloop()
