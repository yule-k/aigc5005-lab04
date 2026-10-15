import unittest
from tvshows.model import TVShow

class TestTVShow(unittest.TestCase):

    def test_year_and_decade(self):
        show = TVShow("Test", premiered="2011-04-17")
        self.assertEqual(show.year, 2011)
        self.assertEqual(show.decade, 2010)

    def test_missing_premiered(self):
        show = TVShow("Test", premiered=None)
        self.assertIsNone(show.year)
        self.assertIsNone(show.decade)


if __name__ == "__main__":
    unittest.main()