# Є вiдкритий API NASA який дозволяє за певними параметрами отримати данi у виглядi JSON про фото зробленi ровером
# “Curiosity” на Марсi. Серед цих даних є посилання на фото якi потрiбно розпарсити i потiм за допомогою додаткових
# запитiв скачати i зберiгти цi фото як локальнi файли mars_photo1.jpg , mars_photo2.jpg . Завдання потрiбно
# зробити використовуючи модуль requests

import requests
from pathlib import Path


url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

download_folder = Path('C:\\Users\\007\\PycharmProjects\\homeworks\\lesson19\\mars_photos')
download_folder.mkdir(parents=True, exist_ok=True)

response = requests.get(url, params=params)

if response.status_code == 200:
    try:
        data = response.json()
        photos = data.get('photos', [])
        if photos:
            for index, photo in enumerate(photos[:5], start=1):
                img_url = photo['img_src']
                img_response = requests.get(img_url)

                if img_response.status_code == 200:
                    file_name = f"mars_photo{index}.jpg"
                    file_path = download_folder / file_name

                    with file_path.open('wb') as img_file:
                        img_file.write(img_response.content)

                    print(f"Photo saved as {file_name}")
                else:
                    print(f"We have a mistake while downloading  {index}: {img_url}")
        else:
            print("No photos found.")
    except ValueError as result:
        print(f"JSON parsing error: {result}")
else:
    print(f"Response error: {response.status_code}")
