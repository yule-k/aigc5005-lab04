## TV Shows
A hardened Python package that fetches TV show data from the TVMaze API, processes and aggregates records (genre counts, ratings by language, shows per decade), and outputs reproducible summaries with deterministic random sampling.

## Setup
conda env create -f environment.yml
conda activate tvshows
pip install -r requirements.txt
pip install -e .

## Run
python -m tvshows.main
python -m tvshows.main --config config/tvshows.toml

## Check it
python -m ruff format --check .
python -m ruff check .
python -m mypy src
python -m pytest

## Settings
url: The source API endpoint URL for fetching TV show records.

timeout: Request timeout duration in seconds.

output_dir: Directory path where summary.json and run_info.json are saved.

seed: Random seed number ensuring deterministic and reproducible show sampling.

sample_size: The number of featured TV shows randomly selected for the summary.

log_level: Logging verbosity level (e.g., INFO, DEBUG).

## Errors and exit codes
| Error Class | When it is raised | What the user sees / Messages |
| :--- | :--- | :--- |
| `ConfigError` | When the TOML settings file is missing, unreadable, or invalid. | • `Settings file {config_path} does not exist.`<br>• `Settings file {config_path} is invalid TOML.`<br>• `Settings file {config_path} is missing: {missing}` |
| `SourceError` | When network requests fail or the API connection times out. | • `HTTP error while fetching data from {self.url}`<br>• `Unable to reach {self.url}` |
| `DataError` | When downloaded data shape is unexpected or required fields are missing. | • `There is missing data that is required.: {error}`<br>• `{self.url} did not return valid JSON.`<br>• `Expected a list of shows from {self.url}.` |

* **Exit code 0**: Successful execution. Summaries and `run_info.json` were successfully generated.
* **Exit code 1**: Expected failure. An error occurred, it was logged via the logger, and a single clean error message beginning with `Error:` was printed to standard error (`stderr`).

## Reproducing a run
Seed location: The random seed is defined in config/tvshows.toml.

Run info records: run_info.json records the exact configuration settings used, the Python version, and the pinned versions of pytest, mypy, and ruff.

Reproduction steps: To get the exact same featured_shows list, another user needs the same TOML configuration file containing the identical seed and sample_size values, running on the same dataset source.

## What the tests cover
The test suite protects the core behavior of the package, including:

TV show record creation, parsing from dictionaries, and handling missing data (such as missing genres or ratings).

Aggregation correctness using hand-made records.

Exception handling at boundaries (pytest.raises with match arguments).

Deterministic random sampling via seeds (get_featured_shows).

File handling and output generation using tmp_path and conftest.py fixtures.

Entry point execution, exit codes, and error printing for failed runs.

What was chosen not to test: Live network connectivity against the real TVMaze API, as tests must remain independent of external network states and internet availability.


## Known limitations
The package processes the initial page of TV shows from the TVMaze API and relies on the stability of the external public endpoint.