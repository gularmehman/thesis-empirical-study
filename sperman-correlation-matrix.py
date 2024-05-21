import pandas as pd
import numpy as np
from scipy.stats import spearmanr

def spearman_corr_matrix(df):
    columns = df.columns.tolist()
    corr_matrix = pd.DataFrame(index=columns, columns=columns)

    for col1 in columns:
        for col2 in columns:
            corr, _ = spearmanr(df[col1], df[col2])
            corr_matrix.loc[col1, col2] = corr

    return corr_matrix

correlation_matrix = spearman_corr_matrix(data)
print(correlation_matrix)
