<<<<<<< Updated upstream
from src import WisecubeClient

=======
from Wisecube_SDK.src.wisecube_sdk import WisecubeClient
>>>>>>> Stashed changes
RED = '\033[91m'
RESET = '\033[0m'
# open_client = WisecubeClient()
# (RED + "\n\nOPEN CLIENT SEARCH" + RESET)
# open_client.client.search('asd')
# print(RED + '\n\nOPEN CLIENT QA' + RESET)
# pen_client.client.qa('asd')
auth_client = WisecubeClient('cristi@wisecube.ai', 'xdPhQgi8NK9r7tq', 'LUcIwKi1SY2bkQgji8uwA5SAYO20hu0n53Ew4Bdq')
print(RED + "\n\nQA" + RESET)
docs = auth_client.client.qa("What is covid 19?")
print(docs)
print(RED + "\n\nDOCUMENTS" + RESET)
docs = auth_client.client.documents("What is covid 19?")
print(docs)
print(RED + "\n\nSEARCH_TEXT" + RESET)
docs = auth_client.client.search_text("What is covid 19?")
print(docs)
print(RED + "\n\nSEARCH GRAPH_TEXT" + RESET)
docs = auth_client.client.search_graph("What is covid 19?", 20)
print(docs)
print(RED + "\n\nSEARCH GRAPH_LINK" + RESET)
docs = auth_client.client.search_graph("http://www .wikidata.org/entity/Q27677605")
print(docs)