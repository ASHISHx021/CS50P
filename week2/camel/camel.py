#defining main function
def main():
    #takes user input
    user_input = input("camel_case: ")
    
    #function camel_to_snake called with user_input as argument
    #And function returns new converted string stored in snake_case 
    snake_case = camel_to_snake(user_input)
    
    #prints the converted string
    print("snake_case:", snake_case)


#function to convert the camel string to snake_case
def camel_to_snake(camel):
    #intialize the string as empty string
    snake_case = ""
    
    #iterates over each character in the camel string.
    for i in camel:
        
        #checks if current character is 'i' is uppercase 
        if i.isupper():
            #if uppercase , it appends '_' to snake_case and convert it into lower case
            snake_case = snake_case + "_" + i.lower()
        else:
            #if not , directly append to snake_case without modification
            snake_case = snake_case + i   
    
    return snake_case


main()


