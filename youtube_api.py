# youtube_api.py
from googleapiclient.discovery import build

API_KEY = 'AIzaSyByjoWuwLTyVKB0u2-OUWzDxrw2POu5Vpk'

def get_comments(video_id, max_comments=50):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    comments = []
    
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=min(100, max_comments),
        textFormat='plainText'
    )
    response = request.execute()

    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)

    return comments
