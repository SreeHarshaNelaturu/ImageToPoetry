import requests
r = requests.post(
    "https://api.deepai.org/api/neuraltalk",
    files={
        'image': open('/Users/christina/Desktop/longboard-surfer-paul-topp.jpg', 'rb'),
    },
    headers={'api-key': '8a8842f4-e2fc-45f4-b2b9-4c24903cca76'}
)
data = r.json()
print(data['output'])
