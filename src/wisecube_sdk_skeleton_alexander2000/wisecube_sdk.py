from Wisecube_SDK.src.wisecube_sdk_skeleton_alexander2000 import string_query
from Wisecube_SDK.src.wisecube_sdk_skeleton_alexander2000 import api_calls
import requests
import json


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
        return api_calls.create_api_call(payload, self.headers, self.url, "data")


class AuthClient:
    def __init__(self, username, password, api_key):
        self.username = username
        self.password = password
        self.api_key = api_key
        self.url = "https://api.wisecube.ai/orpheus/graphql"
        self.client_id = "1mbgahp6p36ii1jc851olqfhnm"

    def create_token(self):
        # curl -X POST --data @eReteta_user.json -H 'X-Amz-Target: AWSCognitoIdentityProviderService.InitiateAuth' -H
        # 'Content-Type: application/x-amz-json-1.1' https://cognito-idp.us-east-2.amazonaws.com/ | jq -r
        # '.AuthenticationResult.AccessToken'

        payload = {
            "AuthParameters": {
                "USERNAME": "cristi@wisecube.ai",
                "PASSWORD": "xdPhQgi8NK9r7tq"
            },
            "AuthFlow": "USER_PASSWORD_AUTH",
            "ClientId": "1mbgahp6p36ii1jc851olqfhnm"
        }
        headers = {"X-Amz-Target": "AWSCognitoIdentityProviderService.InitiateAuth",
                   "Content-Type": "application/x-amz-json-1.1"
                   }
        cognito_url = "https://cognito-idp.us-east-2.amazonaws.com/"

        response = api_calls.create_api_call(payload, headers, cognito_url, "json")

        token = json.loads(response.text)["AuthenticationResult"]["AccessToken"]

        return token

    def get_headers(self):
        return {
            'Authorization': 'Bearer {}'.format(self.create_token()),
            'Content-Type': 'application/json',
            'x-api-key': self.api_key
        }

    def search(self, text):
        print(text)

    def graph(self):
        print("Auth client graph")

    def qa(self, text):
        headers = self.get_headers()
        payload = string_query.payload
        response = api_calls.create_api_call(payload, headers, self.url, "data")
        print(response.text)
