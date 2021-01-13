import requests

print(requests.__version__)
print(requests.get('http://www.google.com/').status_code)

script = requests.get('https://raw.githubusercontent.com/alexbali/cmput_401_lab1/master/test.py?token=APMEG62VD34RLHWVY3H4WZ27747PS')
open('script_test.txt','w+').write(script.text)

print(script.text)