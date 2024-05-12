# just exercise in HTTP methods

import datetime

import requests

pixela_endpoint = "https://pixe.la/v1/users"
USER_NAME = "tommy2ragnar"
TOKEN = "mytoken4Pixela"

user_params = {
    "token" : TOKEN,
    "username" : USER_NAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}
#created account on pixela
# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_params = {
    "id" : "graph1",
    "name" : "My Study graph",
    "unit" : "Hours",
    "type" : "int",
    "color" : "sora",

}

headers = {
    "X-USER-TOKEN" : TOKEN
}
#
# response = requests.post(graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/graph1"
today = datetime.datetime.today().strftime("%Y%m%d")
pixel_params = {
    "date" : today,
    "quantity": "5",
}
#
# response = requests.post(url=pixel_endpoint,json=pixel_params, headers=headers)
# print(response.text)

update_endpoint = f"{pixel_endpoint}/{today}"

new_pixel_data = {
    "quantity" : "2"
}
#
# response = requests.put(url=update_endpoint,json=new_pixel_data, headers=headers)
# print(response)

delete_endpoint = update_endpoint
response = requests.delete(update_endpoint,headers=headers)
print(response)

