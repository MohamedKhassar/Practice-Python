import random

def main():
    number=random.randrange(1,100)
    guessing=int(get_input("Guess the number between 1 and 100: "))
    while number!=guessing:
        if guessing>0 and guessing<=100:
            if guessing>number:
                print("Too high!")
            else:
                print("Too low!")
            guessing=int(get_input("Guess again: "))
        else:
            guessing=int(get_input("Invalid input. Please enter a number between 1 and 100: "))
    print(f"Congratulations! You guessed the number {number} correctly.")

def get_input(placeholder):
    answer=input(placeholder)
    return answer

main()