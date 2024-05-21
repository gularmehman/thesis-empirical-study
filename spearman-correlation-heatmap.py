import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load your data
data = pd.read_csv('PEmpirical4.csv')

# Select only the numeric columns for correlation
numeric_data = data.select_dtypes(include=[np.number])

# Calculate the Spearman correlation matrix
spearman_corr = numeric_data.corr(method='spearman')

# Create a mask for the upper triangle
mask = np.triu(np.ones_like(spearman_corr, dtype=bool), k=1)

# Set up the matplotlib figure
plt.figure(figsize=(10, 8))

# Define a custom formatting function to remove leading zeros for both positive and negative numbers
def custom_fmt(x):
    if x == 0:
        return '0'
    # Format the number to two decimal places
    formatted = "{:.2f}".format(x)
    # Remove the leading zero for positive numbers, handle negative numbers separately
    return formatted.lstrip('0').replace('-0', '-') if '0' in formatted else formatted

# Draw the heatmap with the mask and custom annotations
sns.heatmap(spearman_corr, mask=mask, annot=True, cmap='coolwarm', fmt="",
            annot_kws={'size': 10, 'ha': 'center', 'va': 'center'},
            square=True, linewidths=.5)

# Apply custom formatting to each text annotation in the heatmap
for text in plt.gca().texts:
    text.set_text(custom_fmt(float(text.get_text())))

# Title and save figure adjustments
plt.title('Spearman Correlation Matrix', fontsize=20)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.savefig('spearman_correlation_matrix.png', dpi=300, bbox_inches='tight')  # Save the plot

# Show plot
plt.show()
