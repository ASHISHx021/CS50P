#main function
def main():
    #takes time from user as a string
    user_time = input("What time is it? ")
    #calls the convert function and passes the user_time as argument
    Mtime(convert(user_time))


#function to covert string into floating time
def convert(time):  
      #splits the hours and minutes using the ":""
      hours, minutes = time.split(":")
      #convert hours string into float
      hours = float(hours)
      #converts minutes string into float 
      minutes = float(minutes)/60
      #Adds the converted hours and minutes together
      time = float(hours + minutes)
      #returns the converted time
      return time

#it takes converted time as argument and checks conditions
def Mtime(time): 
     if 7.00 <= time <= 8.00:
        print("breakfast time")
     elif 12.00 <= time <= 13.00:
         print("lunch time")
     elif 18.00 <= time <= 19.00:
         print("dinner time")
     else:
        print()     
     


if __name__ == "__main__":
    main()