import requests
import json
Base ="http://127.0.0.1:5000/"
# response = requests.get(Base+"/first/nowkshi")
# response = requests.put(Base+"/second",{"nowkshi":"hi"})
data = {
    'name': 'nowkshi',
    'dept': 'SEE',
    'session': 'lpl'
}
json_data = json.dumps(data)
headers = {
    'Content-Type': 'application/json'
}
response = requests.put(Base+"/add_student/1",data=json_data, headers=headers)
print(response.json())