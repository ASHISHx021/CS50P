def main():
   #calls the get function and stores the returned value in x
   x = get_fraction()
   print(x)






def get_fraction():
    while True:
        try:
            user_input = input("Fraction : ")
            #The input string is split into two parts, x and y, using split("/")
            x,y = user_input.split("/")
            #x and y are converted from strings to integers
            x = int(x)
            y = int(y)

            output = x/y 
            #checks the conditions
            if 0 <= output <= 0.1:
                return "E"
            elif 0.9 <= output <= 1:   
               return "F"
            elif 0.1 < output < 1:
                #Returns the percentage of fraction rounded to the nearest integer
                return (f"{round(output*100)}") + "%"   
        #handles the exceptions
        except (ValueError, ZeroDivisionError):
            pass
         
main()   
     