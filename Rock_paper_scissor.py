#input From user
#computer choice=random
#result 

'''
cases:
A - rock (if user inputs rock)
rock and Rock =tie
rock and paper= paper win
rock and Scissor= rock win

B-paper(if user inputs paper)
paper and Rock = paper win
paper and paper= tie
paper and Scissor= Scissor win

C-Scissor (if user inputs Scissor)
Scissor and Rock = rock win
Scissor and paper= Scissor win
Scissor and Scissor= tie win
'''
import random
item_list= ["Rock","Paper","Scissor"]

user_choice=input("enter your choice (Rock,Paper,Scissor)")
computer_choice=random.choice(item_list)#choose a random varient from the list


print(f"user choice = {user_choice} and computer choice = {computer_choice}")

if user_choice == computer_choice : #for tie
    print("Tie try again")
    
elif user_choice == "Rock": #if user choose rock 
    if computer_choice =="paper": #and comp choose paper 
        print("paper covers rock thus computer win lamao You loser ") #comp wins
    else :
        print("Rock Smashes Scissor You win Do Something Better In Life Now lol ") #else comp choose scissor You win
        
elif user_choice == "Paper": 
    if computer_choice =="rock":
        print("You won Touch Some Grass ") 
    else :
        print("lamao Loser") 
        
elif user_choice == "Scissor": 
    if computer_choice =="rock":
        print("Get Better You Losser you lost") 
    else :
        print("Finally You won Atleast Something") 
    
       
    