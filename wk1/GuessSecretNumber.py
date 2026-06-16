# number of trials
low = 1
high = 100
x=7
for i in range(x):
    if(low<=high):
         guess = (low + high) // 2
         print("Is your number", guess, "?")
         user_input = input("Your response (higher/lower/correct): ").strip().lower()
         if user_input == "correct":
             print("Your secret number is", guess, "guessed", i+1, "attempts!")
             break
         elif user_input == "higher":
             low = guess + 1
         elif user_input == "lower":
             high = guess - 1
         else:
             print("Invalid input. Please type 'higher', 'lower', or 'correct'.")