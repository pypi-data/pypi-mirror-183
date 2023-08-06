import pandas as pd

def read_data():
    df_train = pd.read_csv('/data/ArrowHead_TRAIN.tsv', sep='\t', header=None)
    return df_train
