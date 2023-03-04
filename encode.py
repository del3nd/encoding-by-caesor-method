import pyperclip

def encode(text, shift, side):
    new_text = ''

    all_letters = 'abcdefghijklmnopqrstuvwxyz'

    for letter in text:

        upper = True if letter.isupper() else False
        
        letter = letter.lower()

        if letter in all_letters:
            try:
                new_text += all_letters[all_letters.index(letter) - shift if side == 'left' else all_letters.index(letter) + shift].upper() if upper == True else (all_letters[all_letters.index(letter) - shift if side == 'left' else all_letters.index(letter) + shift])
            except:
                new_text += all_letters[-(shift - all_letters.index(letter)) if side == 'left' else shift - (len(all_letters) - all_letters.index(letter))].upper() if upper == True else all_letters[-(shift - all_letters.index(letter)) if side == 'left' else shift - (len(all_letters) - all_letters.index(letter))]
        else:
            new_text += letter



    return new_text

def main():
    print('Enter the text to encode: ', end = '')
    text = input()
    print("Enter shift: ", end = '')
    shift = int(input())
    print("Enter side: ", end = '')
    side = input()
    proccessing = True

    #checking
    if shift > 26:
        print("shift haven't to be bigger then 26 ")
        proccessing = False
    elif side.lower() not in ['right', 'left']:
        print('side have to be said like right or left')
        proccessing = False

    result = encode(text, shift, side)

    if proccessing:
        print(f'The result is: \n{result}')
        print('Do you wish to copy result to clipboard? [y/n]: ', end = '')
        asnwer = True if input() in ['yes', 'y'] else False

        if asnwer:
            pyperclip.copy(result)

if __name__ == '__main__':
    main()