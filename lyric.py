import lyricwikia

'''

@author ssaxena36

'''

class SongLyrics(object):
    def __init__(self):
        pass
    def getLyrics(self, artist, song):
        out = ""
        try:
            out = lyricwikia.get_lyrics(artist, song)
        except:
            return "No lyrics found. :("
        return out