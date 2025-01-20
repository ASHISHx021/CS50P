month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    user_input = input("Date: ")
    try:
        # Check if the input contains a "/" 
        if "/" in user_input:
            mm, dd, yyyy = user_input.split("/")  #Split into month, day, and year
        
        # Check if the input contains a ","
        elif "," in user_input:
            mmdd, yyyy = user_input.split(", ")  #Split into "Month DD" and year
            mm, dd = mmdd.split(" ")   #Split "Month DD" into month and day
            
            mm = (month.index(mm)) + 1  #Convert month name to month numbe
        
        #Validate the month and day numbers
        if int(mm) > 12 or int(dd) > 31:
            raise ValueError
    #Handle invalid inputs and exceptions
    except (ValueError, NameError, KeyError):
        pass
    
    else:
        print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
        break