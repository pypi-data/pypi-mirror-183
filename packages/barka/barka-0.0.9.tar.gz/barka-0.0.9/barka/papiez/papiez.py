import requests

api_url = 'https://www.youtube.com/watch?v=mCUFL05rS5w'

def use_requests(api_url):
    response = requests.get(api_url)
    print(response)

def greet():
    print('hello world')

use_requests(api_url)
