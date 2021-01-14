import requests

print(requests.__version__)
print(requests.get('http://www.google.com/').status_code)

script = requests.get('https://raw.githubusercontent.com/alexbali/cmput_401_lab1/master/test.py')
print(script.text)