def guessgame():

  import random
  #Create a random number
  number = random.randint(1, 9)

  guesses = 0

  while True:

    guesses = guesses + 1

    usernumber = input('Guess a number between 1 and 9 or type exit to quit: ')
    
    if usernumber == 'exit':
        break
    
    int_as_string = int(usernumber)

    if number == int_as_string:
      print(f'You guessed right with {guesses} Guesses')

    elif number > int_as_string:
      print('You guessed to low!')

    elif number < int_as_string:
      print('You guessed too high!')
    
guessgame()