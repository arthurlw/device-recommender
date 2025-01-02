from sentiment import ReviewSentimentAnalyzer
from scrape import GSMArenaScraper

device_name = input("Please input your device name: ")
scraper = GSMArenaScraper(device_name)

# Find the device page
device_page = scraper.find_device_page()
if device_page:
    print(f"Found device page: {device_page}")

    # Find the review page
    review_page = scraper.find_review_page()
    if review_page:
        print(f"Specific review page URL: {review_page}")

        # Scrape reviews
        reviews = scraper.scrape_reviews()
        print(reviews)
    else:
        print("Review page URL not found!")
else:
    print("Device not found!")

price_score = 0.8  # Example price score
ecosystem_score = 0.7  # Example ecosystem score

analyzer = ReviewSentimentAnalyzer(preferences={
    'sentiment': 0.4,
    'price': 0.4,
    'ecosystem': 0.2
})

# Aggregate sentiment score
sentiment_score = analyzer.aggregate_scores(reviews)
print(f"Sentiment Score: {sentiment_score}")

# Calculate weighted score
weighted = analyzer.calculate_weighted_score(sentiment_score, price_score, ecosystem_score)
print(f"Weighted Score: {weighted}")