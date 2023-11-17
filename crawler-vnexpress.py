import os
import tqdm
import requests
from bs4 import BeautifulSoup
import re

total_pages = 20

for i in tqdm.tqdm(range(1, total_pages + 1)):
    content = requests.get(f"   ").content
    soup = BeautifulSoup(content, "html.parser")
    wrapper = soup.find('body')
    images = wrapper.find_all("img")

    for image in images:
        imgData = image['src']
        print(imgData)

        if "data:image" not in imgData:
            if imgData:
                downloadPath = 'D:\\UIT\\Semester_5\\IR\\images\\'

                # Extract filename from URL
                filename = os.path.basename(imgData)
                cleaned_filename = re.sub(r'[\\/:*?"<>|&=]', '', filename)

                # Get file extension
                file_extension = os.path.splitext(cleaned_filename)[1].lower()

                # Change extension to .jpg or .png
                if file_extension not in ['.jpg', '.png']:
                    file_extension = '.jpg'  # Change to '.png' if you prefer PNG format

                # Create full file path with new extension
                new_filename = os.path.splitext(cleaned_filename)[0] + file_extension
                file_path = os.path.join(downloadPath, new_filename)

                # Download and save the image
                response = requests.get(imgData)
                with open(file_path, "wb") as file:
                    file.write(response.content)

                print(f"Image '{imgData}' downloaded and saved as '{new_filename}'")
