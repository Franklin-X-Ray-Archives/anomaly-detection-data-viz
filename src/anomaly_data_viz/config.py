
import sys
from enum import Enum
from typing import Protocol, cast




class AppConfig(Protocol):
    debug: bool
    host: str = "0.0.0.0"
    port: int = 5000
    repository: str = "https://github.com/Franklin-X-Ray-Archives/anomaly-detection-data-viz"
    sleep: float 
