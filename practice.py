'''num=int(input("emter a number"))

if num > 1 :
    for i in range (2,int(num**0.5)+1):
        if num % i==0:
            print("not a prime number")
            break
    else:
        print(num,"is a prime number")'''


'''def prime_re(num):
    if num<= 1:
        return False
    for i in range (2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

num = int(input("enter a number"))
if prime_re(num):
    print(num,"number is prime")
else:
    print(num,"not prime")'''


def compo(num):
    if num<1:
        return False
    for i in range (2,int(num**0.5)+1):
        if num % i == 0 :
            return True
    return False

num=int(input("enter a number"))
if compo(num):
    print ("its a composite number")
elif num <= 1:
    print ("nor prime nor compo")
else:
    print("prime ")