# Random Wallpaper Changer

This script downloads a random image from the internet and sets it as the desktop wallpaper on a Windows machine.

## Features

- Downloads a random image from [Picsum](https://picsum.photos/).
- Sets the downloaded image as the desktop wallpaper.

## Prerequisites

- Python 3.6 or higher
- `requests` library

## Installation

1. Clone the repository or download the script.
2. Install the required library using pip:
   ```bash
   pip install requests
   ```

## Usage

1. Run the script:
   ```bash
   python program.py
   ```
2. The script will download a random image and set it as your desktop wallpaper.

## Code Explanation

### Main Script

```python
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
```

### Explanation

- **Imports**: The script imports necessary libraries including `requests`, `ctypes`, and `os`.
- **download_random_image Function**: This function downloads a random image from Picsum and saves it as `random_wallpaper.jpg`. It returns the absolute path of the downloaded image.
- **set_wallpaper Function**: This function sets the downloaded image as the desktop wallpaper using the `ctypes` library.
- **Main Execution**: The script downloads a random image and sets it as the wallpaper if the download is successful.

## License

This project is licensed under the MIT License.
