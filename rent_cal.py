'''
input :
rent
Total Food Ordered
electricity unit
Charge Per Unit
total no of person 

Output
total Amount You Have To Pay

'''
rent=int(input("enter Your Rent:"))
food=int(input("enter Total Price OF Food Ordered:"))
ele_spend=int(input("Enter Electricity spend:"))
Charge_per_Unit=int(input("Enter Charge Per Unit"))
Total_peeps=int(input("Enter Total Number OF person"))

# basic logic OF this Program
'''
adding all the inputs and dividing it with the the total number of peeps

'''
bill= ele_spend*Charge_per_Unit #getting the bill for easier calculation this will help in dividing electricity properlly



#now a variable which takes output
 
output=(rent+food+bill)/Total_peeps
print(f"the amount per person is ",output)