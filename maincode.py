import random

items = ['Snake','Water','Gun']

your_choice = input('Enter your move {Snake/Water/Gun}')
comp_choice = random.choice(items)

print(f"Your choice = {your_choice}, computer's choice = {comp_choice}")
#rules of the game and the winner
if your_choice == comp_choice:
  print("Both chose same item so it's a tie!")
elif your_choice == "Snake":
  if comp_choice == "Water":
    print("Snake drinks water, You WIN!")
  else:
    print("Gun kills the Snake, Computer WINS!")
elif your_choice == "Water":
  if comp_choice == "Gun":
    print("Gun fails in Water, You WIN!")
  else:
    print("Snake drinks the Water, Computer WINS!")
elif your_choice == "Gun":
  if comp_choice == "Snake":
    print("Gun kills the snake, You WIN!")
  else:
    print("Gun doesn't work in Water, Computer WINS!")
