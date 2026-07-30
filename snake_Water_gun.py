import random
#a small game called snake water gun where computer choose one of this and u choose one of this
#snake=1
#water=-1
#gun=0

computer=random.choice ([1,0,1])
youstr=input("enter Your Choice SNAKE(s),WATER(w), GUN(g)" )
youdict={"s":1,"w":-1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}


you=youdict[youstr]
print(f"you chose {reversedict[you]}\n computer chose {reversedict[computer]}")
#here we have two numbers one computer choose and one you chose

if((computer==you)):
    print("draw hoagaya ladle")
else:
    if(computer==-1 and you ==1):    #(computer-you)=-2
        print("kya baat hai lavde jeet gaya tu")
    elif(computer==-1 and you ==0):  #(computer-you)=-1
        print("Haar gaya chomu lol")
    elif(computer==1 and you ==-1):  #(computer-you)= 2
        print("Haar gaya chomu lol")
    elif(computer==1 and you ==0):   #(computer-you)= 1 
        print("kya baat hai lavde jeet gaya tu")
    elif(computer==0 and you ==-1):  #(computer-you)= 1
        print("kya baat hai lavde jeet gaya tu")
    elif(computer==0 and you ==1):   #(computer-you)= -1
        print("Haar gaya chomu lol")
    else:
        print("something went wrong zzzzzzzzzz")
        
#all the possiblities are taken here
#check the patter 
'''
shortend ver
here you lose when its 2 or -1 so....
if((computer-you)==-1 or (Computer-you)==2)
print("you lose)
else:
print("youwin")
'''