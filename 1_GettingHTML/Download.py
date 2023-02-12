import  requests

url = 'https://www.pagina12.com.ar/'

p12 = requests.get(url)
print(p12.status_code)

#print(p12.text) 

p12.content # Used for obtain bytes and get images, videos etc

#print(p12.headers)

# Notify you the server knows this request its from
# an automatize software using an specific library
print(p12.request.headers)

