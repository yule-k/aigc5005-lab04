from pathlib import Path

import pytest

from tvshows.config import load_settings
from tvshows.errors import ConfigError


def test_settings_are_read_from_a_complete_file(tmp_path: Path) -> None:
    """Test that every setting is read from a complete TOML file."""
    path = tmp_path / "settings.toml"
    path.write_text(
        'url = "https://example.invalid"\n'
        "timeout = 5\n"
        'output_dir = "out"\n'
        "seed = 7\n"
        "sample_size = 2\n"
        'log_level = "DEBUG"\n',
        encoding="utf-8",
    )
    settings = load_settings(path)
    assert settings.seed == 7
    assert settings.log_level == "DEBUG"


def test_a_missing_settings_file_raises_config_error(tmp_path: Path) -> None:
    """Test that a settings file that does not exist raises ConfigError."""
    with pytest.raises(ConfigError, match="does not exist"):
        load_settings(tmp_path / "none.toml")


def test_an_incomplete_settings_file_raises_config_error(tmp_path: Path) -> None:
    """Test that a settings file with missing keys raises ConfigError."""
    path = tmp_path / "partial.toml"
    path.write_text("seed = 1\n", encoding="utf-8")
    with pytest.raises(ConfigError, match="missing"):
        load_settings(path)
