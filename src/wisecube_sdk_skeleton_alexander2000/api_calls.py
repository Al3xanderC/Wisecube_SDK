import requests

expected_status_codes = [200, 201, 204]


def create_api_call(payload, headers, url):
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        response.raise_for_status()
        if response.status_code in expected_status_codes:
            print("Response Status Code:", response.status_code)
            print("Response Body:", response.text)
            return response
        else:
            print(f"Unexpected Status Code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print("An error occurred during the API call:", e)
        return None
