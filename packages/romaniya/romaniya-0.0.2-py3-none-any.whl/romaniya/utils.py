import pandas as pd
import os

def read_data():
    df_train = pd.read_csv('/data/ArrowHead_TRAIN.tsv', sep='\t', header=None)
    print(os.getcwd())    
    return df_train

