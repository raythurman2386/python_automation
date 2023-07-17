import os, sys
import requests
from bs4 import BeautifulSoup


def download_images(url, folder="images"):
    try:
        os.makedirs(folder, exist_ok=True)
    except Exception as e:
        print(f"Error creating folder: {e}")
        return
    
    os.chdir(os.path.abspath(folder))
    
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        images = soup.find_all('img')
        
        for image in images:
            name = image['alt']
            link = image['src']
            
            try:
                with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
                    im = requests.get(link)
                    f.write(im.content)
                    print(f'Writing: {name}')
            except Exception as e:
                print(f"Error writing image '{name}': {e}")
    except Exception as e:
        print(f"Error requesting the URL: {e}")
            

if __name__ == "__main__":
    download_images(sys.argv[1])