def main():
    x = get_menu()
    print(x)



    

def get_menu():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total = 0

    while True:
        try:
            user_input = input("Item: ").title().strip() 

            total = total + menu[user_input]
            print(f"Total: ${total:.2f}")
        # Break the loop if Ctrl+D is pressed
        except EOFError:
            break
        #f the user enters invalid item,Then it ignores the invalid input and continues
        except KeyError:
            pass
        

main()    