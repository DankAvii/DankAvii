Practical 7
pip install requests
pip install beautifulsoup4
Aim: Web Crawling and Indexing
∙ Develop a web crawler to fetch and index web pages.
∙ Handle challenges such as robots.txt, dynamic content, and crawling
delays
a] 
import requests
from bs4 import BeautifulSoup
import urllib3
 
# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
class WebCrawler:
 
    def __init__(self):
        self.visited_urls = set()
 
    def crawl(self, url, depth=2):
 
        if depth == 0 or url in self.visited_urls:
            return
 
        try:
            response = requests.get(url, verify=False)
 
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
 
                self.index_page(url, soup)
 
                self.visited_urls.add(url)
 
                for link in soup.find_all("a"):
                    new_url = link.get("href")
 
                    if new_url and new_url.startswith("http"):
                        print("Crawling:", new_url)
                        self.crawl(new_url, depth-1)
 
        except Exception as e:
            print("Error crawling", url, ":", e)
 
    def index_page(self, url, soup):
 
        title = soup.title.string if soup.title else "No title"
 
        paragraph = soup.find("p")
        paragraph_text = paragraph.get_text() if paragraph else "No paragraph found"
 
        print("\nIndexing:", url)
        print("Title:", title)
        print("First Paragraph:", paragraph_text)
        print("---------------------------")
 
 
if __name__ == "__main__":
 
    crawler = WebCrawler()
    crawler.crawl("https://www.example.com")
 

 

b]
 

import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urlparse
 
 
class WebCrawler:
 
    def __init__(self):
        self.visited_urls = set()
 
    def crawl(self, url, depth=3, delay=1):
 
        if depth == 0:
            return
 
        if url in self.visited_urls:
            return
 
        try:
            if not self.is_allowed_by_robots(url):
                print(f"Skipping {url} due to robots.txt rules")
                return
 
            response = requests.get(url)
 
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
 
                self.index_page(url, soup)
                self.visited_urls.add(url)
 
                for link in soup.find_all("a"):
                    new_url = link.get("href")
 
                    if new_url and new_url.startswith("http"):
                        time.sleep(delay)  # Delay between requests
                        self.crawl(new_url, depth - 1, delay)
 
        except Exception as e:
            print(f"Error crawling {url}: {e}")
 
    def is_allowed_by_robots(self, url):
 
        parsed_url = urlparse(url)
        robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
 
        try:
            response = requests.get(robots_url)
 
            if response.status_code == 200:
                robots_txt = response.text
 
                if "User-agent: *" in robots_txt:
                    start_index = robots_txt.find("User-agent: *")
                    end_index = robots_txt.find("User-agent:", start_index + 1)
 
                    if end_index == -1:
                        end_index = len(robots_txt)
 
                    relevant_section = robots_txt[start_index:end_index]
 
                    if "Disallow: /" in relevant_section:
                        return False
 
            return True
 
        except:
            return True
 
    def index_page(self, url, soup):
 
        title = soup.title.string if soup.title else "No title"
 
        paragraph = soup.find("p")
        paragraph_text = paragraph.get_text() if paragraph else "No paragraph found"
 
        print("\nIndexing:", url)
        print("Title:", title)
        print("First Paragraph:", paragraph_text)
        print("---------------------------")
 
 
if __name__ == "__main__":
 
    crawler = WebCrawler()
    crawler.crawl("https://10fastfingers.com/typing-test/english")
