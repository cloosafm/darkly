import requests
from bs4 import BeautifulSoup
import os



def find_files(url, visited=None, depth=0, max_depth=26):
    if visited is None:
        visited = set()
    
    if depth > max_depth:
        print(f"Max depth reached at {url}")
        return
    
    if url in visited:
        return
    
    visited.add(url)
    
    try:
        req = requests.get(url)
        req.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return
    
    soup = BeautifulSoup(req.content, 'html.parser')

    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.endswith('/'):
            find_files(url + href, visited, depth + 1, max_depth)
        elif 'flag' in href:
            file_url = url + href

            with open('href.txt', 'a') as f:
                f.write(f"{file_url}\n")
                file_content_req = requests.get(file_url)
                file_content = file_content_req.text
                f.write(f"{file_content}\n")

    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.endswith('/'):
            find_files(url + href, visited, depth + 1, max_depth)
        elif href:
            file_url = url + href
            try:
                file_req = requests.head(file_url)
                file_req.raise_for_status()
                file_size = int(file_req.headers.get('content-length', 0))
                if file_size > 0:
                    file_content_req = requests.get(file_url)
                    file_content_req.raise_for_status()
                    file_content = file_content_req.text
                    with open('found.txt', 'a') as f:
                        f.write(f"{file_url}\n")
                        f.write(f"{file_content}\n")
            except requests.exceptions.RequestException as e:
                print(f"Failed to get file info: {e}")

# Starting URL
url = 'http://192.168.56.101/.hidden/'

find_files(url)
