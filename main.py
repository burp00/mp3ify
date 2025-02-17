import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import yt_dlp

# Spotify API credentials
SPOTIPY_CLIENT_ID = "<CLIENT ID HERE>"
SPOTIPY_CLIENT_SECRET = "<CLIENT SECRET HERE>"

# Initialization of Spotify API
try:
    sp = spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id = SPOTIPY_CLIENT_ID, client_secret = SPOTIPY_CLIENT_SECRET
        )
    )
except Exception as e:
    print(f"❌ Error initializing Spotify API: {e}")
    exit(1)

# "song_list" folder for download destination
destination_folder = os.path.join(os.path.dirname(__file__), "song_list")
os.makedirs(destination_folder, exist_ok = True)


def song_request(spotify_track_url):
    # Processing URL to only get only track id
    track_id = spotify_track_url.split("/")[-1].split("?")[0]

    # Aquire song info from the API
    track = sp.track(track_id)

    song_name = track["name"]
    artist = track["artists"][0]["name"]
    full_song_name = f"{song_name} {artist}"

    print(f"🎵 Processing song: {full_song_name}")
    download_song(full_song_name)


def playlist_request(spotify_playlist_url):
    # Processing URL to only get only playlist id
    playlist_id = spotify_playlist_url.split("/")[-1].split("?")[0]

    # Aquire playlist info from the API
    results = sp.playlist_tracks(playlist_id)

    tracks = results["items"]

    # Iterate through all the songs in the playlist
    for item in tracks:
        track = item["track"]
        song_name = track["name"]
        artist = track["artists"][0]["name"]
        full_song_name = f"{song_name} {artist}"

        print(f"🎶 Processing playlist song: {full_song_name}")
        download_song(full_song_name)


def download_song(song_name):
    print(f"🔍 Searching for: {song_name} on YouTube...")

    # Writting the request format before passing it to yt-dlp
    ydl_req = {
        "format": "bestaudio/best",
        "outtmpl": f"{destination_folder}/{song_name}",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "quiet": True,
    }

    # Search the song name on Youtube and download it
    try:
        with yt_dlp.YoutubeDL(ydl_req) as ydl:
            ydl.download([f"ytsearch:{song_name}"])

        print(f"✅ Downloaded song with name: {song_name}")

    except Exception as e:
        print(f"❌ Error downloading {song_name}: {e}")


if __name__ == "__main__":
    spotify_link = input("🎵 Enter Spotify song or playlist link: ")

    # Checking if the user's link is a song or playlist link
    if "playlist" in spotify_link:
        playlist_request(spotify_link)
    else:
        song_request(spotify_link)
