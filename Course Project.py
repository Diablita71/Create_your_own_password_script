import secrets
import string

def password_gen(password_length, specific_word):
    
    characters = string.ascii_letters + string.digits
    
    secure_password = ''.join(secrets.choice(characters) for i in range(password_length))
    secure_password += specific_word
    
    return secure_password
    
def main():
    
    user_password_length = int(input("Input number of digits for password: "))
    user_specific_word = input("Input specific word for password: ")
    print("Password Generated: ", password_gen(user_password_length, user_specific_word))
    
main()