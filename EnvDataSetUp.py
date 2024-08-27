import os

from dotenv import load_dotenv

load_dotenv('.env')

username1 = os.getenv('Username1')
password1 = os.getenv('Password1')
username2 = os.getenv('Username2')
password2 = os.getenv('Password2')


def myEnvironment():
    print(f'My first username is: {username1}')
    print(f'My first password is: {password1}')
    print(f'My second username is: {username2}')
    print(f'My second username is: {password2}')


if __name__ == "__main__":
    myEnvironment()
