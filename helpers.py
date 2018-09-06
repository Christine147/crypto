def alphabet_position(letter):
    alphabet = ('abcdefghijklmnopqrstuvwxyz')
    letter_low = letter.lower()
    position = alphabet.index(letter_low)
    return position 
    
def rotate_character(char,rot):
    if char.isalpha():
        alphabet = ('abcdefghijklmnopqrstuvwxyz')
        position = alphabet_position(char)
        num_of_clicks = (position + rot) % 26
        new_letter = alphabet[num_of_clicks]
        if char.isupper():
            return new_letter.upper()
        else:
            return new_letter
    else:
        return char