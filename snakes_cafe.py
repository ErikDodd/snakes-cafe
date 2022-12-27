def menu():
    print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************
""")
    print("""
Appetizers
----------
Egg Rolls
Dumplings
Pot Stickers

Entrees
-------
Pho'
Vermicelli
Pad Thai
Green Curry

Desserts
--------
Rootbeer Float
Ice Cream Sundae
Brownies

Drinks
------
Beer
Coca-Cola
LaCroix
    """)

def food_order():
    print(""" 
***********************************
** What would you like to order? **
***********************************
    """)
    food_order_dict = {}
    ask_again = True
    while ask_again:
        food_order = input("> ")
        if food_order in food_order_dict:
            food_order_dict[food_order] += 1
        else:
            food_order_dict[food_order] = 1
        for key in food_order_dict:
            if food_order != "quit":
                print(f"** {food_order_dict[key]} orders of {key} has been added to your meal **")
        if food_order == "quit":
            print("Thank you for vising Snakes Cafe!")
            quit()
            break
    #print(f"** 1 order of {food_order} has been added to your meal **")

    #ask_again = True
    #while ask_again:
        #print("Would you like to order other items?")
        #next_order = input("> ")
        #if next_order == "quit":
            #quit()
        #if next_order == "yes":
            #print("What else would you like to order?")
           # more_food = input("> ")
            #if more_food == "quit":
                #quit()
            #print(f"** 1 order of {more_food} has been added to your meal **")
        #else:
            #break
    # print(f"** Your order is {food_order} and {more_food} **")


menu()
food_order()

