import random
from settings import max_posts_per_user, max_likes_per_user, number_of_users
from utils import randon_username, random_password, post_payload


class BotService:
    users = list()
    posts = list()

    def __init__(self, client):
        self.client = client

    def create_user(self):
        for i in range(1, number_of_users + 1):
            username = randon_username()
            password = random_password()
            self.client.sign_up(username=username, password=password)
            self.users.append({"username": username, "password": password})

    def post(self):
        for i in range(0, len(self.users)):
            body = post_payload()
            for n in range(1, random.randint(2, max_posts_per_user + 1)):
                post = self.client.create_post(username=self.users[i].get("username"),
                                               password=self.users[i].get("password"), post_payload=body)
                self.posts.append(post)

    def like(self):
        for i in range(0, len(self.users)):
            pk = random.choice(self.posts).get('id')
            for k in range(1, max_likes_per_user + 1):
                self.client.like_post(username=self.users[i].get("username"),
                                      password=self.users[i].get("password"), pk=pk)

    def main(self):
        self.create_user()
        self.post()
        self.like()
