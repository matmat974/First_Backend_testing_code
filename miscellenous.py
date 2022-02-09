import requests

#http://rahulshettyacademy.com
#'visit-month'
#
# res = requests.get('http://rahulshettyacademy.com', allow_redirects=True, cookies={'visit-month' : 'February'}, timeout=1)
#
# # print(res.history)
# print(res.status_code)



# cook = {'visit-month' : 'February'}
# se = requests.session()
# se.cookies.update({'visit-year' : '2022'})
# response = se.get('https://httpbin.org/cookies', cookies=cook)
#
# print(response.history)
# print(response.status_code)
# print(response.text)


url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files = {'file': open('/Users/matthew/Downloads/DOG.webp', 'rb')}
r = requests.post(url,files=files)
print(r.status_code)
print(r.text)
