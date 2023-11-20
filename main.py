import requests
from bs4 import BeautifulSoup
import os


def download_webpage(url, local_filename):
    # Send a GET request
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the GET request was unsuccessful

    # Parse the webpage's content
    soup = BeautifulSoup(response.content, 'html.parser')

    # try:
    #     # Write the webpage's content to a local file
    #     with open(local_filename, 'w', encoding='utf-8') as file:
    #         file.write(str(soup))
    # except FileNotFoundError:
    #     print(local_filename)
    paths = local_filename.rsplit("/",1)
    if len(paths) == 2:
        if not os.path.exists(paths[0]):
            os.makedirs(paths[0])
        with open(local_filename, 'w', encoding='utf-8') as file:
            file.write(str(soup))
    else:
        with open(local_filename, 'w', encoding='utf-8') as file:
            file.write(str(soup))

# # Example usage:
# download_webpage('https://docs.okera.com/odas/latest/', 'local_file.html')

def extract_urls():

    url = 'https://docs.okera.com/odas/latest/'
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))
    # print(urls)
    local_filename = "/Users/sankarshpallela/Documents/sanky/work/2023/Nov/"
    for ur in urls:
        if ur != "":
            if ur[-1] == '/':
                ur = ur [0:-1]
            download_webpage(url+ur,local_filename+ur+".html")
    
extract_urls()