import pandas as pd

BRANDS = ["atomberg", "crompton", "havells", "usha", "orient", "panasonic", "bajaj"]

def compute_sov(df):
    # Ensure missing columns exist and are numeric
    if "likes" not in df:
        df["likes"] = 0
    if "retweets" not in df:
        df["retweets"] = 0
    if "sentiment" not in df:
        df["sentiment"] = 0

    df["likes"] = pd.to_numeric(df["likes"], errors="coerce").fillna(0)
    df["retweets"] = pd.to_numeric(df["retweets"], errors="coerce").fillna(0)
    df["sentiment"] = pd.to_numeric(df["sentiment"], errors="coerce").fillna(0)

    results = []

    for brand in BRANDS:
        mention_col = f"mention_{brand}"

        if mention_col not in df:
            df[mention_col] = 0

        mentions = df[mention_col].sum()
        engagement = (df["likes"] + df["retweets"]).sum()
        sentiment = df["sentiment"].mean()

        results.append({
            "brand": brand,
            "mentions": mentions,
            "engagement": engagement,
            "sentiment": sentiment
        })

    sov_df = pd.DataFrame(results)

    # Normalize carefully
    total_mentions = max(sov_df["mentions"].sum(), 1)
    total_engagement = max(sov_df["engagement"].sum(), 1)

    sov_df["mentions_norm"] = sov_df["mentions"] / total_mentions
    sov_df["engagement_norm"] = sov_df["engagement"] / total_engagement

    if sov_df["sentiment"].max() != sov_df["sentiment"].min():
        sov_df["sentiment_norm"] = (
            (sov_df["sentiment"] - sov_df["sentiment"].min()) /
            (sov_df["sentiment"].max() - sov_df["sentiment"].min())
        )
    else:
        sov_df["sentiment_norm"] = 0

    sov_df["SoV"] = (
        0.5 * sov_df["mentions_norm"] +
        0.3 * sov_df["engagement_norm"] +
        0.2 * sov_df["sentiment_norm"]
    )

    sov_df.to_csv("F:/INTERNSHIPS/ATOMBERG/CODES/data/sov_output.csv", index=False)
    print("Saved SoV results to data/sov_output.csv")

    return sov_df
