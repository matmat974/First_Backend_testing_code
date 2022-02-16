import requests
import json



response = requests.get('https://api.kumuapi.com/v1/sms/retrieve-otp-codes',
             params={'cellphone': '0000432222', 'country_code': '63', 'rate_limit': '2'},
             headers={'otp-secret-key': '782a6798b2f0ce9a01be38af39ef34bd'})

print(response.text)
print(type(response.text))

# dict = json.loads(response.text)
# print(type(dict))
# print(dict['data'][1]['verification_code'], dict['data'][1]['created_at'])
# list = dict['data']
#
# print(type(list))
# print(list[0]['verification_code']
print("hello world")
print("hello 1")
print("hello 2")