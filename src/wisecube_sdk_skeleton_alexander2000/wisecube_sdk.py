from Wisecube_SDK.src.wisecube_sdk_skeleton_alexander2000 import string_query
from Wisecube_SDK.src.wisecube_sdk_skeleton_alexander2000 import api_calls


class WisecubeClient:
    def __init__(self, *args):
        if len(args) == 0:
            open_url = "http://127.0.0.1:5000/api/endpoint"
            self.client = OpenClient(open_url)
        elif len(args) == 3:
            self.client = AuthClient(*args)
        else:
            raise Exception("Invalid args")


class OpenClient:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'Content-Type': 'application/json'
        }

    def search(self, text):
        # payload = string_query.qa_query.format(QUERY=text)
        payload = "QUERY"
        print(payload)
        print(self.headers)
        print("Open client search")

    def qa(self, text):
        # payload = string_query.qa_query.format(QUERY=text)
        payload = "QUERY"
        return api_calls.create_api_call(payload, self.headers, self.url)


class AuthClient:
    def __init__(self, username, password, api_key):
        self.username = username
        self.password = password
        self.api_key = api_key
        self.url = "http://127.0.0.1:5000/api/endpoint"

    def create_token(self):
        print("create token {}".format(self.username))
        return "sdafsafawe"

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'x-api-key': self.api_key,
            "Authorization": "bearer {}".format(self.create_token())
        }

    def search(self, text):
        headers = self.get_headers()
        print(headers)

    def graph(self):
        print("Auth client graph")

    def qa(self, text):
        headers = self.get_headers()
        # payload = string_query.qa_query.format(QUERY=text)
        payload = "QUERY"
        return api_calls.create_api_call(payload, headers, self.url)
