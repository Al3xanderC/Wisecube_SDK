import requests

# TODO validare erori si status code  partea de retry
def create_api_call(payload, headers, url):

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    return response