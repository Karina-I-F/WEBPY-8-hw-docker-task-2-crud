import requests

HOST = 'http://127.0.0.1:8000/api/v1/'

#  get urls
# resp = requests.get(f'{HOST}').json()
# print(resp)

# get all products
resp = requests.get(f'{HOST}products/').json()
print(resp)

# create product 1
resp = requests.post(f'{HOST}products/',
                     json={
                         "title": "Помидор",
                         "description": "Лучшие помидоры на рынке"}).json()
print(resp)

# create product 2
resp = requests.post(f'{HOST}products/',
                     json={
                         "title": "Ежевика",
                         "description": "Сочная и спелая"}).json()
print(resp)

# create product 3
resp = requests.post(f'{HOST}products/',
                     json={
                         "title": "Клубника",
                         "description": "Лучшая на рынке"}).json()
print(resp)

# create product 4
resp = requests.post(f'{HOST}products/',
                     json={
                         "title": "Авокадо",
                         "description": "Спелые авокадо, идеальные для завтрака"}).json()
print(resp)

# get product by id
resp = requests.get(f'{HOST}products/3').json()
print(resp)

# search for products by title and description
resp = requests.get(f'{HOST}products/?search=помидор').json()
print(resp)

# update product
resp = requests.patch(f'{HOST}products/1/',
                      json={
                          "description": "Самые сочные и ароматные помидорки"}).json()
print(resp)

# delete product by id
# resp = requests.delete(f'{HOST}products/4/')
# print(resp.status_code)

# get all stocks
resp = requests.get(f'{HOST}stocks/').json()
print(resp)

# create stock 1
resp = requests.post(f'{HOST}stocks/',
                     json={
                         "address": "мой адрес не дом и не улица, мой адрес сегодня такой: www.ленинград-спб.ru3",
                         "positions": [{
                             "product": 2,
                             "quantity": 250,
                             "price": 120.50
                         },
                             {
                                 "product": 3,
                                 "quantity": 100,
                                 "price": 180
                             }]
                     }).json()
print(resp)

# create stock 2
resp = requests.post(f'{HOST}stocks/',
                     json={
                         "address": "г. N, Фруктовый рынок",
                         "positions": [{
                             "product": 2,
                             "quantity": 1000,
                             "price": 200
                         },
                             {
                                 "product": 3,
                                 "quantity": 2000,
                                 "price": 180
                             }]
                     }).json()
print(resp)

# create stock 3
resp = requests.post(f'{HOST}stocks/',
                     json={
                         "address": "г. K, Фермерский рынок",
                         "positions": [{
                             "product": 1,
                             "quantity": 250,
                             "price": 90.50
                         },
                             {
                                 "product": 3,
                                 "quantity": 1050,
                                 "price": 185
                             }]
                     }).json()
print(resp)

# get stock by id
resp = requests.get(f'{HOST}stocks/2').json()
print(resp)

# search for stocks where there is a certain product
resp = requests.get(f'{HOST}stocks/?products=2').json()
print(resp)

# update stock
resp = requests.patch(f'{HOST}stocks/3/',
                      json={
                          "positions": [{
                              "product": 2,
                              "quantity": 100,
                              "price": 130.80
                          },
                              {
                                  "product": 1,
                                  "quantity": 243,
                                  "price": 145}]
                      }).json()
print(resp)

# delete stock by id
# resp = requests.delete(f'{HOST}stocks/1/')
# print(resp.status_code)
