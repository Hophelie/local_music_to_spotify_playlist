# local_music_to_spotify_playlist


# Spotify Playlist Creator

This script allows you to create a playlist on Spotify and add songs from your music collection based on their metadata (title and artist). It supports MP3, MP4, and M4A file formats.

## Getting Started

To use this script, you'll need to have a Spotify account and create a Spotify application to obtain the necessary credentials.

## Usage
Replace the empty client_id and client_secret variables in the script with your own Spotify application credentials.
Customize the playlist name and description in the script to fit your preferences.
Set the folder_path variable to the directory where your music files are located.
Run the script:

```python playlist_creator.py```

The script will authenticate with Spotify using your credentials and create a private playlist. It will then search for each music file in the specified folder, retrieve the song metadata, and add the corresponding tracks to the playlist.
