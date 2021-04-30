# import all the required packages
import tkinter as tkt
import tkinter.messagebox
from datetime import date
from os import path
from tkinter import *
from tkinter import ttk

import regex as reg
import requests
import pytest

# This url has the rates of the currencies of other countries with respect to India
url = 'https://api.exchangerate-api.com/v4/latest/INR'
data = requests.get(url).json()
dictionary_check = data['rates']


# To write the daily rates to a file
def writeExRatesToFile():
    today = date.today()
    txt_name = str(today) + ".txt"
    file_txt = open(txt_name, "w")
    # Reading from file
    for i in data['rates']:
        file_txt.write("\n %s : %f" % (i, data["rates"][i]))

    file_txt.close()


# To check if the file exists or not (For unit testing using pytest)
def check_file(txt_name):
    return path.exists(txt_name)


# To check if the dictionary of rates is empty or not (For unit testing using pytest)
def rates_exists(rates):
    if len(rates) == 0:
        return False
    else:
        return True


class currencyConverter:
    def __init__(self, urls):
        self.url = urls
        self.cur = data['rates']

    def convert(self, from_the_currency, to_the_currency, amount_calculated):
        if from_the_currency != 'INR':
            amount_calculated = amount_calculated / self.cur[from_the_currency]

        amount_calculated = round(amount_calculated * self.cur[to_the_currency], 2)
        return amount_calculated


# This method handles that only numbers should be entered in the boxes
# action tells about whether the box is empty or not
def EnterOnlyNumbers(action, s):
    print('action ='+str(action))
    regex = reg.compile(r"[0-9,]*?(\.)?[0-9,]*$")
    res = regex.match(s)
    return s == "" or (s.count('.') <= 1 and res is not None)


class Gui(tkt.Tk):

    def __init__(self, conv):
        tkt.Tk.__init__(self)
        self.my_converter = conv
        self.geometry("450x500")
        self.configure(background='pink')
        self.title('My Currency Converter')

        # Creating all the required labels
        self.intro_label_of_gui = Label(self, text='MY CURRENCY CONVERTER', fg='green', relief=tkt.SUNKEN,
                                        borderwidth=2)
        self.intro_label_of_gui.config(font=('Times', 16, 'bold'))
        self.line_1 = Label(self, text='Select the country you want to convert your currency to', relief=tkt.FLAT,
                            borderwidth=0)
        self.lines_2 = Label(self, text='Please enter the amount you want to convert', relief=tkt.FLAT, borderwidth=0)
        self.lines_3 = Label(self, text='The converted amount ', relief=tkt.FLAT, borderwidth=0)

        self.intro_label_of_gui.place(x=30, y=5)
        self.line_1.place(x=40, y=70)
        self.lines_2.place(x=70, y=145)
        self.lines_3.place(x=150, y=300)

        # Entry box for the rates
        valid = (self.register(EnterOnlyNumbers), '%d', '%P')
        self.amount_field_entry = Entry(self, bd=3, relief=tkt.RIDGE, bg='light blue', justify=tkt.CENTER,
                                        validate='key', validatecommand=valid)
        self.converted_amount_field_label = Label(self, fg='black', bg='light green', relief=tkt.SUNKEN,
                                                  justify=tkt.CENTER, width=20, borderwidth=3)

        # dropdown for choosing the country currency
        self.from_variable_of_currency = StringVar(self)
        # Making india as the default or base currency for user
        self.from_variable_of_currency.set("INR")
        self.to_variable_of_currency = StringVar(self)
        # Making united states as the default currency to be converted to
        self.to_variable_of_currency.set("USD")

        font = ("Times", 9, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_variable_of_currency,
                                                   values=list(self.my_converter.cur.keys()), font=font,
                                                   state='readonly', width=15, justify=tkt.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_variable_of_currency,
                                                 values=list(self.my_converter.cur.keys()), font=font,
                                                 state='readonly', width=15, justify=tkt.CENTER)

        # placing the dropdown boxes
        self.from_currency_dropdown.place(x=150, y=115)
        self.amount_field_entry.place(x=135, y=175)
        self.to_currency_dropdown.place(x=150, y=270)
        self.converted_amount_field_label.place(x=135, y=330)

        # Convert button for conversion of currency
        self.convert_to_button = Button(self, text="CONVERT TO DESIRED CURRENCY", fg="black", command=self.enact)
        self.convert_to_button.config(font=('Times', 10, 'bold'))
        self.convert_to_button.place(x=70, y=220)

        # Thank you label
        self.thank_you_label = Label(self, text='THANK YOU VISIT AGAIN', fg='blue')
        self.thank_you_label.place(x=220, y=400, anchor='center')
        self.thank_you_label.config(font=('Times', 14, 'bold'))

        # Exit button
        self.exit_button = Button(self, text='Exit', fg='red', command=self.quit)
        self.exit_button.place(x=200, y=450, anchor='center')

    def enact(self):
        try:
            amt = float(self.amount_field_entry.get())
            f_cur = self.from_variable_of_currency.get()
            t_cur = self.to_variable_of_currency.get()
            amount_after_conversion = self.my_converter.convert(f_cur, t_cur, amt)
            amount_after_conversion = round(amount_after_conversion, 4)
            self.converted_amount_field_label.config(text=str(amount_after_conversion))
        except ValueError:
            def pop():
                tkt.messagebox.showinfo('Oops', 'Please add your currency')

            if len(self.amount_field_entry.get()) == 0:
                pop()


if __name__ == '__main__':
    writeExRatesToFile()
    convert = currencyConverter(url)

    Gui(convert)
    mainloop()
