import pandas as pd
import os
from importlib import resources

def read_data_2() -> pd.DataFrame:
    with resources.path("romaniya_menim.data", "ArrowHead_TRAIN.tsv") as df:
        return pd.read_csv(df, sep='\t', header=None)



def read_data():
    print(os.getcwd())    
    df_train = pd.read_csv('/home/javidan/Codes/UCRArchive_2018/ArrowHead/ArrowHead_TRAIN.tsv', sep='\t', header=None)
    return df_train

