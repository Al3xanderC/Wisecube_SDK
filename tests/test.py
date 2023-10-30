from Wisecube_SDK.src.wisecube_sdk_skeleton_alexander2000.wisecube_sdk import WisecubeClient
RED = '\033[91m'
RESET = '\033[0m'
open_client = WisecubeClient()
auth_client = WisecubeClient('usr', 'pass', 'key')

print(RED + "\n\nOPEN CLIENT SEARCH" + RESET)
open_client.client.search('asd')
print(RED + '\n\nOPEN CLIENT QA' + RESET)
open_client.client.qa('asd')

print(RED + '\n\nAUTH CLIENT CREATE_TOKEN' + RESET)
auth_client.client.create_token()
print(RED + '\n\nAUTH CLIENT GET_HEADER' + RESET)
auth_client.client.get_headers()
print(RED + '\n\nAUTH CLIENT GRAPH' + RESET)
auth_client.client.graph()
print(RED + '\n\nAUTH CLIENT QA' + RESET)
auth_client.client.qa('asd')
print(RED + '\n\nAUTH CLIENT SEARCH' + RESET)
auth_client.client.search('asd')
