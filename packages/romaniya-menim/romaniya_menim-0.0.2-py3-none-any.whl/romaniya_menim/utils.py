import pandas as pd
import os

def read_data():
    print(os.getcwd())    
    df_train = pd.read_csv('/home/javidan/Codes/UCRArchive_2018/ArrowHead/ArrowHead_TRAIN.tsv', sep='\t', header=None)
    return df_train

