## TV Shows Summary
This package downloads TV show records from the TVMaze public API and summarizes them by genre, average rating by language, and premiere decade.

The project refactors the original Lab 02 script into a Python package with separate modules for data models, data fetching, aggregations, reporting, and configuration.

## Data source
The program uses the TVMaze public API:
https://api.tvmaze.com/shows?page=0
The API returns roughly 240 TV show records.

## Setup
Create the Conda environment:
conda env create -f environment.yml
pip install -r requirements.txt

## Run
python main.py

# Test
python -m unittest discover -s tests

## Layout
`config.py` Stores shared settings such as the TVMaze source URL, request timeout, and output path.

`model.py` Contains the TVShow class, which represents one TV show record and cleans or prepares values such as language, rating, year, and decade.

`sources.py` Contains the class responsible for downloading data from the TVMaze API and converting raw dictionaries into TVShow objects. This is the only module that imports requests.

`aggregations.py` Contains the Aggregation base class and the aggregation subclasses that summarize TV show data.

`report.py` Builds the final summary dictionary from the aggregation results and writes it to a JSON file.

`main.py` Acts as the entry point and connects the source, aggregations, and report-writing logic.

## What moved where
tvmaze() → TVMazeSource.fetch() in `sources.py`


number_genres() → GenreCount.compute() in `aggregations.py`


average_rating_by_language() → AverageRatingByLanguage.compute() in `aggregations.py`


shows_per_decade() → ShowsPerDecade.compute() in `aggregations.py`


Summary + JSON writing → `report.py`

## Design choices
`TVShow` represents one cleaned TV show record.
  
`TVMazeSource` handles downloading data and converts raw dictionaries into `TVShow` objects.


`Aggregation` is the base class for the summary calculations.

`GenreCount`, `AverageRatingByLanguage`, and `ShowsPerDecade` inherit from it and override `compute()`.


To add a new aggregation, create another subclass of `Aggregation` and define its own `compute()` method.

## Known limitations
Although this program analyzed only the records from the first page for the assignment, it could be developed into an analysis tool that utilizes the full dataset and data visualization to boost TVmaze's conversion rates.