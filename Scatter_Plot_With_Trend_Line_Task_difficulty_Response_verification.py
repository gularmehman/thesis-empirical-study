import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('PEmpirical4.csv')


data['Task difficulty'] = pd.to_numeric(data['Task difficulty'], errors='coerce')
data['Response verification'] = pd.to_numeric(data['Response verification'], errors='coerce')


data.dropna(subset=['Task difficulty', 'Response verification'], inplace=True)

plt.figure(figsize=(10, 6))
sns.regplot(x='Task difficulty', y='Response verification', data=data, scatter_kws={'alpha':0.5})

plt.title('Scatter Plot with Trend Line: Task difficulty vs. Response verification', fontsize=20)
plt.xlabel('Task difficulty', fontsize=20)
plt.ylabel('Response verification', fontsize=20)

plt.savefig('Scatter_Plot_With_Trend_Line_Task_difficulty_Response_verification.png', dpi=300, bbox_inches='tight')
plt.show()
