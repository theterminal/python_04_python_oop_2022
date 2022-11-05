# from project.album import Album     # When working in main project directory uncomment this line
# from project.song import Song       # When working in main project directory uncomment this line

from album import Album             # When working in main project directory comment out this line
from song import Song               # When working in main project directory comment out this line


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f'Band {self.name} already has {album.name} in their library.'

        self.albums.append(album)
        return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name: str):
        try:
            alb = next(filter(lambda x: x.name == album_name, self.albums))
        except StopIteration:
            return f'Album {album_name} is not found.'

        if alb.published:
            return f'Album has been published. It cannot be removed.'

        self.albums.remove(alb)
        return f'Album {album_name} has been removed.'

    def details(self,):
        return f'Band {self.name}\n' + \
               '\n'.join([x.details() for x in self.albums])


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
