import pandas as pd
import numpy as np



data = data.apply(pd.to_numeric, errors='coerce')
def calculate_pi(column1, column2):
    denominator = column1 + column2
    pi_values = column1 / (denominator + 0.0001)  # Avoid division by zero
    return pi_values.mean()

pi_matrix = pd.DataFrame(index=data.columns, columns=data.columns, dtype=float)
for col1 in data.columns:
    for col2 in data.columns:
        if col1 != col2:
            pi_matrix.loc[col1, col2] = calculate_pi(data[col1], data[col2])
        else:
            pi_matrix.loc[col1, col2] = np.nan  # Optionally set diagonal to NaN

print(pi_matrix)
pi_matrix.to_csv('pi_value_matrix.csv')
