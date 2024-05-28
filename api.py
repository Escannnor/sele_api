# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys


# url = 'https://downloadwella.com/kaoaeztlu62g/Orion.and.the.Dark.(NKIRI.COM).2024.NF.WEBRip.DOWNLOADED.FROM.NKIRI.COM.mkv.html'
# driver = webdriver.Edge()

# driver.get(url)
# time.sleep(20)
# driver.maximize_window()
# # window = driver.find_element(By.TAG_NAME, 'html')
# # window.send_keys(Keys.PAGE_DOWN)
# time.sleep(20)
# print("Done")


import requests

url = 'https://dummyjson.com/products'
response = requests.get(url)
data = response.json()
# print(data)
for x in data['products']:
    title = x['title']
    img = x['images'][0]
    print(f'{title} has image {img}')
    
import requests

ref = None


# class Payment:
#     def __init__(self,key,email,amounts):
#         self.key = key
#         self.email = email
#         self.amounts = amounts
        
#     def pay(self):
#         url = "https://api.paystack.co/transaction/initialize"
#         data = {
#             'email': self.email,
#             'amount' : self.amounts * 100
#         }
        
#         headers = {
#             "Authorization": 'Bearer ' + self.key,
#             "Content-Type" : 'application/json'
#         }
        
#         response = requests.post(url, headers=headers, json=data)
#         if response.status_code == 200:
#             data = response.json() 
#             ref = data['data']['reference']
#             auth_link = data['data']['authorization_url']
#             result = {
#                 'reference_id': ref,
#                 'auth_url': auth_link
#                 }
#             return data
            
#         else:
#             return ('Error:', response.status_code)

import requests

email = str(input())
sk = str(input())
amount = int(input())
url = ''
data = {
    'email': email,
    'amount': amount * 100
}

header = {
    'Authorization': 'Bearer'+ sk,
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=header, data=data)