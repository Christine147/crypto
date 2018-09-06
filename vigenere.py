from helpers import alphabet_position, rotate_character

    
def encrypt (text,keyword):
    secret = ''
    index = 0
    for char in text:
        if char.isalpha():
            secret_key = index % len(keyword)
            rot = alphabet_position(keyword[secret_key])
            secret += rotate_character(char,rot)
            index += 1
        else:
            secret += char
    return secret
    

def main():
    user_input = input('Type a message: ')   
    key = input('Key: ')
    result = encrypt(user_input, key)
    print (result)

    
if __name__ == '__main__':
    main()
