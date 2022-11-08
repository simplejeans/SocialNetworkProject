# import random
# import requests
# import json
# from random_word import RandomWords
#
#
# class Bot:
#
#     with open('config.json') as json_file:
#         data = json.load(json_file)
#         number_of_users = data["number_of_users"]
#         max_posts_per_user = data["max_posts_per_user"]
#         max_likes_per_user = data["max_likes_per_user"]
#
#     users = list()
#     posts = list()
#
#     def sign_up(self):
#         for i in range(1, self.number_of_users+1):
#             random_word = RandomWords()
#             username = random_word.get_random_word()
#             data = {"username": f"{username}", "password": "qwerty", "password2": "qwerty"}
#             response = requests.post('http://127.0.0.1:8000/api/users/register/', json=data)
#             self.users.append(response.json())
#
#     def create_a_post(self):
#         for i in range(0, len(self.users)):
#             data = {"username": f'{self.users[i].get("username")}', "password": "qwerty"}
#             get_token = requests.post('http://127.0.0.1:8000/api/users/token/', json=data)
#             token = get_token.json().get("access")
#             head = {"Authorization": f"Bearer {token}"}
#             random_text = "".join(chr(random.randint(33, 126)) for m in range(10))
#             for n in range(1, random.randint(2, self.max_posts_per_user + 1)):
#                 response = requests.post(f"http://127.0.0.1:8000/api/posts/", headers=head, json={"body": f"{random_text}"})
#                 self.posts.append(response.json())
#
#     def likes(self):
#         for i in range(0, len(self.users)):
#             data = {"username": self.users[i].get("username"), "password": "qwerty"}
#             get_token = requests.post('http://127.0.0.1:8000/api/users/token/', json=data)
#             token = get_token.json().get("access")
#             head = {"Authorization": "Bearer {}".format(token)}
#             for k in range(1, self.max_likes_per_user + 1):
#                 requests.post(f"http://127.0.0.1:8000/api/posts/{random.choice(self.posts).get('id')}/like/", headers=head)
#
#     def main(self):
#         self.sign_up()
#         self.create_a_post()
#         self.likes()
#
#
from clients import SocialNetworkAPIClient
from services import BotService

if __name__ == "__main__":
    client = SocialNetworkAPIClient()
    bot = BotService(client)
    bot.main()

