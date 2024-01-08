def qa(response):
    return response.json()


def documents(response):
<<<<<<< Updated upstream:src/wisecube_sdk/create_response.py
    return response.json()["data"]["summaryInsights"][0]
=======
    return response.json()

>>>>>>> Stashed changes:src/create_response.py

def search_graph(response):
    return response.json()


def search_text(response):
    return response.json()