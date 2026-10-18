# the record class
from tvshows.errors import DataError


class TVShow:
    """A single TV Show record."""

    def __init__(self, name, language=None, genres=None, rating=None, premiered=None):
        self.name = name
        self.language = language
        self.genres = genres if genres is not None else []
        self.rating = rating if rating is not None else None
        self.premiered = premiered

        if isinstance(rating, dict):
            self.rating = rating.get("average")
        else:
            self.rating = None

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


def __str__(self) -> str:
        genres = ", ".join(self.genres)
        return (
            f"{self.name} ({self.year}) - {self.language} - "
            f"{genres} - Rating: {self.rating}"
        )

def tvshow_from_dict(show_data):
    """Create a TVShow instance from a dictionary."""
    try:
        name = show_data.get("name")
        return TVShow(
            name=name,
            language=show_data.get("language"),
            genres=show_data.get("genres"),
            rating=show_data.get("rating"),
            premiered=show_data.get("premiered"),
        )
    except KeyError as error:
        raise DataError(
            f"There is missing data that is required.: {error}"
        ) from KeyError
    except Exception as error:
        raise DataError(f"Error ocurred during fetching data: {error}") from error
