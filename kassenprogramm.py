#!/usr/bin/env python3

# Account Program
# Version 0.1
# by R. Zwyer

# used
"""
  * variable
  * calculation
  * input
  * float
  * round
  * if, else
  * print
"""

# variable transformation from german to english
# ****************
# continue_program = eingabe
# product_prize = preis
# discount_percent = rabatt_in_prozent
# discount_currency = rabatt_in_euro
# product_prize_discount = neuer_preis
# zahlung = payment
# change = rückgeld

# variable
continue_program = "n"

# program start
while continue_program == "n":
    
#   Entry of prize and discount
    product_prize = input("How much it cost $: ")
    discount_percent = input("How much discount in %: ")
    
#   change data type from string to float.point
    product_prize = float(product_prize)
    discount_percent = float(discount_percent)
    
#   calculate
    discount_currency = product_prize/100 * discount_percent
    product_prize_discount = product_prize - discount_currency
    print("Product prize with", discount_percent, "% discount is: ", product_prize_discount)
    
#   Entry payment and change datatype to float
    payment = input("The customer pay: ")
    payment = float(payment)
    
#   Change money & and round it to 2 points after comma
    change = round(payment - product_prize_discount,2)
    if change <0:
        print("The payed money is not enough")
    else:
        print("Paid in $:", payment, "Product prize with discount in $:", product_prize_discount)
        print("Change money in $:", change)
    
#   Ask to restart program
    continue_program = input("Is your work time over 'n' ?")
    
#   End the program
print("Thank you for your effort and enjoy your life")