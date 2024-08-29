import tweepy
import pandas as pd

# Twitter API credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Initialize Tweepy client
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

# Load the CSV file into a DataFrame
df = pd.read_csv("amazon_products.csv")

# Define the number of tweets to post
num_tweets = 1  # Adjust this as needed

# Loop through the top items and tweet them
for index, row in df.head(num_tweets).iterrows():
    try:
        # Create the product URL
        product_url = f"http://www.amazon.in/dp/{row['ASIN']}/ref=nosim?tag=dealsfinde0a6-21"

        # Prepare the tweet content
        tweet = (
            f"{row['Product Title']}\n"
            f"Price: ₹{row['Price']}\n"
            f"Grab it here: {product_url}\n"
            f"#Deals #Discounts #Amazon"
        )

        # Post the tweet
        client.create_tweet(text=tweet)
        print(f"Tweeted: {row['Product Title']}")

        # Remove the tweeted product from the DataFrame
        df = df.drop(index)

    except Exception as e:
        # Handle any errors during tweeting
        print(f"Error tweeting {row['Product Title']}: {e}")

# Save the updated DataFrame back to the CSV file
df.to_csv("amazon_products.csv", index=False)

print("Tweeting complete.")
