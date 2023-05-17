import pandas as pd
import os


def write_to_excel(records, path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    df = pd.DataFrame(records)
    df.to_excel(path, index=False)
