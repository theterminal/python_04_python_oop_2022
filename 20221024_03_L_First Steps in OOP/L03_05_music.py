# 20221024 - Python OOP - First Steps in OOP
# 05 - Music - judge url: https://judge.softuni.org/Contests/Practice/Index/1934#4


# --------------------- version 1 --------------------- judge 100%


class Music:
    def __init__(self, title: str, artist: str, lyrics: str):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return f'{self.lyrics}'


song = Music("Title", "Artist", "Lyrics")
print(song.print_info())
print(song.play())
