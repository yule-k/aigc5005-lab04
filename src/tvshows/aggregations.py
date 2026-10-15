# base class and subclasses


class Aggregation:
    """Base class for aggregations."""

    def compute(self, shows):
        raise NotImplementedError


class GenreCount(Aggregation):
    """Count the number of shows in each genre."""

    name = "count by genres"

    def compute(self, shows):
        genre_counts = {}

        for show in shows:
            for genre in show.genres:
                genre_counts[genre] = genre_counts.get(genre, 0) + 1
        return genre_counts


class AverageRatingByLanguage(Aggregation):
    """Calculate the average rating for each language."""

    name = "average ratings by language"

    def compute(self, shows):
        language_basket = {}

        for show in shows:
            language = show.language
            rating = show.rating

            if rating is None:
                continue

            rating_sum, show_count = language_basket.get(language, (0, 0))

            language_basket[language] = (rating_sum + rating, show_count + 1)
        avg_ratings = {
            language: round(rating_sum / show_count, 2)
            for language, (rating_sum, show_count) in language_basket.items()
        }

        return avg_ratings


class ShowsPerDecade(Aggregation):
    """Count the number of shows that premiered in each decade."""

    name = "shows premiered per decade"

    def compute(self, shows):
        decade_counts = {}

        for show in shows:
            decade = show.decade

            if decade is None:
                continue

            decade_counts[decade] = decade_counts.get(decade, 0) + 1

        return decade_counts
