import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('PEmpirical4.csv')

data['User satisfaction'] = pd.to_numeric(data['User satisfaction'], errors='coerce')
data['Perspective taking'] = pd.to_numeric(data['Perspective taking'], errors='coerce')

data.dropna(subset=['User satisfaction', 'Perspective taking'], inplace=True)

plt.figure(figsize=(10, 6))
sns.regplot(x='User satisfaction', y='Perspective taking', data=data, scatter_kws={'alpha':0.5})


plt.title('Scatter Plot with Trend Line: User satisfaction vs. Perspective taking', fontsize=20)
plt.xlabel('User satisfaction', fontsize=20)
plt.ylabel('Perspective taking', fontsize=20)

plt.savefig('Scatter_Plot_With_Trend_Line_User_satisfaction_Perspective_taking.png', dpi=300, bbox_inches='tight')
plt.show()
