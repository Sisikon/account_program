#!/usr/bin/env python3

# Account Program
# Version 0.1
# by R. Zwyer

# Short the "kassenprogramm.py" with function code (def) without discount calculation

# used
"""
  * variable
  * def
  * calculation
  * input
  * float
  * round
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
# turnover = umsatz
# checkout_process = kassenvorgang

# variable
continue_program = "n"
turnover = 0

# program start
while continue_program == "n":
    
#   function "checkout_process()" include the complete calculation
    def checkout_process():
        product_prize = input("How much it cost $: ")
        product_prize = float(product_prize)
        
        payment = input("The customer pay: ")
        payment = float(payment)
        
        change = round(payment - product_prize,2)
        
        print("Paid in $:", payment, "Product prize :", product_prize)
        print("Change money in $:", change)
        
        # return will end the dev function
        return product_prize
    
#   calculation of the turnover based on the checkout process    
    turnover = turnover + checkout_process()
    print(turnover)

#   Ask to restart program
    continue_program = input("Is your work time over 'n' ?")
    
#   End the program
    print("Thank you for your effort and enjoy your life")
    print(turnover)