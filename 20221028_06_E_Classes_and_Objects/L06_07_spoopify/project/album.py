# from project.song import Song                       # When working in main project directory uncomment this line
from song import Song                                 # When working in main project directory comment out this line


class Album:
    def __init__(self, name: str, *songs: Song):
        self.name = name
        self.published = False
        self.songs = list(songs)

    def add_song(self, song: Song):
        if song in self.songs:
            return f'Song is already in the album.'
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f'Cannot add songs. Album is published.'

        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str):
        if self.published:
            return f'Cannot remove songs. Album is published.'
        try:
            sng = next(filter(lambda x: x.name == song_name, self.songs))
        except StopIteration:
            return f'Song is not in the album.'

        self.songs.remove(sng)
        return f'Removed song {song_name} from album {self.name}.'

    def publish(self):
        if self.published:
            return f'Album {self.name} is already published.'

        # works
        self.published = True
        return f'Album {self.name} has been published.'

    # works
    def details(self):
        return f'Album {self.name}\n' +\
               '\n'.join([f'== {(x.get_info())}' for x in self.songs]) + '\n'
