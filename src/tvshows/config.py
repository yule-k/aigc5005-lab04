import tomllib
from dataclasses import dataclass
from pathlib import Path

from tvshows.errors import ConfigError

REQUIRED_KEYS = ["url", "timeout", "output_dir", "seed", "sample_size", "log_level"]


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

    # Every setting must be in the file; a missing one is an error, not a default.
    missing = [key for key in REQUIRED_KEYS if key not in raw]
    if missing:
        raise ConfigError(f"Settings file {config_path} is missing: {missing}")

    # Extracts values from TOML data, creates a Settings object, and returns it.
    return Settings(
        url=raw["url"],
        timeout=raw["timeout"],
        output_dir=Path(raw["output_dir"]),
        seed=raw["seed"],
        sample_size=raw["sample_size"],
        log_level=raw["log_level"],
    )
