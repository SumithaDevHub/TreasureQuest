print("Welcome to Treasure Island! Your mission is to find the treasure")
choice = input ("Left or Right?").lower()
if choice == "left":
    swim_choice = input("Swim / Wait").lower()
    if swim_choice == "wait":
        door_choice = input("Which color door? (yellow, blue, red)").lower()
        if door_choice == "yellow":
            print("You Win!")
        elif door_choice == "blue":
            print("Eaten by beasts. Game over!")
        elif door_choice == "red":
            print("Burned by fire. Game over!")
        else:
            print("Game Over!")
    else:
        print("Attacked by a trout. Game Over!")
else:
    print("Fell in a hole. Game Over!")