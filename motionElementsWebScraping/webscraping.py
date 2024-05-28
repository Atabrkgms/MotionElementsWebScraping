import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome( options=options)

base_url = 'https://www.motionelements.com/tr/search/video?s=&page='
total_pages = 200  

video_links = []

for page in range(1, total_pages + 1):
    url = f"{base_url}{page}"
    driver.get(url)
    time.sleep(5) 
    
    html_content = driver.page_source
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    product_grid_items = soup.find_all('div', class_='product-grid-item')
    
    for item in product_grid_items:
        a_tag = item.find('a', class_='product-click')
        if a_tag and 'href' in a_tag.attrs:
            video_links.append(a_tag['href'])
    
    print(f"Page {page} done.")

driver.quit()

df = pd.DataFrame(video_links, columns=['Video Link'])

df.to_csv('video_links.csv', index=False, encoding='utf-8')

print("All video links have been saved to video_links.csv.")
