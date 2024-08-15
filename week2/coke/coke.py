#total price user need to paid
price= 50
#acceptable coins only
coin = [10,25,5]
#to track how much money is inserted
total_paid = 0

#loop iterates until the price is grater than 0
while price > 0:
        #print current amount user needs to pay
        print(f"Amount Due: {price}")

        user_input = int(input("Insert Coin: "))
        
        #check whether inserted amount is acceplatble
        if user_input in coin:
            #if coin is valid , it subtract coins value from remaining price
            price = price - user_input
            
            # to keep track how much coin user has inserted
            total_paid = total_paid + user_input

#if price become lower than total paid or '0'
if total_paid >= price:
        print(f"Change Owed: {total_paid - 50}")        

       