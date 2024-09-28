# У venv Python встановiть Flask за допомогою команди pip install flask
# Створiть у окремiй директорiї файл app.py та скопіюйте у нього код файлу app.py який приведено нижче в початкових даних.
# Запустiть http сервер за допомогою команди python app.py
# Сервер стартує за базовою адресою http://127.0.0.1:8080
# Враховуючи документацію яку наведено нижче вам потрібно написати код який використовуючи модуль request
# зробить через POST upload якогось зображення на сервер, за допомогою GET отримає посилання на цей файл и
# потім за допомогою DELETE зробить видалення файлу з сервера

import requests


base_url = 'http://127.0.0.1:8080'
image_path = 'C:\\Users\\007\\PycharmProjects\\homeworks\\lesson19\\mars_photos\\mars_photo1.jpg'

# 1. (POST)
upload_url = f'{base_url}/upload'
with open(image_path, 'rb') as image_file:
    files = {'image': image_file}
    response = requests.post(upload_url, files=files)

if response.status_code == 201:
    image_url = response.json()['image_url']
    print(f"Image {image_url} has been downloaded")
else:
    print(f"Error downloading image: {response.status_code}")
    exit()


filename = image_url.split('/')[-1]

# 2. GET
get_image_url = f'{base_url}/image/{filename}'
headers = {'Content-Type': 'text'}  # Получить URL
response = requests.get(get_image_url, headers=headers)

if response.status_code == 200:
    print(f"Image URL: {response.json()['image_url']}")
else:
    print(f"Getting error image URL: {response.status_code}")


# 3. DELETE
delete_image_url = f'{base_url}/delete/{filename}'
response = requests.delete(delete_image_url)

if response.status_code == 200:
    print(f"Image {filename} has been deleted.")
else:
    print(f"Error deleting image: {response.status_code}")