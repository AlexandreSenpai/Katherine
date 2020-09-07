import requests

class Youtube:
    def __init__(self, token: str):
        self._token = token
        self._base_url = 'https://www.googleapis.com/youtube/v3/search?key={}&order=viewCount&q={}&type=video&videoDefinition=high'
        self.youtube_url = 'www.youtube.com/watch?v={}'

    def most_viewed(self, query: str) -> (str):
        req = requests.get(self._base_url.format(self._token, query))
        if req.status_code == 200:
            if len(req.json().get('items', [{}])) > 0:
                return self.youtube_url.format(req.json().get('items', [{}])[0].get('id', {}).get('videoId', ''))