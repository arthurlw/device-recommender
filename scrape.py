import requests
from bs4 import BeautifulSoup
import re

class GSMArenaScraper:
    BASE_URL = "https://www.gsmarena.com/"
    
    def __init__(self, device_name):
        self.device_name = device_name
        self.device_page_url = None
        self.review_page_url = None

    def clean_url_text(self, url_text):
        """Clean text from URL to match device names"""
        # Remove the model number suffix (e.g., -12771)
        text = re.sub(r'-\d+$', '', url_text)
        # Replace underscores with spaces
        text = text.replace('_', ' ')
        return text.lower().strip()

    def clean_device_name(self, name):
        """Clean and standardize device name for matching"""
        # Remove any special characters and extra spaces
        cleaned = ' '.join(name.lower().split())
        return cleaned

    def find_device_page(self):
        """
        Finds the device page URL for the given device name.
        """
        # Convert spaces to plus signs for the search URL
        search_term = self.device_name.replace(' ', '+')
        search_url = f"{self.BASE_URL}results.php3?sQuickSearch=yes&sName={search_term}"
        
        try:
            response = requests.get(search_url)
            response.raise_for_status()  # Raise an exception for bad status codes
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all phone entries
            phone_entries = soup.find_all('div', class_='makers')
            if not phone_entries:
                return None

            cleaned_search = self.clean_device_name(self.device_name)
            
            for phones in phone_entries:
                links = phones.find_all('a')
                for link in links:
                    href = link.get('href', '')
                    link_text = self.clean_url_text(href)
                    
                    # For iPhone, ensure exact model match
                    if 'iphone' in cleaned_search:
                        iphone_model = re.search(r'iphone\s*(\d+)(?!\s*pro)', cleaned_search)
                        link_model = re.search(r'iphone\s*(\d+)(?!\s*pro)', link_text)
                        
                        if iphone_model and link_model and iphone_model.group(1) == link_model.group(1):
                            self.device_page_url = self.BASE_URL + href
                            return self.device_page_url
                    
                    # For other devices, match all words
                    else:
                        search_words = cleaned_search.split()
                        if all(word in link_text for word in search_words):
                            cleaned_link = self.clean_url_text(href)
                            # Additional check to avoid partial matches
                            if len(cleaned_link.split()) == len(search_words):
                                self.device_page_url = self.BASE_URL + href
                                return self.device_page_url
            
            return None
            
        except requests.RequestException as e:
            print(f"Error fetching search results: {e}")
            return None

    def find_review_page(self):
        """
        Finds the review page URL from the device page.
        """
        if not self.device_page_url:
            return None
        
        try:
            response = requests.get(self.device_page_url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            meta_links = soup.find('ul', class_='article-info-meta')
            if meta_links:
                review_link = meta_links.find('li', class_='article-info-meta-link-review')
                if review_link and review_link.find('a'):
                    self.review_page_url = self.BASE_URL + review_link.find('a')['href']
                    return self.review_page_url
            return None
            
        except requests.RequestException as e:
            print(f"Error fetching device page: {e}")
            return None

    def scrape_reviews(self):
        """
        Scrapes reviews from the review page.
        """
        if not self.review_page_url:
            return []
        
        try:
            response = requests.get(self.review_page_url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            reviews = []
            # Look for review content in article body
            article = soup.find('div', class_='article-content')
            if article:
                review_elements = article.find_all('p')
                for review in review_elements:
                    if review.text.strip():
                        reviews.append(review.text.strip())
            return reviews
            
        except requests.RequestException as e:
            print(f"Error fetching review page: {e}")
            return []

if __name__ == "__main__":
    # Test cases
    test_devices = [
        "Samsung Galaxy S24 Ultra",
        "iPhone 16",
    ]
    
    for device in test_devices:
        print(f"\nTesting device: {device}")
        scraper = GSMArenaScraper(device)
        device_page = scraper.find_device_page()
        
        if device_page:
            print(f"Found device page: {device_page}")
            review_page = scraper.find_review_page()
            if review_page:
                print(f"Found review page: {review_page}")
                reviews = scraper.scrape_reviews()
                print(f"Number of review paragraphs found: {len(reviews)}")
            else:
                print("No review page found")
        else:
            print("Device page not found")