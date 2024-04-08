import requests


# try:
#     response = requests.get('https://gitlab.ru', timeout=1)
#     print(response.status_code)
# except requests.exceptions.ReadTimeout as ex:
#     print(ex)

# response = requests.get('https://httpbin.org/basic-auth/user/passwd', auth=('user', 'passwd'))
# print(response.request.headers)

class MyAuth(requests.auth.AuthBase):
    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password

    def __call__(self, r):
        # r.headers['Authorization'] = f'Basic {self.username}:{self.password}'
        return r


url = 'https://httpbin.org/get'
response = requests.get(url, auth=MyAuth())
print(response.text)
