unit= input("enter C or F :").lower()
temp= float(input("enter current temp  :"))


if unit =="c" or unit =="C":
    temp= round((9*temp)/5+32,1)
    print(f"the current temparature in farenhite is {temp}")
    
elif unit =="f" or unit =="F":
    temp= round((temp-32)*5/9,1)
    print(f"the current temparature in celsius is {temp}")
else :
    print("backchodi mat kar lode")