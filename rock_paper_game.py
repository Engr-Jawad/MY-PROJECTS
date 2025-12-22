# #input from the user
# #computer random choice
# #print rersults

# # cases
# # case 1
# # rock->rock=Tie
# # rock->paper=paper win
# # rock->scissors=rock win


# # case 2
# # paper -> rock =paper win
# # paper -> paper =tie
# # paper -> scissors = scissors win 


# # case 3
# # scissors -> rock= rock win
# # scissors -> paper = scissors win 
# # scissors -> scissors =tie

# # lets start coding
import random
# attempt=0
# while(attempt < 5):
list=['rock','paper','scissors']
user_action=input("enter your choice (rock,paper,scissors) :")
computer_action=random.choice(list)
print(f"\n you chose {user_action},computer choice {computer_action}.\n")
if user_action==computer_action:
    print(f"both players selected {user_action}.its a tie !")
elif user_action=='rock':
    if computer_action == 'paper':
        print("paper cover rock so computer wins ")
    else:
        print("rock  break the scissors so rock wins")
elif user_action == 'paper':
    if computer_action=='scissors':
        print("scissors cut paper so computer wins")
    else:
        print("paper cover rock so paper wins")
elif user_action=='scissors':
    if computer_action=='rock':
        print("rock break the scissors so computer wins")
    else:
        print("scissor cut paper so scissors wins")




# ##############################same code but below code have the gui  and the above code have not gui ##############
# import random
# import tkinter as tk

# # Main window
# root = tk.Tk()
# root.title("Rock Paper Scissors")
# root.geometry("400x300")

# choices = ['rock', 'paper', 'scissors']

# # Result label
# result_label = tk.Label(root, text="Choose Rock, Paper, or Scissors",
#                         font=("Arial", 12), pady=20)
# result_label.pack()

# def play(user_action):
#     computer_action = random.choice(choices)

#     if user_action == computer_action:
#         result = f"Both chose {user_action}. It's a Tie!"
#     elif user_action == 'rock':
#         if computer_action == 'paper':
#             result = "Paper covers Rock. Computer Wins!"
#         else:
#             result = "Rock breaks Scissors. You Win!"
#     elif user_action == 'paper':
#         if computer_action == 'scissors':
#             result = "Scissors cut Paper. Computer Wins!"
#         else:
#             result = "Paper covers Rock. You Win!"
#     elif user_action == 'scissors':
#         if computer_action == 'rock':
#             result = "Rock breaks Scissors. Computer Wins!"
#         else:
#             result = "Scissors cut Paper. You Win!"

#     result_label.config(
#         text=f"You chose: {user_action}\nComputer chose: {computer_action}\n\n{result}"
#     )

# # Buttons
# button_frame = tk.Frame(root)
# button_frame.pack(pady=20)

# rock_btn = tk.Button(button_frame, text="Rock", width=20,
#                      command=lambda: play('rock'))
# paper_btn = tk.Button(button_frame, text="Paper", width=20,
#                       command=lambda: play('paper'))
# scissors_btn = tk.Button(button_frame, text="Scissors", width=20,
#                          command=lambda: play('scissors'))

# rock_btn.grid(row=0, column=0, padx=5)
# paper_btn.grid(row=0, column=1, padx=5)
# scissors_btn.grid(row=0, column=2, padx=5)

# # Start GUI loop
# root.mainloop()
