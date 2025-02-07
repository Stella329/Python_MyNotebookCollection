# Pixela HOW TO USE: https://pixe.la/
# Pixela API Documentation: https://docs.pixe.la/
# view the graph: https://pixe.la/v1/users/<username>/graphs/<graphID>.html ==> https://pixe.la/v1/users/xiaopanda/graphs/graph-1.html
# my_profile_page: https://pixe.la/@xiaopanda

import requests
import datetime as dt

USERNAME='xiaopanda'
TOKEN='19953329'
GRAPH_ID='graph-1'

pixela_endpoint = 'https://pixe.la/v1/users'

today_obj = dt.date.today()  ## output: 2024-06-05
today = str(today_obj).replace('-','') # str.replace(old,new,count); YYYYMMMDD


#TODO 1 create a user
parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

p_respond = requests.post(url=pixela_endpoint,json=parameters)
print(p_respond.text)


#TODO 2 create a graph
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_header = {
    'X-USER-TOKEN': TOKEN,
}
graph_params = { #graph configuration
    'id': 'graph-1', # an ID for identifying the pixelation graph
    'name': 'Excercise-Tracking',
    'unit': 'day', # the quantity recorded in the pixelation graph
    'type': 'int', #type of quantity; Only int or float
    'color': 'ajisai',
}

g_response = requests.post(url=graph_endpoint, json=graph_params, headers=graph_header)
print(g_response.text)




#TODO 3 Post value to the graph: Post a Pixel, to habit graph of the date today
post_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
post_header={
    'X-USER-TOKEN': TOKEN,
}

post_params={
    'date': today,
    'quantity': '30',
}

post_response = requests.post(url=post_endpoint, json=post_params, headers=post_header)
print(post_response.text)


#TODO 4.1 Put: update the graph
graph_update_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
graph_update_header = {
    'X-USER-TOKEN': TOKEN,
}
graph_update_params = {
    'name':'Daily Booking Reading Tracker',
    'unit': 'page',
}

graph_update_response = requests.put(url=graph_update_endpoint, json=graph_update_params, headers=graph_update_header)
print(graph_update_response.text)


#TODO 4.2 Put: update the previous data (update the pixel)
data_update_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}'
header={
    'X-USER-TOKEN': TOKEN,
}
data_update_params = {
    'quantity': '4',
}
data_update_response = requests.put(url=data_update_endpoint, json=data_update_params, headers=header)
print(data_update_response.text)


# #TODO 5 Delete a pixel
# delete_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}'
# header={
#     'X-USER-TOKEN': TOKEN,
# }
# response = requests.put(url=data_update_endpoint, headers=header)
# print(response.text)
