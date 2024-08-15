#defining the function that takes string as input
def convert(string):
   
   #replcing emojis with input string
   output = string.replace(":)", "🙂").replace(":(", "🙁")
   return output

def main():
    #taking user input
    usr_input = input()
    
    #calling convert function and printing output
    print(convert(usr_input))
main()    