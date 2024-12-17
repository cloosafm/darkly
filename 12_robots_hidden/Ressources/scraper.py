import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class Scraper:
    def __init__(self, url):
        self.url = url
        self.visited_urls = set()
        self.files = set()
        self.max_depth = 0
        self.content_list = []
        self.session = requests.Session()  # helps clean up connections to avoi all the max-tries srrors...

    def download_url(self, url):
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Failed to fetch {url}: {e}")
            return ""

    def get_linked_urls(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href != "../":
                href = urljoin(url, href)
                if not href.endswith('/'):
                    self.files.add(href)
                elif href.endswith('/'):
                    yield href

    def crawl(self, url, depth):
        if url in self.visited_urls:
            return
        self.visited_urls.add(url)

        if depth > self.max_depth:
            self.max_depth = depth

        html = self.download_url(url)
        if not html:
            return

        for linked_url in self.get_linked_urls(url, html):
            self.crawl(linked_url, depth + 1)

    def spider(self):
        self.crawl(self.url, 0)
        print(f"Maximum depth: {self.max_depth}\n")

    def print_files(self):
        for url in self.files:
            try:
                response = self.session.get(url)
                response.raise_for_status()
                content = response.text
                if content not in self.content_list:
                    self.content_list.append(content)
                    print(content)
                    print('---------------------------------')
            except requests.RequestException as e:
                print(f"Failed to fetch file {url}: {e}")

    def close(self):
        self.session.close()


if __name__ == '__main__':
    scraper_instance = Scraper(url='http://192.168.56.101/.hidden/')
    try:
        scraper_instance.spider()
        scraper_instance.print_files()
    finally:
        scraper_instance.close()
