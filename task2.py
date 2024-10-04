data_file = 'player_data.txt'

def save_data(health, score):
    with open(data_file, 'w') as file:
        file.write(f"{health}\n{score}\n")
    print("Data saved successfully.")

def load_data():
    try:
        with open(data_file, 'r') as file:
            health = int(file.readline().strip())
            score = int(file.readline().strip())
        print("Data loaded successfully.")
        return health, score
    except FileNotFoundError:
        print("No saved data found. Starting new game.")
        return 100, 0 

def main():
    print("Welcome to the Text-Based Game!")
    health, score = load_data()

    while True:
        print(f"\nCurrent Health: {health}, Current Score: {score}")
        print("Choose an action:")
        print("1. Play Game (increase score)")
        print("2. Take Damage (decrease health)")
        print("3. Save Game")
        print("4. Load Game")
        print("5. Exit Game")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            score += 5
            print("You played the game and earned 5 points!")
        
        elif choice == '2':
            damage = int(input("Enter damage taken: "))
            health -= damage
            if health < 0:
                health = 0
            print(f"You got {damage} damage!")
        
        elif choice == '3':
            save_data(health, score)
        
        elif choice == '4':
            health, score = load_data()
        
        elif choice == '5':
            print("Exiting the game. Goodbye!!")
            break
        
        else:
            print("Invalid choice, please try again!!")

if __name__ == "__main__":
    main()