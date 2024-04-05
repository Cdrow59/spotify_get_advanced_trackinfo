import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth


def get_spotify_track_info(track_id):
    # Replace 'YOUR_CLIENT_ID' and 'YOUR_CLIENT_SECRET' with your Spotify API credentials
    client_id = '1487838d67b04fdfaf1c669ea76e3d3a'
    client_secret = '271749c4f66449808c8419e8803c8145'
    redirect_uri = 'http://localhost:8000/callback'

    filename = (os.path.splitext(os.path.basename(__file__))[0])
    cache_path = ("C:\\Users\\Clayton\\AppData\\Local\\Temp\\vscode\\" +filename+ ".cache")
    
    # Initialize Spotipy with client credentials
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri,cache_path=cache_path))

    # Get track information
    track_info = sp.track(track_id)
    audio_features = sp.audio_features([track_id])[0]
    
    # Get the first artist's information to infer the genre
    artist_info = sp.artist(track_info['artists'][0]['id'])


    # Display track information
    print(f"Track: {track_info['name']}")
    print(f"Artist: {', '.join([artist['name'] for artist in track_info['artists']])}")
    print(f"Album: {track_info['album']['name']}")
    print(f"Genre: {', '.join(artist_info['genres'])}")
    print(f"Release Date: {track_info['album']['release_date']}")
    print(f"Duration: {audio_features['duration_ms'] / 1000} seconds")
    print(f"Tempo (BPM): {audio_features['tempo']}")
    print(f"Key: {audio_features['key']}")
    print(f"Camelot: {audio_features['key'] % 12}A")
    print(f"Popularity: {track_info['popularity']}")
    print(f"Happiness: {audio_features['valence']}")
    print(f"Danceability: {audio_features['danceability']}")
    print(f"Energy: {audio_features['energy']}")
    print(f"Acousticness: {audio_features['acousticness']}")
    print(f"Instrumentalness: {audio_features['instrumentalness']}")
    print(f"Liveness: {audio_features['liveness']}")
    print(f"Speechiness: {audio_features['speechiness']}")
    print(f"Loudness: {audio_features['loudness']} dB")
    print(f"Explicit: {track_info['explicit']}")

if __name__ == "__main__":
    # Replace 'SPOTIFY_TRACK_ID' with the actual Spotify track ID you want to get information for
    track_id = input('enter a SPOTIFY_TRACK_ID\n')
    get_spotify_track_info(track_id)
    