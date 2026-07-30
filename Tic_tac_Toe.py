#import Tkinter Which Is an standar library in python for Gui

import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner

    for combo in [[0,1,2],[3,4,5],[6,7,8],
                  [0,3,6],[1,4,7],[2,5,8],
                  [0,4,8],[2,4,6]]:
        
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            winner = True
            return  # stop further checking

    if all(button["text"] != "" for button in buttons) and not winner:
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        winner = True
        
def ai_move():
    global winner

    # All winning combinations
    combos = [[0,1,2],[3,4,5],[6,7,8],
              [0,3,6],[1,4,7],[2,5,8],
              [0,4,8],[2,4,6]]

    # 1️⃣ Try to WIN
    for combo in combos:
        values = [buttons[i]["text"] for i in combo]
        if values.count("O") == 2 and values.count("") == 1:
            index = combo[values.index("")]
            buttons[index]["text"] = "O"
            check_winner()
            return

    # 2️⃣ Try to BLOCK player
    for combo in combos:
        values = [buttons[i]["text"] for i in combo]
        if values.count("X") == 2 and values.count("") == 1:
            index = combo[values.index("")]
            buttons[index]["text"] = "O"
            check_winner()
            return

    # 3️⃣ Otherwise pick first empty
    for i in range(9):
        if buttons[i]["text"] == "":
            buttons[i]["text"] = "O"
            check_winner()
            return
    
def restart_game():
    global current_player, winner

    current_player = "X"
    winner = False

    for button in buttons:
        button.config(text="", bg="SystemButtonFace")

    label.config(text=f"Player {current_player}'s turn")
    
def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = "X"
        check_winner()

        if not winner:
            ai_move()

root=tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [tk.Button(root,text="",font=("normal",25),width=6,height=2,command=lambda i=i: button_click(i)) for i in range (9) ]
for i,button in enumerate(buttons):
    button.grid(row=i //3, column=i % 3)
    
    
current_player="X"
winner = False
label=tk.Label(root,text=f"Player {current_player}'s turn",font =("normal",16))
label.grid(row=3,column=0,columnspan=3)

restart_btn = tk.Button(root, text="Restart", font=("normal", 14), command=restart_game)
restart_btn.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()