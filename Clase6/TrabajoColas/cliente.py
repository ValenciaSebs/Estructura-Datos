import requests

url = 'https://cuddly-telegram-7vppw459wxjfp57r-8000.app.github.dev/'

# ejemplo request en GET
r = requests.get(url)
print(r.text)

# ejemplo request en POST
r = requests.post(url + 'encolar', json={'nombre': 'Juan', 'productos': ['manzana', 'pera'],"Documento":123456})
r = requests.post(url + 'encolar', json={'nombre': 'Sebastian', 'productos': ['Melon'],"Documento":36984})
r = requests.post(url + 'encolar', json={'nombre': 'Tomas', 'productos': ['Aguacate'],"Documento":785214})
r = requests.post(url + 'encolar', json={'nombre': 'Jafir', 'productos': ['Morcilla'],"Documento":741258})
print(r.text)