import requests
import pandas as pd

def scrape_twitter(query, limit=50):
    print("Scraping Twitter using Nitter...")

    base = "https://nitter.net/search"
    params = {
        "q": query,
        "f": "tweets"
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(base, params=params, headers=headers)
    html = response.text

    tweets = []

    import re
    pattern = r'class="tweet-content media-body">(.*?)<\/div>'

    matches = re.findall(pattern, html, re.DOTALL)

    for m in matches[:limit]:
        text = re.sub("<.*?>", "", m).strip()

        tweets.append({
            "source": "twitter",
            "query": query,
            "content": text,
            "likes": 0,
            "retweets": 0
        })

    df = pd.DataFrame(tweets)

    df.to_csv("F:/INTERNSHIPS/ATOMBERG/CODES/data/twitter_results.csv", index=False)
    print("Saved twitter_results.csv")

    return df


if __name__ == "__main__":
    scrape_twitter("smart fan", 20)
