from spotipy.oauth2 import SpotifyClientCredentials as SCC
import spotipy, re, os

class Serve:
    def __init__(self):
        self.credentialManager = SCC(
            client_id=os.environ.get('spotipyClientID'),
            client_secret=os.environ.get('spotipyClientSecret')
        )

        self.spotify = spotipy.Spotify(client_credentials_manager=self.credentialManager)

    def serve_new_releases(self):
        nr = str(self.spotify.new_releases(country='US', limit=10, offset=0))

        pattern = r"(?<='name': ')[\w\s!\"#$%&\'()*+,\-.\/:;<=>?@\[\]\\_\^`\|~]*(?=', 'ty)"
        results = re.findall(pattern, nr)

        return results