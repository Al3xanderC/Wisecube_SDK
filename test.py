from src.wisecube_sdk_skeleton_alexander2000.wisecube_sdk import WisecubeClient


client = WisecubeClient("user", "pwd", "key").client
# client = WisecubeClient().client

print(type(client))

client.search("e")

