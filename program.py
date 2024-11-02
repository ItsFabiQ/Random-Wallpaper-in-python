import requests
import ctypes
import os

def download_random_image():
    url = "https://picsum.photos/1920/1080"
    response = requests.get(url)
    if response.status_code == 200:
        with open("random_wallpaper.jpg", "wb") as file:
            file.write(response.content)
        return os.path.abspath("random_wallpaper.jpg")
    else:
        print("Failed to download image")
        return None

def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

if __name__ == "__main__":
    image_path = download_random_image()
    if image_path:
        set_wallpaper(image_path)
