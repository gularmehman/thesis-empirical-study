import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('PEmpirical4.csv')
data['Clarity of expectations'] = pd.to_numeric(data['Clarity of expectations'], errors='coerce')
data['Decoding quality '] = pd.to_numeric(data['Decoding quality '], errors='coerce')

data.dropna(subset=['Clarity of expectations', 'Decoding quality '], inplace=True)
plt.figure(figsize=(10, 6))
sns.regplot(x='Clarity of expectations', y='Decoding quality ', data=data, scatter_kws={'alpha':0.5})

plt.title('Scatter Plot with Trend Line: Clarity of Expectations vs. Decoding Quality', fontsize=20)
plt.xlabel('Clarity of Expectations', fontsize=20)
plt.ylabel('Decoding Quality', fontsize=20)


plt.savefig('Scatter_Plot_With_Trend_Line_Clarity_Decoding.png', dpi=300, bbox_inches='tight')
plt.show()
