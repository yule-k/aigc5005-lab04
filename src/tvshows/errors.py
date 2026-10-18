class TvShowsError(Exception):
    """Base class for every error this package raises on purpose."""


class SourceError(TvShowsError):
    """Errors occurring during network connection failures or external API downloads."""


class ConfigError(TvShowsError):
    """The settings file is missing, unreadable or incomplete."""


class DataError(TvShowsError):
    """The data received from the source is invalid or malformed."""
