from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class ReviewSentimentAnalyzer:
    def __init__(self, preferences=None):
        self.analyzer = SentimentIntensityAnalyzer()
        self.preferences = preferences or {
            'sentiment': 0.5,
            'price': 0.3,
            'ecosystem': 0.2
        }

    def analyze_review_sentiment(self, review):
        """
        Analyze the sentiment of a single review.
        Returns a compound score between -1 (negative) and +1 (positive).
        """
        sentiment = self.analyzer.polarity_scores(review)
        return sentiment['compound']

    def aggregate_scores(self, reviews):
        """
        Aggregate sentiment scores for a list of reviews.
        Returns the average compound score.
        """
        if not reviews:
            return 0  # Handle edge case for empty reviews list
        total_score = sum(self.analyze_review_sentiment(review) for review in reviews)
        return total_score / len(reviews)

    def calculate_weighted_score(self, sentiment_score, price_score, ecosystem_score):
        """
        Calculate a weighted score based on sentiment, price, and ecosystem preferences.
        """
        return (self.preferences['sentiment'] * sentiment_score +
                self.preferences['price'] * price_score +
                self.preferences['ecosystem'] * ecosystem_score)


# Example Usage
if __name__ == "__main__":
    reviews = [
        "This device is amazing! I love the display and the performance.",
        "The battery life is disappointing, but the build quality is decent.",
        "A great value for the price, though the camera could be better."
    ]

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
