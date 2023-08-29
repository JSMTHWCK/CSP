
import numpy as np
print("Welcome to the Space Travel Calculator")
distance = float(input("input distance (in light years) to object"))
speed = float(input("in decimal form, choose aircraft speed"))
time = distance/speed
print("it would take " + str(time) + " time to reach destination")

###Norman###
restaurants = ["Din Tai Fung","Houston's","Paulette's Pupusas","Leah's Thai","Taco Bell"]
new_restaurant = input("What restaurant would you like to add to the list?")

for i in range(len(restaurants) - 1,-1,-1):
    choice = input("Do you like A) " + new_restaurant + " or B) " + restaurants[i] + " more?")
    if choice == "A":
        continue
    elif choice == "B":
        restaurants.insert(i + 1,new_restaurant)
        break
    else:
        print("Please choose A or B (case sensitive)")
if new_restaurant not in restaurants:
    restaurants.insert(0,new_restaurant)
print(restaurants)
###Uemura###
def play_game():
    logicDict = {
            "rock" : {"rock":0, "paper":2, "scissors" : 1},
            "paper" : {"rock":1, "paper":0, "scissors":2},
            "scissors": {"rock":2,"paper":1,"rock":0}
        }
    current_score = 0
    for i in range(3):
        if np.abs(current_score) != 2:
            print("round " + str(i))
            p1move = input("Player 1 make your move ").lower()
            p2move = input("Player 2 make your move ").lower()
            if p1move not in logicDict or p2move not in logicDict:
                print("invalid move, round will be replayed")
                i -= 1
            else:
                winner = logicDict[p1move][p2move]
                if winner == 0:
                    print("round " + str(i) + " ended in a tie")
                else:
                    print("winner of round " + str(i) + " is player " + str(winner))
                current_score += [0,1,-1][winner]
    if current_score > 0:
        print("Player 1 won")
    elif current_score < 0:
        print("Player 2 won")
    else:
        print("it's a tie")



play_game()
###Tandon###
existing_count = {"aluminum":135,"plastic":102,"paper":213}

def sort_items(itemstring):
    codes = {"a":"aluminum","p":"plastic","r":"paper"}
    for char in itemstring.lower():
        if char in codes:
            if char in codes:
                existing_count[codes[char]] += 1
    print(existing_count)
    

sort_items("AAPAARRRRPAAPPRRP")
