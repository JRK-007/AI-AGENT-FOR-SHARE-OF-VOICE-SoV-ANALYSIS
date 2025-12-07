import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def search_youtube(query, max_results=20):
    print("Fetching YouTube Results...")

    query = query.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={query}"

    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    scripts = soup.find_all("script")

    data_script = None
    for s in scripts:
        if "ytInitialData" in s.text:
            data_script = s.text
            break

    json_text = re.search(r"ytInitialData = ({.*?});", data_script).group(1)

    import json
    data = json.loads(json_text)

    contents = (
        data["contents"]["twoColumnSearchResultsRenderer"]
        ["primaryContents"]["sectionListRenderer"]["contents"][0]
        ["itemSectionRenderer"]["contents"]
    )

    videos = []

    for item in contents:
        if "videoRenderer" in item:
            info = item["videoRenderer"]

            title = info["title"]["runs"][0]["text"]
            vid_id = info["videoId"]
            channel = info["ownerText"]["runs"][0]["text"]
            views = info.get("viewCountText", {}).get("simpleText", "0")

            videos.append({
                "source": "youtube",
                "query": query,
                "title": title,
                "channel": channel,
                "video_id": vid_id,
                "url": f"https://www.youtube.com/watch?v={vid_id}",
                "views": views
            })

            if len(videos) >= max_results:
                break

    df = pd.DataFrame(videos)
    df.to_csv("F:/INTERNSHIPS/ATOMBERG/CODES/data/youtube_results.csv", index=False)


    print("Saved YouTube results to data/youtube_results.csv")
    return df

if __name__ == "__main__":
    search_youtube("smart fan", 20)
