import requests as rq 
import concurrent.futures as cf 
from Judiciary_Scraper.utils.imports import * 
from Judiciary_Scraper.utils.config_variables import *

## find file directory S
def find_file(filename, search_path):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

## find path from logs file directory   
search_path = '/' 
filename = 'test.log'
print("search directory")
file_path = find_file(filename, search_path)

## verify if path exists
if file_path:
    print(f'Found File: {file_path}')
    logging.basicConfig(filename=file_path, level=logging.INFO)
else:
    print('File not found')


## ===========================//===========================


## get response to url
def fetch_url(url):
    response = rq.get(url)
    return {'url': url, 'status_code': response.status_code, 'content': response.text}

## generate multiple urls
all_url = [URL for URL in range(1, 21)]

## enable multiple threads per run start to all responses
with cf.ThreadPoolExecutor(max_workers=20) as executor:
    futures = [executor.submit(fetch_url, URL) for url in all_url]
    
logging.info(f"--------------------------------------------------")

## save to response results in test.log file
for future in cf.as_completed(futures):
    result = future.result()
    # print(f"URL: {result['url']}, Status Code: {result['status_code']}")
    logging.info(f"URL: {result['url']}, Status Code: {result['status_code']}")
