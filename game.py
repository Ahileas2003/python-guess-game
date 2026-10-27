import random

secret_number = random.randint(1, 10)

def check_guess(user_guess):
    if user_guess < secret_number:
        return "Моето число е по-голямо. Опитай пак!"
    elif user_guess > secret_number:
        return "Моето число е по-малко. Опитай пак!"
    else:
        return f"Поздравления! Позна числото {secret_number}!"

def new_game():
    global secret_number
    secret_number = random.randint(1, 10)
