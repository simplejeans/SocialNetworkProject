from requests import request, Response


class SocialNetworkAPIClient:
    sign_up_url = "http://127.0.0.1:8000/api/users/register/"
    create_post_url = "http://127.0.0.1:8000/api/posts/"
    sign_in_url = "http://127.0.0.1:8000/api/users/token/"

    @staticmethod
    def client(method: str, url: str, headers: dict, json: dict) -> Response:
        return request(method=method, url=url, headers=headers, json=json)

    def sign_up(self, username: str, password: str) -> None:
        data = {"username": username, "password": password, "password2": password}
        self.client(method="post", url=self.sign_up_url, headers={}, json=data)

    def sign_in(self, username: str, password: str) -> str:
        data = {"username": username, "password": password}
        response = self.client(method="post", url=self.sign_in_url, headers={}, json=data)
        access_token = response.json().get("access")
        return access_token

    def create_post(self, username: str, password: str, post_payload: dict):
        access_token = self.sign_in(username=username, password=password)
        data = post_payload
        response = self.client(method="post", url=self.create_post_url,
                               headers={"Authorization": f"Bearer {access_token}"}, json=data)
        return response.json()

    def get_like_url(self, pk: int) -> str:
        return f"http://127.0.0.1:8000/api/posts/{pk}/like/"

    def like_post(self, username: str, password: str, pk: int):
        access_token = self.sign_in(username=username, password=password)
        create_like_url = self.get_like_url(pk=pk)
        self.client(method="post", url=create_like_url,
                    headers={"Authorization": f"Bearer {access_token}"}, json={})
