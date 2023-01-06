# Jennifer Souvannasing, SEC 290 Block 2, Programming assignment wk3 - Step 3, 07/19-20/22

# This function will convert letters to MORSE code
# There has to be a better way to store all the numbers and letter for this.
def text_to_morse(user_input):
        
    if user_input == 'A':
        morse_out = '.-'

    elif user_input == 'B':
        morse_out = '-...'

    elif user_input == 'C':
        morse_out = '-.-.'

    elif user_input == 'D':
        morse_out = '-..'

    elif user_input == 'E':
        morse_out = '.'

    elif user_input == 'F':
        morse_out = '..-.'

    elif user_input == 'G':
        morse_out = '--.'

    elif user_input == 'H':
        morse_out = '....'

    elif user_input == 'I':
        morse_out = '..'

    elif user_input == 'J':
        morse_out = '.---'

    elif user_input == 'K':
        morse_out = '-.-'

    elif user_input == 'L':
        morse_out = '.-..'

    elif user_input == 'M':
        morse_out = '--'

    elif user_input == 'N':
        morse_out = '-.'

    elif user_input == 'O':
        morse_out = '---'

    elif user_input == 'P':
        morse_out = '.--.'

    elif user_input == 'Q':
        morse_out = '--.-'

    elif user_input == 'R':
        morse_out = '.-.'

    elif user_input == 'S':
        morse_out = '...'

    elif user_input == 'T':
        morse_out = '-'

    elif user_input == 'U':
        morse_out = '..-'

    elif user_input == 'V':
        morse_out = '...-'

    elif user_input == 'W':
        morse_out = '.--'
        
    elif user_input == 'X':
        morse_out = '-..-'

    elif user_input == 'Y':
        morse_out = '-.--'


    elif user_input == 'Z':
        morse_out = '--..'        

    elif user_input == '':
        return morse_out
    
    else:
        morse_out = 'Unknown'

    return morse_out

# Banner
intro = '|          Text to Morse Letter Translator        |'
text_len = len(intro)
print('{}'.format('-' * text_len))
print(intro)
print('{}'.format('-' * text_len))
print()

# Input looping
for user_input in range (26):
    user_input = input('Please enter an usercase letter to be translated: ')
    morse_out = text_to_morse(user_input)
    print('Your code for {} is {}'.format(user_input,morse_out))

# Exit message
print('Thanks for translating with us!')
