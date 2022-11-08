from random_word import RandomWords

random_word = RandomWords()


def randon_username() -> str:
    username = random_word.get_random_word()
    return username


def random_password() -> str:
    password = random_word.get_random_word()
    return password


def post_payload() -> dict:
    body = {"body": f"{random_word.get_random_word()}"}
    return body
