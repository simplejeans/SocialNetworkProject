from django.utils.datetime_safe import datetime
from freezegun import freeze_time
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from posts.models import Post, User, Like


class PostApiTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username="alabama", password="password")
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        self.post = Post.objects.create(body="qwerty", author=self.user)
        self.like = Like.objects.create(post=self.post, user=self.user)

    def test_post(self):
        sample_post = {"body": "qwerty"}
        response = self.client.post(reverse("post-list"), sample_post)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        post = Post.objects.last()
        self.assertEqual(post.body, sample_post["body"])
        self.assertEqual(post.author, self.user)

    def test_like(self):
        url = reverse("post-like", kwargs={"pk": self.post.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        like = Like.objects.last()
        self.assertEqual(like.post, self.post)
        self.assertEqual(like.user, self.user)

    def test_unlike(self):
        url = reverse("post-unlike", kwargs={"pk": self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        like = Like.objects.last()
        self.assertIsNone(like)


@freeze_time("2022-10-16")
class LikesAnalyticsApiTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username="alabama", password="password")
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        self.post = Post.objects.create(body="qwerty", author=self.user)
        self.post2 = Post.objects.create(body="qwerty2", author=self.user)
        self.like = Like.objects.create(post=self.post, user=self.user, created_at=datetime.now)
        self.like2 = Like.objects.create(post=self.post2, user=self.user, created_at=datetime.now)

    def test_likes_analytics(self):
        url = "http://127.0.0.1:8000/api/posts/likes/analytics/?date_from=2022-10-15&date_to=2022-10-18/"
        expected_data = [{"date": "2022-10-16", "likes": 2}]
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected_data)


@freeze_time('2022-10-16T00:00:00Z')
class UserActivityTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username="alabama", is_active=True)
        self.user.set_password("password")
        self.user.save()

    def test_user_activity(self):
        self.client.force_login(self.user)
        url = reverse("users:user_activity", kwargs={"user_id": self.user.id})
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code, response.json())
        response_data = response.json()
        self.assertEqual(response_data["user"], self.user.id)
        self.assertEqual(response_data["last_login"], '2022-10-16T00:00:00Z')
        self.assertEqual(response_data["last_request"], '2022-10-16T00:00:00Z')
