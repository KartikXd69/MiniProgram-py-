import random
n=random.randint(1,10) #generate number from 1 to 10
a=-1 #start from zero 
guessess=0
while(a != n ):
    a=int(input("guess a number"))
    if(a>n):
        print("lower number please")
        guessess+=1 #make the guessess + 
    elif(a<n):
        print("Higher number please")
        guessess+=1 #make the guessess + 
print(f"you Have guessed The Number {n} in {guessess} attempts ")
print("congratulations and celebration ")
