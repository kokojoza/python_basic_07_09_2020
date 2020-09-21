import os
import requests


def get_htm():
    url = 'https://geekbrains.ru/'
    response = requests.get(url)
    return response.text


def get_image(url):
    response = requests.get(url)
    return response.content


def save_html_to_file(file_path, htm_text):
    with open(file_path, 'wb', encoding='UTF-8') as file:
        file.write(htm_text)


def save_image(file_path, image_bytes):
    with open(file_path, 'w') as file:
        file.write(image_bytes)


if __name__ == '__main__':
    img_url = 'https://d2xzmw6cctk25h.cloudfront.net/geekbrains/public/ckeditor_assets/pictures/9558/retina-c94f3091e3c68919cbdfadb7c530d18e.png'
    file_name = 'temp_gb_main.html'
    file_folder = os.path.dirname(__file__)
    file_path = os.path.join(file_folder, file_name)
    image_path = os.path.join(file_folder, 'retina-c94f3091e3c68919cbdfadb7c530d18e.png')
    # html_text = get_htm()
    # save_html_to_file(file_path, html_text)
    img_bytes = get_image(img_url)
    save_image(image_path, img_bytes)
