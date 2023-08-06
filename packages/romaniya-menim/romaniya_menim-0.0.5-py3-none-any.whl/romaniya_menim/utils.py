import pandas as pd
import os
from importlib import resources

def read_data_2(dataset_name) -> pd.DataFrame:
    with resources.path("romaniya_menim.data", dataset_name + "_TRAIN.tsv") as df:
        return pd.read_csv(df, sep='\t', header=None)


