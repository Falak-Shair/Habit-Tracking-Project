import requests
from datetime import datetime


USER_NAME = "falak"
TOKEN = "lkjhgfdsazxcvbnm"
GRAPH_Id = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

users_params = {
    "token": USER_NAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=users_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_Id,
    "name": "Codding Graph",
    "unit": "hour",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_Id}"

today = datetime.today()

graph_content = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you study today.")
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)


# Updating any pixel

# yesterday = datetime(year=2021, month=9, day=27)
# update_graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_Id}/{yesterday.strftime('%Y%m%d')}"
# updated_content = {
#     "quantity": "7"
# }
#
# update_graph = requests.put(url=update_graph_endpoint, json=updated_content, headers=headers)
# print(update_graph.text)


# Deleting any pixel

# delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_Id}/{yesterday.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)