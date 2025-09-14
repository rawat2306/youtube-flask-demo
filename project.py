import requests
import os
API_KEY = os.environ.get("YOUTUBE_API_KEY")
MAX_RESULTS = 5

def get_videos(search_query):
    """Fetch YouTube videos for a given search query."""
    url = (
        f"https://www.googleapis.com/youtube/v3/search"
        f"?part=snippet&type=video&maxResults={MAX_RESULTS}"
        f"&q={search_query}&key={API_KEY}"
    )

    response = requests.get(url)
    if response.status_code != 200:
        return {"error": f"API request failed: {response.status_code}"}

    data = response.json()
    results = []

    for item in data.get("items", []):
        snippet = item.get("snippet", {})
        video_id = item.get("id", {}).get("videoId")

        if not video_id:  # skip if no video
            continue

        results.append({
            "title": snippet.get("title", "No Title"),
            "channel": snippet.get("channelTitle", "Unknown Channel"),
            "link": f"https://www.youtube.com/watch?v={video_id}",
            "thumbnail": snippet.get("thumbnails", {}).get("medium", {}).get("url")
        })

    return results
