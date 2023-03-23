import os
import requests
from bs4 import BeautifulSoup

def download_images(url, folder):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for img in soup.findAll('img'):
        img_url = img.get('src')
        if img_url.startswith('http'):
            response = requests.get(img_url)
            filename = os.path.join(folder, img_url.split('/')[-1])
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f'Downloaded {filename}')

if __name__ == '__main__':
    url = input('Enter URL to download images from: ')
    folder = input('Enter folder to save images in: ')
    if not os.path.exists(folder):
        os.makedirs(folder)
    download_images(url, folder)
