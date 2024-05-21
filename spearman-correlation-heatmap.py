import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv('PEmpirical4.csv')
numeric_data = data.select_dtypes(include=[np.number])
spearman_corr = numeric_data.corr(method='spearman')
mask = np.triu(np.ones_like(spearman_corr, dtype=bool), k=1)
plt.figure(figsize=(10, 8))
def custom_fmt(x):
    if x == 0:
        return '0'
    # Format the number to two decimal places
    formatted = "{:.2f}".format(x)
    # Remove the leading zero for positive numbers, handle negative numbers separately
    return formatted.lstrip('0').replace('-0', '-') if '0' in formatted else formatted
sns.heatmap(spearman_corr, mask=mask, annot=True, cmap='coolwarm', fmt="",
            annot_kws={'size': 10, 'ha': 'center', 'va': 'center'},
            square=True, linewidths=.5)
for text in plt.gca().texts:
    text.set_text(custom_fmt(float(text.get_text())))
plt.title('Spearman Correlation Matrix', fontsize=20)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.savefig('spearman_correlation_matrix.png', dpi=300, bbox_inches='tight')  # Save the plot
plt.show()
