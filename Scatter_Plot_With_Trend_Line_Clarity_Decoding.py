import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load your data - replace this with your actual data loading line
data = pd.read_csv('PEmpirical4.csv')
# Ensure the data types are correct for plotting
data['Clarity of expectations'] = pd.to_numeric(data['Clarity of expectations'], errors='coerce')
data['Decoding quality '] = pd.to_numeric(data['Decoding quality '], errors='coerce')

# Drop rows where any of the two columns is NaN to ensure the regression works
data.dropna(subset=['Clarity of expectations', 'Decoding quality '], inplace=True)

# Create a scatter plot with a regression line
plt.figure(figsize=(10, 6))
sns.regplot(x='Clarity of expectations', y='Decoding quality ', data=data, scatter_kws={'alpha':0.5})

# Set the plot title and labels
plt.title('Scatter Plot with Trend Line: Clarity of Expectations vs. Decoding Quality', fontsize=20)
plt.xlabel('Clarity of Expectations', fontsize=20)
plt.ylabel('Decoding Quality', fontsize=20)

# Save the plot
plt.savefig('Scatter_Plot_With_Trend_Line_Clarity_Decoding.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
