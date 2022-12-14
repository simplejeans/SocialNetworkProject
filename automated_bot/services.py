import random
from settings import max_posts_per_user, max_likes_per_user, number_of_users
from utils import get_randon_username, get_random_password, get_post_payload


class BotService:
    users = list()
    posts = list()

    def __init__(self, client):
        self.client = client

    def create_users(self):
        for i in range(1, number_of_users + 1):
            username = get_randon_username()
            password = get_random_password()
            self.client.sign_up(username=username, password=password)
            self.users.append({"username": username, "password": password})

    def create_posts(self):
        for i in range(0, len(self.users)):
            body = get_post_payload()
            for n in range(1, random.randint(2, max_posts_per_user + 1)):
                post = self.client.create_post(username=self.users[i].get("username"),
                                               password=self.users[i].get("password"), post_payload=body)
                self.posts.append(post)

    def like_posts(self):
        for i in range(0, len(self.users)):
            pk = random.choice(self.posts).get('id')
            for k in range(1, max_likes_per_user + 1):
                self.client.like_post(username=self.users[i].get("username"),
                                      password=self.users[i].get("password"), pk=pk)

    def main(self):
        self.create_users()
        self.create_posts()
        self.like_posts()
