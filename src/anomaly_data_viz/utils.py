"""Tools for data handling."""
import base64
import io

import pandas as pd


def upload_file(contents: str, filename: str) -> pd.DataFrame:
    """Upload file from user input."""
    if contents not in "" and filename not in "" and "csv" in filename:
        content_type, content_string = contents.split(",")
        print("content type:", content_type)
        decoded = base64.b64decode(content_string)
        return pd.read_csv(io.StringIO(decoded.decode("utf-8")))

    return pd.DataFrame()
