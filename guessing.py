import art

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


def quessing(text):

    art.tprint('\nif side was right')

    for i in range(1, 26):
        print(f"{encode(text, i, 'left')}\n(shift = {i})\n")

    art.tprint('\nif side was left')
    for i in range(1, 26):
        print(f"{encode(text, i, 'right')}\n(shift = {i})\n")

def main():
    print('Enter the text: ', end = '')
    text = input()

    quessing(text)

if __name__ == '__main__':
    main()
