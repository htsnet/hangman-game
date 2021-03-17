# -*- coding: utf-8 -*-

# global variables
word_letters = ''
max_tries = 6
tries = 0
tries_ok = 0
game_over = False
array_letters = []
show_word = ''


def start_game():
    global guessing_word
    global game_over
    global tries
    global tries_ok
    global show_word
    
    tries= 0
    tries_ok = 0
    
    # import modules
    import random
    
    # import words from hangman_guessing.py
    from hangman_guessing import guess_list
    
    # get an random word
    guessing_word = random.choice(guess_list).upper()
    show_word = '______'
    word_letters = len(guessing_word)
    
    # keep the gam runing until the game is over
    game_over = False
        
    # get hangman shapesfrom hangman_life.py
    from hangman_life import game_name
    print(game_name)

    # show initial message 
    print("The word was choosen!")
    print('The word has {} letters.'.format(word_letters))
    ask_letter()
    
    
    
def ask_letter():
    global guessing_word
    global game_over
    global array_letters
    global tries
    
    if tries >= max_tries:
        game_over = True
        end_game()
    
    # ask an letter
    letter = input('Type an letter ').upper()
    if letter < 'A' or letter > 'Z':
        print('This is not an valid option. Try again.')
        ask_letter()
    elif letter in array_letters:
        print('This letter was already used. Try another.')
        ask_letter()
    else:
        array_letters.append(letter)
        tries += 1
        if letter in guessing_word:
            letter_ok(letter)
        else:
            letter_wrong(letter)
                
def letter_ok(letter):
    global show_word
    global guessing_word
    global tries_ok
    
    fromPosition = 0
    # change all letters found
    while True:
        position = guessing_word.find(letter, fromPosition)
        #print(position)
        if position < 0:
            break
        show_word = show_word[:position] + letter + show_word[position+1:]
        fromPosition = position + 1
        tries_ok += 1
        
    
    print('The word is: ', ' '.join(show_word))
    if guessing_word == show_word or tries_ok == 6:
        end_game()
    else: 
        ask_letter()


def letter_wrong(letter):
    print('This letter is not in the word.')
    ask_letter()

def end_game():
    import sys
    global game_over
    print("The game is over!")
    print(f'The word is {guessing_word}')
    if game_over:
        print('You loose!!')
    else:
        print('You win!!! ;-)')
    sys.exit()

start_game()