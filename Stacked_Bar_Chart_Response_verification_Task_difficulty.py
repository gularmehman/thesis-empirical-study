import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('PEmpirical4.csv')

data['Task difficulty'] = pd.Categorical(data['Task difficulty'],
    categories=[1, 2, 3, 4, 5],
    ordered=True
)
category_labels = {1: 'Very easy', 2: 'Moderately easy', 3: 'Neutral', 4:'Moderately difficult', 5:'Very difficult' }
data['Task difficulty'] = data['Task difficulty'].map(category_labels)

pivot_data = data.pivot_table(index='Task difficulty', columns='Response verification', aggfunc='size', fill_value=0)


colors = ['salmon', 'steelblue', 'skyblue', 'plum', 'cornflowerblue']
pivot_data.plot(kind='bar', stacked=True, figsize=(10, 6), color=colors)
plt.title('Stacked Bar Chart of Response verification by Task difficulty', fontsize=20)
plt.xlabel('Task difficulty', fontsize=20)
plt.ylabel('Count of Responses', fontsize=20)
plt.xticks(rotation=0)  # Adjust rotation as needed
plt.legend(title='Response verification', labels=['Does not check', 'Checks'], fontsize=20)
plt.savefig('Stacked_Bar_Chart_Response_verification_Task_difficulty.png', dpi=300, bbox_inches='tight')
plt.show()
