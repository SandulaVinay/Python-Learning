guess = True
import random
def guess_number():
    random_number = random.randint(1,100)
    return random_number
secret_number = guess_number()
while guess is True:
    print("Welcome!")
    user_input = input("Choose your difficulty 'E' for Easy 'H' for Hard").lower()
    print("Guess Number between 1 to 100!")
  
    if user_input == 'e':
        print("You have 10 chances to guess.")
        user_input = 10
    
    if user_input == 'h':
        print("You have 5 chances to guess.")
        user_input = 5

    # Comparative
    user_guess = 0
    
    while user_guess < 1:
        for i in range(1,user_input +1):
            guess_input = int(input(f"Guess{i}:"))
            
            if guess_input < secret_number:
                print("Too Low!")
                user_guess = 1

            elif guess_input > secret_number:
                print("Too High!")
                user_guess = 1
            
            elif guess_input == secret_number:
                print("You Won!")
                break
        else:
            print(f"Guess Number:{secret_number}")
            print("You Lost")                
            break


    guess = False
    break
