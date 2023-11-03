from Wisecube_SDK.src.wisecube_sdk_skeleton_alexander2000.wisecube_sdk import WisecubeClient
#RED = '\033[91m'
#RESET = '\033[0m'
#open_client = WisecubeClient()
auth_client = WisecubeClient('cristi@wisecube.ai', 'xdPhQgi8NK9r7tq', 'LUcIwKi1SY2bkQgji8uwA5SAYO20hu0n53Ew4Bdq')
response = auth_client.client.qa("what is covid ?")
print(response)
#(RED + "\n\nOPEN CLIENT SEARCH" + RESET)
#open_client.client.search('asd')
#print(RED + '\n\nOPEN CLIENT QA' + RESET)
#pen_client.client.qa('asd')



