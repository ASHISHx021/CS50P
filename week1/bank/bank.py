#taking user input and avoiding whitespaces with split and handling case-insensitively with lower 
Greeting = input("Greeting: ").strip().lower()

#check if hello is present in striing
if Greeting.startswith("hello"):
    print("$0")
#chack if greeting start with h but not hello    
elif Greeting.startswith("h"):
    print("$20")
else:
    print("$100")    

