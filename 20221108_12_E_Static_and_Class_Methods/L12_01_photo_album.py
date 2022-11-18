# 20221108 - Python - Python OOP - Static and Class Methods
# 01 - Photo Album - judge url: https://judge.softuni.org/Contests/Compete/Index/2431#0


from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages                                          # each page can contain only 4 photos
        self.photos = [[] for _ in range(pages)]                    # matrix that should hold the photos

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE))

    def add_photo(self, label: str):
        for page_i in range(len(self.photos)):
            if len(self.photos[page_i]) < PhotoAlbum.PHOTOS_PER_PAGE:
                self.photos[page_i].append(label)
                return f'{label} photo added successfully on page {page_i + 1} slot {len(self.photos[page_i])}'
        return 'No more free slots'

    def display(self):
        result = ['-' * 11]
        for page in self.photos:
            result.append(('[] ' * len(page)).rstrip())
            result.append('-----------')

        return '\n'.join(result)


# album = PhotoAlbum.from_photos_count(50)        # creates instance of Album using classmethod 'from_photos_count' and insertion of 50 photos
# print(album.photos)                             # [[], [], [], [], [], [], [], [], [], [], [], [], []]


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
