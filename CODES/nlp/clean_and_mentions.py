import re
import pandas as pd

BRANDS = ["atomberg", "crompton", "havells", "usha", "orient", "panasonic", "bajaj"]

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^\w\s]", " ", text)
    return text.strip()

def detect_mentions(text):
    clean = clean_text(text)
    mentions = {b: 0 for b in BRANDS}

    for brand in BRANDS:
        if brand in clean:
            mentions[brand] = 1

    return mentions

def apply_mentions(df, column="content"):
    df["clean_text"] = df[column].apply(clean_text)
    for brand in BRANDS:
        df[f"mention_{brand}"] = df["clean_text"].apply(lambda t: 1 if brand in t else 0)
    return df
