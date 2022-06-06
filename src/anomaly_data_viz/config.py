"""Configuration for app"""
from typing import Protocol


class AppConfig(Protocol):
    """Class for app configuration"""

    name: str = "anomaly-data-viz"
    debug: bool
    host: str = "0.0.0.0"
    port: int = 5000
    repository: str = (
        "https://github.com/Franklin-X-Ray-Archives/anomaly-detection-data-viz"
    )
    sleep: float

    def set_debug_mode(self, mode: bool) -> None:
        """Set debug mode"""
        self.debug = mode

    def __repr__(self) -> str:
        """Return app config string representation"""
        rep = "AppConfig(" + self.name + "," + str(self.host) + str(self.port) + ")"
        return rep
