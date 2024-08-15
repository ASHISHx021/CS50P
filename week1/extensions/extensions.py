#taking user input and using case-insensitively with lower

user_input =input("File name: ").lower().strip()

# cheking the conditions for extensions and used endswith to check suffix 
if user_input.endswith(".gif"):
    print("image/gif")

elif user_input.endswith(".jpeg") | user_input.endswith(".jpg"):
    print("image/jpeg")

elif user_input.endswith(".png"):
    print("image/png")

elif user_input.endswith(".pdf"):
    print("application/pdf")

elif user_input.endswith(".txt"):
    print("text/plain")

elif user_input.endswith("zip"):
    print("application/zip")

else:
    print("application/octet-stream")      
