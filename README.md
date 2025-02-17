# 🎵 mp3ify
> All of these instructions are created for Windows, you need to find alternative instructions for other platforms

## Features
- Convert Spotify **songs or playlists** to **MP3**
- Uses **yt-dlp** to fetch the best YouTube audio match
- **FFmpeg** is used for proper MP3 conversion
- Saves MP3s to a `song_list` folder

## Installation
First download all the present, next...

Run this command to install `spotipy` and `yt-dlp` with the help of the `requirements.txt`

```
pip install -r requirements.txt
```

Next, you have to a create an app in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard), which will be used in the script

You also need `FFmpeg` which can be installed using this command:
```
winget install Gyan.FFmpeg
```

## Usage
Run `main.py` and enter a Spotify link, a track and/or a playlist:

```
python main.py
```

# Troubleshooting
The only issue I got was `ffmpeg not found`, just make sure it is installed and added to **System Path

# Future Implementations❓(maybe?)
- Maybe a GUI implementation
- Generate a Download History
- Allow Playlist Downloads in Bulk (with multi-threading)
- Convert MP3 Files to Other Formats (WAV, AAC, FLAC)
\
### Thank You for Visiting!
