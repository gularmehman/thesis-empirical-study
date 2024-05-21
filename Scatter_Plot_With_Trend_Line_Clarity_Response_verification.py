import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('PEmpirical4.csv')

data['Clarity of expectations'] = pd.to_numeric(data['Clarity of expectations'], errors='coerce')
data['Response verification'] = pd.to_numeric(data['Response verification'], errors='coerce')

data.dropna(subset=['Clarity of expectations', 'Response verification'], inplace=True)

plt.figure(figsize=(10, 6))
sns.regplot(x='Clarity of expectations', y='Response verification', data=data, scatter_kws={'alpha':0.5})

plt.title('Scatter Plot with Trend Line: Clarity of Expectations vs. Response verification')
plt.xlabel('Clarity of Expectations')
plt.ylabel('Response verification')

plt.savefig('Scatter_Plot_With_Trend_Line_Clarity_Response_verification.png', dpi=300, bbox_inches='tight')
plt.show()
