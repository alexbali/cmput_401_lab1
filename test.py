import requests

print(requests.__version__)

print(requests.get('http://www.google.com/').status_code)