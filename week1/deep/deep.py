#printig the input string and using split to avoid any whitespaces
x = input("What is the Answer to the Great Question of Life, the Universe, and Everything?").strip()

#to check the user input & coverting the input in lower case 
if x == "42" or x.lower() in ["forty-two", "forty two"]:
    print("Yes")
else:
    print("No")    

