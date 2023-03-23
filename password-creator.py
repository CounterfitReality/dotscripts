import string
import secrets

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

if __name__ == '__main__':
    length = int(input('Enter password length: '))
    password = generate_password(length)
    print(f'Your random password is: {password}')
