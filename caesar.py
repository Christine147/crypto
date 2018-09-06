from helpers import alphabet_position, rotate_character

    
def encrypt(text,rot):
    zen = ""
    for char in text:
        zen = zen + rotate_character(char,rot)
    return zen

def main():
    user_input = input('Type a message: ')   
    rotations = int(input('Rotate by: ')) 
    result = encrypt(user_input, rotations)
    print (result)

if __name__ == '__main__':
    main()


        
        






