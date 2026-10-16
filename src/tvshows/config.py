import tomllib
from dataclasses import dataclass
from pathlib import Path

from tvshows.errors import ConfigError


@dataclass(frozen=True)
class Settings:
    """Settings loaded from the TOML configuration file."""

    url: str
    timeout: int
    output_dir: Path
    seed: int
    sample_size: int
    log_level: str


def load_settings(path: Path | str = "config/tvshows.toml") -> Settings:
    """Load settings from a TOML file and return a Settings instance."""
    config_path = Path(path)
    try:
        with config_path.open("rb") as handle:
            raw = tomllib.load(handle)
    except FileNotFoundError as error:
        raise ConfigError(f"Settings file {config_path} does not exist.") from error
    except (tomllib.TOMLDecodeError, ValueError) as error:
        raise ConfigError(f"Settings file {config_path} is invalid TOML.") from error

    # Extracts values ​​from TOML data, creates a Settings object, and returns it.
    return Settings(
        url=raw.get("url", "https://api.tvmaze.com/shows?page=0"),
        timeout=raw.get("timeout", 10),
        output_dir=Path(raw.get("output_dir", "data/processed")),
        seed=raw.get("seed", 42),
        sample_size=raw.get("sample_size", 3),
        log_level=raw.get("logging", {}).get("level", "INFO"),
    )
