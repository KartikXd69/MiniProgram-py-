
n=int(input("enter A number :"))

table = [n*i for i in range (1,11)]#generate a table of number given by user
with open ("table.txt","a") as f:
    f.write(f"table of {n} is : {str(table)} \n")