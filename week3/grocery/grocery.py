def main():
    grocery = {}

    while True:
        try:
            user_input = input().strip()
            if user_input in grocery:
                #If the item is already in the dictionary increment its count by 1.
                grocery[user_input] = grocery[user_input] + 1
            else:
                #If the item is not in the dictionary,add it with count by 1.
                grocery[user_input] = 1
        except EOFError:
                print()
                #Sort the items alphabetically and print them in uppercase with their counts.
                for user_input in sorted(grocery):
                     print(f"{grocery[user_input]} {user_input.upper()}")
                break
        except KeyError:
             pass     

main()
