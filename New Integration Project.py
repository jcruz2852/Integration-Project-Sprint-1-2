# John Cruz
# This program will calculate the price of granite/quartz/marble/quartzite countertops for clients.
# "to explain code that isnt obvious"
# "citations"

print('''Greetings, my name is John, i'm a Business Computer Systems major.
I currently work for my dad who owns a countertop business in south West Florida.
I chose this major because one day I hope to run his business when
he decides to retire.''')

print('\n')  # spacing my codes so that i can read them easier in shell.

print("Available Stones:")

print(sep='')
print("Granite", " Quartz", " Marble", " and Quartzite", sep=',', end='!')  # The stones we supply and sell.

print(sep='')  # a line break in shell for clear reading and remember that the top code belongs with the bottom code.

# LEVEL ONE Stone Prices per Sq.Ft:
# granite = 45
# quartz = 50
# marble = 60
# quartzite = 60


# Getting information. (Can give input for all stones or for just one. square feet is required.)
square_feet = int(input("How many square feet does your project have? "))
material_type = input("What material type would you like pricing for? ")

# calculating subtotal
if material_type == "granite":
    material_price = 45
    print("Your subtotal is: $", format(material_price * square_feet, '0.2f'), sep='')
elif material_type == "quartz":
    material_price = 50
    print("Your subtotal is: $", format(material_price * square_feet, '0.2f'), sep='')
elif material_type == "marble":
    material_price = 60
    print("Your subtotal is: $", format(material_price * square_feet, '0.2f'), sep='')
elif material_type == "quartzite":
    material_price = 60
    print("Your subtotal is: $", format(material_price * square_feet, '0.2f'), sep='')

sink = 200
sink_cut = 150
discount = 200
total_extras = 200 + 150 - 200
print("Your total is: $", format(material_price * square_feet + total_extras, '0.2f'), sep='')

# calculating square footage when customer only provides a layout.
# Vanity size is 70in x 22.5in
vanity = int(70 * 22.5)
print("your vanity square footage is: ", vanity / 144)

# calcualting square footage, but leaving out decimals or the remainder.
vanity = int(70 * 22.5)
print("your vanity square footage is: ", vanity // 144)

# calculating backsplash sq/ft
print("your backsplash square footage is: ", (100 * 4) / 144)

# calculating a discount percentage
original_price = float(input("Enter the original cost of the item: "))
sale_price = float(input("Enter the sale price: "))
percent_off = int((original_price - sale_price) / original_price * 100)
print("Original price: $", format(original_price, '.2f'), sep='')
print("Sale price: $", format(sale_price, '.2f'), sep='')
print("Percent off: ", format(percent_off, "d"), "%", sep='')

# this is how you use "**"
print(12 ** 2)

# this is how you us "%"
print(12 % 5)

# this is how you use a concatenate
a = "countertops"
b = "are"
c = "cool"
d = "bro"
print(a + b + c + d)

a = "countertops"
print(a * 50)

# granite is on sale if project is above 50sq/ft
square_feet = int(input("How many square feet does your project have? "))
granite_price = 0
if square_feet >= 50:
    granite_price += 40
    print("Congratulations, you qualify for our sale. Your granite price is: $", format(granite_price, '0.2f'), sep='')
else:
    granite_price += 45
    print("You don't qualify for our sale. Your granite price is: $", format(granite_price, '0.2f'), sep='')

# free sink if your material is granite and you have more than 50 sq/ft
material_type = input("What material type would you like pricing for? ")
square_feet = int(input("How many square feet does your project have? "))
sink = 200
if (material_type == "granite") and (square_feet < 50):
    sink = 0
    print("Congrats you qualify for our base level discount. You get a FREE sink! Sink price is: $", format(sink, '0.2f'), sep='')
if (material_type != "granite") or (square_feet > 50):
    print("You don't qualify for our sink discount. Sink price is: $ ", format(sink, '0.2f'), sep='')

# getting material price using def and if-elif-else. menu.
def material_type1(granite):
    print("You have selected granite.")


def material_type2(quartz):
    print("You have selected quartz.")


def material_type3(marble):
    print("You have selected marble.")


def material_type4(quartzite):
    print("You have selected quartzite.")


while True:
    print("What material would you like to see pricing for?")
    print("Please enter 'done' when done looking.")
    print("Granite")
    print("Quartz")
    print("Marble")
    print("Quartzite")
    material_type = input("Selection: ")

    if material_type == "Granite":
        print("Our granite is $45.00 a square foot.")

    elif material_type == "Quartz":
        print("Our Quartz is $50.00 a square foot.")

    elif material_type == "Marble":
        print("Our Marble is $60.00 a square foot.")

    elif material_type == "Quartzite":
        print("Our Quartzite is $60.00 a square foot.")

    elif material_type == "done":
        break

    else:
        print("Please check your spelling. If spelling is correct then please verify that you've chosen a valid option.")

# random number, vanity give away.
import random


for i in range(1, 1001):
    number_selected = int(input("Please select a number between 0 and 1000:"))
    random_number = random.randint(1, 1001)
    if number_selected != random_number:
        print("Random number:", random_number)
        print("Sorry you are not the winner. Come by our location to receive 5% off of any material.")
        break
    if number_selected == random_number:
        print("Random number:", random_number)
        print("Congratulations you are the winner. Come by our location to receive you FREE vanity.")
        break

import random

def random_max():
    num1 = random.randint(0, 1000)
    num2 = random.randint(0, 1000)
    if num1 > num2:
        print("The random max number is:", num1)
    else:
        print("The random max number is:", num2)
random_max()

#using not
material_type = ['granite', 'quartz', 'marble', 'quartzite']
selection = input("Select the stone that you want pricing for: ")
if selection not in material_type:
    print("We do not have this material type. Please call for more information.")
if selection in material_type:
    print("We have this material. Please call for pricing.")