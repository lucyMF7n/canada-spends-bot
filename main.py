import os
import openai
import tweepy
import feedparser
from dotenv import load_dotenv

load_dotenv()

# Setup OpenAI + X API
openai.api_key = os.getenv("OPENAI_API_KEY")
client = tweepy.Client(
    consumer_key=os.getenv("X_CONSUMER_KEY"),
    consumer_secret=os.getenv("X_CONSUMER_SECRET"),
    access_token=os.getenv("X_ACCESS_TOKEN"),
    access_token_secret=os.getenv("X_ACCESS_SECRET")
)

# Step 1: Get latest GC news
rss_url = "https://api.io.canada.ca/io-server/gc/news/en/v2?sort=publishedDate&orderBy=desc&publishedDate%3E=2021-10-25&pick=100&format=atom&atomtitle=National%20News"
feed = feedparser.parse(rss_url)
latest = feed.entries[0]

# Step 2: Create GPT prompt
prompt = f"""
You are a non-partisan watchdog account called Canada Spends. Your tone is factual, witty, and engaging.

Here is a Government of Canada announcement:
Title: {latest.title}
Date: {latest.published}
Summary: {latest.summary}
Link: {latest.link}

Create a punchy X post that:
- Summarizes this announcement in plain language.
- Highlights the spending amount or policy implication.
- Uses an engaging hook or analogy.
- Avoids opinions, but encourages people to think.
- Is under 280 characters.
- Includes the link and the hashtag #CanadaSpends

Output only the final post.
"""

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7,
)

tweet = response['choices'][0]['message']['content'].strip()

# Step 3: Tweet
client.create_tweet(text=tweet)
print("Tweeted:", tweet)
