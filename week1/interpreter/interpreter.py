#taking the user input
user_input = input("Expression: ")

#spliting string into three parts 
x,y,z = user_input.split()


x = float(x) #converts the x into floating no.
y = str(y)    #converts the y to string.
z = float(z) #converts the y into floating no.

#checking the conditions
if y == "+":
    print(round(x+z,1))
elif y == "-":
    print(round(x-z,1))
elif y == "*":
    print(round(x*z,1))
elif y =="/" and z!=0:
    print(round(x/z,1))
else: 
    print("Invalid expression")        


