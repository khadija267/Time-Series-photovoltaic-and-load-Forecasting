### Unit and integration tests ###
#"API endpoint tests","Model inference tests","Utility function tests"

import requests

files = {'file': open('test.csv', 'rb')}
response = requests.post('http://localhost:8000/predict/', files=files)
print(response.json())