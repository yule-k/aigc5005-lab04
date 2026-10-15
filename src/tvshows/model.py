#the record class

class TVShow:
    """A single TV Show record."""

    def __init__(self, name, language=None, genres=None, rating=None, premiered=None):
        self.name = name
        self.language = language
        self.genres = genres
        self.rating = rating
        self.premiered = premiered

        # Save and calculate year and decade from premiered ('2013-06-24')
        if self.premiered:
            try:
                self.year = int(self.premiered[:4])
                self.decade = (self.year // 10) * 10
            except ValueError:
                self.year = None
                self.decade = None
        else:
            self.year = None
            self.decade = None


def tvshow_from_dict(show_data):
    """Create a TVShow instance from a dictionary."""
    rating_data = show_data.get("rating") or {}

    return TVShow(
        name=show_data.get("name"),
        language=show_data.get("language"),
        genres=show_data.get("genres"),
        rating=rating_data.get("average"),
        premiered=show_data.get("premiered")
    )