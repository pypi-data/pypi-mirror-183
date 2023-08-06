import requests

API_URL = 'https://www.youtube.com/watch?v=0qzLRlQFFQ4'

def use_requests():
    response = requests.get(API_URL)
    print(response)

def greet():
    print('hello world')

use_requests()
