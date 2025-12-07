import pandas as pd
from scrapers.youtube_scraper import search_youtube
from scrapers.twitter_scraper import scrape_twitter
from nlp.clean_and_mentions import apply_mentions
from nlp.sentiment import analyze_sentiment
from analysis.compute_sov import compute_sov

print("\n==============================================")
print("  Atomberg AI Agent — Share of Voice Analyzer")
print("==============================================\n")

# Get keywords from user
user_input = input("Enter keyword(s) to analyze (comma-separated). \nDefault = smart fan\n → ")

# Process input
if user_input.strip() == "":
    KEYWORDS = ["smart fan"]
else:
    KEYWORDS = [kw.strip() for kw in user_input.split(",")]

print("\nKeywords selected:", KEYWORDS)

all_results = []

for kw in KEYWORDS:
    print(f"\n============================")
    print(f"   PROCESSING KEYWORD: {kw}")
    print(f"============================")

    print("\n=== Scraping YouTube ===")
    yt = search_youtube(kw, 20)

    print("\n=== Scraping Twitter ===")
    tw = scrape_twitter(kw, 30)

    # Standardize column names
    yt = yt.rename(columns={"title": "content"})
    
    # Combine results
    df_kw = pd.concat([yt, tw], ignore_index=True)

    print("\n=== Cleaning & Mention Detection ===")
    df_kw = apply_mentions(df_kw, column="content")

    print("\n=== Sentiment Analysis ===")
    df_kw["sentiment"] = df_kw["clean_text"].apply(analyze_sentiment)

    # Save per-keyword cleaned data
    df_kw.to_csv(f"F:/INTERNSHIPS/ATOMBERG/CODES/data/cleaned_{kw.replace(' ', '_')}.csv", index=False)

    print("\n=== Computing Share of Voice ===")
    sov_kw = compute_sov(df_kw)

    # Tag each SOV row with the keyword
    sov_kw["keyword"] = kw

    all_results.append(sov_kw)

# Merge all SoV results
final_sov = pd.concat(all_results, ignore_index=True)
final_sov.to_csv("F:/INTERNSHIPS/ATOMBERG/CODES/data/final_sov_comparison.csv", index=False)

print("\n==============================================")
print("       MULTI-KEYWORD ANALYSIS COMPLETE")
print("==============================================\n")
print(final_sov)
