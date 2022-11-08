from random_word import RandomWords

random_word = RandomWords()


def get_randon_username() -> str:
    username = random_word.get_random_word()
    return username


def get_random_password() -> str:
    password = random_word.get_random_word()
    return password


def get_post_payload() -> dict:
    body = {"body": f"{random_word.get_random_word()}"}
    return body
