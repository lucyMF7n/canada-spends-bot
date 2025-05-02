# 🇨🇦 Canada Spends Daily Bot

This bot fetches the latest Government of Canada news from the GC Newsroom RSS feed, uses OpenAI to create a punchy, non-partisan X post, and tweets it daily using the X (Twitter) API.

## 🔧 Setup

1. Clone this repo and `cd` into it.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file with:

```
OPENAI_API_KEY=your_openai_key
X_CONSUMER_KEY=your_x_consumer_key
X_CONSUMER_SECRET=your_x_consumer_secret
X_ACCESS_TOKEN=your_x_access_token
X_ACCESS_SECRET=your_x_access_secret
```

4. Run the bot:

```bash
python main.py
```

You can also schedule this with GitHub Actions using `cron.yaml`.

## 🧠 What It Does

- Pulls the latest GC news: `https://api.io.canada.ca/...`
- Feeds the top story into GPT with a custom prompt
- Posts the generated copy to @CanadaSpends (or your account)
