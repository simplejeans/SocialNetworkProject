import json

with open('config.json') as json_file:
    data = json.load(json_file)

    number_of_users = data["number_of_users"]
    max_posts_per_user = data["max_posts_per_user"]
    max_likes_per_user = data["max_likes_per_user"]

