def main():

 user_input = input("Input: ")
 #function passing the user_input string as an argument which is the input string with vowels removed
 print(remove_vowels(user_input))

def remove_vowels(user_input):
    letter_to_replace = "aeiouAEIOU"

    for i in letter_to_replace:
     # in the user_input string with an empty string (""),removing it from the string.
     user_input = user_input.replace(i, "")

    return user_input 

main()     

