

import pandas as pd
import numpy as np
import base64
import io


def upload_file(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            return pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        
    except Exception as e:
        print("ERROR:", e)
        return 'There was an error processing this file.'
