"""Configuration for app."""

from pydantic import BaseModel


class AppConfig(BaseModel):  # type: ignore[misc]
    """Class for app configuration."""

    name: str
    title: str
    debug: bool
    host: str
    port: int
    repository: str
    assets_folder: str

    def set_debug_mode(self, mode: bool) -> None:
        """Set debug mode."""
        self.debug = mode

    def repr_config(self) -> str:
        """Return app config string representation."""
        rep = "AppConfig(" + self.name + "," + str(self.host) + "," + str(self.port) + ")"
        return rep
