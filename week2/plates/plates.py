def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #The plate must be between 2 and 6 characters long and consist of only letters and digits.
    if 2 <= len(s) <=6 and s.isalnum():
            
            #if the plate consist only all alphabetic then it valid
            if s.isalpha():
                return True
            else:
               """if plate is not all alpha, then it must start with at least 2 letter
                 and end with at least 2 digits"""
            if s[:2].isalpha() and s[-2:].isdigit():
                      #itearte through each character in plate
                        for i in range(len(s)):
                           #if digit is found
                           if s[i].isdigit():
                                #if digit start with '0' or letter,its invalid
                                if s[i].startswith("0") or s[i:].isalpha():
                                    return False
                                else:
                                     return True
            else:
                    return False  
    else:
        return False                       
                 



main()