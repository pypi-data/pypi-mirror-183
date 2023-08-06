import pandas as pd
import os

def read_data():
    print(os.getcwd())    
    df_train = pd.read_csv('/data/ArrowHead_TRAIN.tsv', sep='\t', header=None)
    return df_train

