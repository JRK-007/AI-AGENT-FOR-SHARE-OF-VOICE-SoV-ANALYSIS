import requests
from bs4 import BeautifulSoup
import pandas as pd

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

def fetch_google_results(query, num_results=20):
    print("Starting Google scrape...")

    url = f"https://www.google.com/search?q={query}&hl=en"
    response = requests.get(url, headers=HEADERS)

    print("Page downloaded. Parsing...")

    soup = BeautifulSoup(response.text, "html.parser")
    results = []

    # TRY MULTIPLE SELECTORS
    selectors = [
        "div.tF2Cxc",           # Most common search result block
        "div.g",                # Generic Google result container
        "div.MjjYud"            # Newer layout Google is testing
    ]

    for sel in selectors:
        for g in soup.select(sel):
            title = g.find("h3")
            link = g.find("a")
            snippet = g.find("div", class_="VwiC3b") or g.find("span", class_="aCOpRe")

            if title and link:
                results.append({
                    "title": title.text.strip(),
                    "link": link["href"],
                    "snippet": snippet.text.strip() if snippet else "",
                    "query": query,
                    "source": "google"
                })

            if len(results) >= num_results:
                break

        if len(results) >= num_results:
            break

    print(f"Collected {len(results)} results.")
    return pd.DataFrame(results)


if __name__ == "__main__":
    df = fetch_google_results("smart fan", 20)
    df.to_csv("../data/google_smartfan.csv", index=False)
    print("Saved file to ../data/google_smartfan.csv")
