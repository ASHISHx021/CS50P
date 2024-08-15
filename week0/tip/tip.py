def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = float(dollars) * float(percent)
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    #replacing any "$"" with blank sapce
    output_d = d.replace("$", " ")
    
    #converting the string into float
    return float(output_d)

def percent_to_float(p):
    #replacing any "%" with blank spaces
    output_p = p.replace("%", " ")
    
    #converting the string into float and divide by 100
    return float(output_p)/100

main()    