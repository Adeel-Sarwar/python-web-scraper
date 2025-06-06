import requests
from bs4 import BeautifulSoup
import csv

def scrape_books():
    url = "https://books.toscrape.com"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        books = soup.find_all('article', class_='product_pod')
        
        data = []
        for book in books:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            data.append({'title': title, 'price': price})
        
        with open('books.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['title', 'price'])
            writer.writeheader()
            writer.writerows(data)
        
        print(f"Scraped {len(data)} books and saved to books.csv")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_books()