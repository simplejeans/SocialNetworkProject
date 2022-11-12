from unittest.mock import patch
import unittest
from clients import SocialNetworkAPIClient


class BotApiTestCase(unittest.TestCase):

    def setUp(self):
        self.client = SocialNetworkAPIClient()

    @patch.object(SocialNetworkAPIClient, 'sign_up')
    def test_sign_up(self, mock_sign_up):
        self.client.sign_up(username='username', password='password')
        mock_sign_up.assert_called_with(username='username', password='password')

    @patch.object(SocialNetworkAPIClient, 'sign_in')
    def test_sign_in(self, mock_sign_in):
        mock_sign_in.return_value = 'sOmEkEy228332'
        response = self.client.sign_in(username='username', password='password')
        self.assertEqual(response, mock_sign_in.return_value)

    @patch.object(SocialNetworkAPIClient, 'create_post')
    def test_create_post(self, mock_create_post):
        self.client.create_post(username='username', password='password', post_payload={'some': 'post'})
        mock_create_post.assert_called_with(username='username', password='password', post_payload={'some': 'post'})

    @patch.object(SocialNetworkAPIClient, 'like_post')
    def test_like_post(self, mock_like_post):
        self.client.like_post(username='username', password='password', pk=2)
        mock_like_post.assert_called_with(username='username', password='password', pk=2)
