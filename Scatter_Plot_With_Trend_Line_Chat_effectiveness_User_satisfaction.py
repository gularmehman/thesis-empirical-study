import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('PEmpirical4.csv')
data['Chat GPT effectiveness'] = pd.to_numeric(data['Chat GPT effectiveness'], errors='coerce')
data['User satisfaction'] = pd.to_numeric(data['User satisfaction'], errors='coerce')
data.dropna(subset=['Chat GPT effectiveness', 'User satisfaction'], inplace=True)

plt.figure(figsize=(10, 6))
sns.regplot(x='Chat GPT effectiveness', y='User satisfaction', data=data, scatter_kws={'alpha':0.5})


plt.title('Scatter Plot with Trend Line: Chat GPT effectiveness vs. User satisfaction')
plt.xlabel('Chat GPT effectiveness')
plt.ylabel('User satisfaction')


plt.savefig('Scatter_Plot_With_Trend_Line_Chat_effectiveness_User_satisfaction.png', dpi=300, bbox_inches='tight')
plt.show()
