import random  # Import the random library to generate random numbers

# The guess function allows the user to guess a random number from 1 to x
def guess(x):
    random_number = random.randint(1, x)  # Generate a random number from 1 to x
    guess = 0  # Initialize the guess value
    while guess != random_number:  # Continue the loop until the guess is correct
        try:
            guess = int(input(f'Guess a number between 1 and {x}: '))  # Get the guess from the user
        except ValueError:  # If the user input is not a number, catch the ValueError
            print("Invalid input. Please enter a number.")  # Inform the user about the error
            continue  # Skip the rest of the loop and start the next iteration
        if guess < random_number:  # If the guess is less than the random number
            print('Sorry, guess again. Too low.')
        elif guess > random_number:  # If the guess is greater than the random number
            print('Sorry, guess again. Too high.')
    print(f'Congratulations! You have guessed the number {random_number} correctly!')  # Print a message when the guess is correct

# The computer_guess function allows the computer to guess the number the user is thinking of
def computer_guess(x):
    low = 1  # Initialize the lower limit
    high = x  # Initialize the upper limit
    while low != high:  # Continue the loop until the computer guesses the number correctly
        guess = random.randint(low, high)  # The computer guesses a random number from low to high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()  # Get feedback from the user
        if feedback not in ['h', 'l', 'c']:  # If the feedback is not 'h', 'l', or 'c'
            print("Invalid input. Please enter 'h', 'l', or 'c'.")  # Inform the user about the error
            continue  # Skip the rest of the loop and start the next iteration
        if feedback == 'h':  # If the guess is higher than the number the user is thinking of
            high = guess - 1
        elif feedback == 'l':  # If the guess is lower than the number the user is thinking of
            low = guess + 1
    print(f'Congratulations! The computer guessed your number, {low}, correctly!')  # Print a message when the computer guesses the number correctly