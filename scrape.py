import requests
from bs4 import BeautifulSoup

def scrape():
    url = 'https://www.gsmarena.com/xiaomi_redmi_pad_pro-review-2718.php'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.select_one('h1').text
    text = soup.select_one('p').text

    print(title)
    print(text)

    comment_divs = soup.find_all('div', class_='review-body clearfix')

    # Extract and print the comments
    for idx, div in enumerate(comment_divs, start=1):
        comment_text = div.get_text(strip=True)
        print(f"Comment {idx}: {comment_text}")

if __name__ == '__main__':
    scrape()