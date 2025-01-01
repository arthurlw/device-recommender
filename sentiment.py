from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_review_sentiment(review):
    sentiment = analyzer.polarity_scores(review)
    return sentiment['compound']  # Returns a score between -1 (negative) and +1 (positive)

# Example review
review = "Comment 1: IntroductionThe Redmi Pad and the Redmi Pad SE gained a lot of traction - their large screens, metal bodies and, of course, attractive pricing making them an excellent choice for consuming multimedia on your couch. Now Xiaomi expands the Redmi tablet series, with a Pad Pro, which adds more premium Dolby Vision display, better performance, and a larger battery.The tablet is offered as a5G model with a built-in GPS, but we are reviewing the Wi-Fi-only version here.The new Redmi Pad Pro brings a 12.1 120 Hz LCD of 2560 x 1600 pixel resolution with Dolby Vision certification. There is a powerful Snapdragon 7s Gen 2 chip, which should be a good upgrade over the Snapdragon 680 and Helio G99 in the older Pad models.The Redmi Pad Pro has an 8MP camera on each side, four  Dolby Atmos speakers with and a large 10,000mAh battery with 33W charging support, which means you won't have to reach for that charger too often.Xiaomi Redmi Pad Pro specs at a glance:Body:280.0x181.9x7.5mm, 571g; Glass front (Gorilla Glass 3), aluminum frame, aluminum back; Stylus support (magnetic).Display:12.10 IPS LCD, 68B colors, 120Hz, Dolby Vision, 600 nits (HBM), 1600x2560px resolution, 16:10 aspect ratio, 249ppi.Chipset:Qualcomm SM7435-AB Snapdragon 7s Gen 2 (4 nm): Octa-core (4x2.40 GHz Cortex-A78 & 4x1.95 GHz Cortex-A55); Adreno 710.Memory:128GB 6GB RAM, 128GB 8GB RAM, 256GB 8GB RAM; UFS 2.2; microSDXC (dedicated slot).OS/Software:Android 14, HyperOS.Rear camera:8 MP, f/2.0, (wide), 1/4.0, 1.12µm.Front camera:8 MP, f/2.3, (wide), 1/4.0, 1.12µm.Video capture:Rear camera: 1080p@30fps;Front camera: 1080p@30fps.Battery:10000mAh; 33W wired, PD3.0, QC3+.Connectivity:Wi-Fi 6; BT 5.2,  aptX HD,  aptX Adaptive; 3.5mm jack.Misc:Accelerometer, gyro, proximity (accessories only), compass; stereo speakers (4 speakers).To further enhance its capabilities Xiaomi sells official accessories including the Redmi Smart Pen, the Redmi Pad Pro Cover and the Redmi Pad Pro Keyboard cover. On the list of omissions we can put the lack of cellular connectivity, NFC, and a fingerprint scanner, but we wouldn't say either of those is a big deal when it comes to tablets.Unboxing the Redmi Pad ProThe Xiaomi Redmi Pad Pro arrives in a thin paper box, which contains the tablet itself and a USB-A-to-C cable. There is no charger and if odds are you don't have a 33W charger, so you'll need to purchase one if maximizing charging speed matters to you."
score = analyze_review_sentiment(review)
print(f"Sentiment Score: {score}")

def aggregate_scores(reviews):
    total_score = 0
    for review in reviews:
        total_score += analyze_review_sentiment(review)
    return total_score / len(reviews)

def weighted_score(device, preferences, sentiment_score, price_score, ecosystem_score):
    return (preferences['sentiment'] * sentiment_score +
            preferences['price'] * price_score +
            preferences['ecosystem'] * ecosystem_score)
