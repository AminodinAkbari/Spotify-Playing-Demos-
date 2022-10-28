from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials,SpotifyOAuth
from django.core.exceptions import ValidationError
from django.contrib import messages
from decouple import config

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=config('CLIENT_ID'),client_secret=config('CLIENT_SECRET')))

def Index(request):
    context = {}
    if request.method == 'POST':
        posted = 1
        query = request.POST.get('name_artist')
        if query:
            results = sp.search(q=query, limit=20)

            songs = {}

            for idx, track in enumerate(results['tracks']['items']):
                songs[track['name']] = track['preview_url']
                context['songs'] = songs
                context['artist'] = query
                
    else:
        posted = 0
    context['posted'] = posted

    return render(request , 'index.html' ,context)