import os
from mutagen.mp4 import MP4
from mutagen.easyid3 import EasyID3
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials and redirect URI
client_id = ''
client_secret = ''
redirect_uri = 'http://localhost/'

# Create an instance of SpotifyOAuth for authentication
scope = 'playlist-modify-private'  # Required permissions to create a playlist
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

# Create the playlist
playlist_name = 'Rababou 2012'
playlist_description = 'Playlist created with the Spotify API featuring songs from my GREEN APPLE IPOD NANO. (It was truly incredible)'

user_id = sp.me()['id']  # Get the user ID
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description=playlist_description)

# Display the URL of the created playlist
playlist_url = playlist['external_urls']['spotify']
print('Playlist created:', playlist_url)

# ---------------------------------------------------

# Variables for file processing
files_list = []
music={}
folder_path = "D:\Musique"

def get_mp4_title(file_path):
    try:
        if file_path.lower().endswith('.mp4') or file_path.lower().endswith('.m4a'):
            # Process MP4 and M4A files
            media = MP4(file_path)
            if '©nam' in media:
                title = media['©nam'][0]
                artist = media['©ART'][0]
                resultats = sp.search(q=f'artist:{artist} track:{title}', type='track', limit=1)
                for track in resultats['tracks']['items']:
                    sp.playlist_add_items(playlist_id=playlist['id'], items=[track['id']])
            else:
                title = "Titre non disponible"
                artist = "Artiste non disponible"
        elif file_path.lower().endswith('.mp3'):
            # Process MP3 files
            media = EasyID3(file_path)
            if 'title' in media:
                title = media['title'][0]
                artist = media['artist'][0]
                resultats = sp.search(q=f'artist:{artist} track:{title}', type='track', limit=1)
                for track in resultats['tracks']['items']: 
                    sp.playlist_add_items(playlist_id=playlist['id'], items=[track['id']])
            else:
                title = "Titre non disponible"
                artist = "Artiste non disponible"
        else:
            return None

    except Exception as e:
        print("Une erreur s'est produite:", str(e))
        return None

# Iterate over the music folders and files
for music_folder in os.listdir(folder_path):
    music_folder_path = os.path.join(folder_path, music_folder)
    for filename in os.listdir(music_folder_path):
        f = os.path.join(music_folder_path, filename)
        get_mp4_title(f)
