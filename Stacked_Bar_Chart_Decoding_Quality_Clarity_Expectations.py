import pandas as pd
import matplotlib.pyplot as plt


data['Decoding quality '] = pd.Categorical(data['Decoding quality '], categories=[1, 2, 3], ordered=True)
data['Clarity of expectations'] = pd.Categorical(
    data['Clarity of expectations'],
    categories=[1, 2, 3],
    ordered=True
)
category_labels = {1: 'Low', 2: 'Moderate', 3: 'High'}
data['Clarity of expectations'] = data['Clarity of expectations'].map(category_labels)

pivot_data = data.pivot_table(index='Clarity of expectations', columns='Decoding quality ', aggfunc='size', fill_value=0)
pivot_data.plot(kind='bar', stacked=True, figsize=(10, 6), color=['salmon', 'steelblue', 'skyblue'])
plt.title('Stacked Bar Chart of Decoding Quality by Clarity of Expectations', fontsize=20)
plt.xlabel('Clarity of Expectations', fontsize=20)
plt.ylabel('Count of Responses', fontsize=20)
plt.xticks(rotation=0)  # Adjust rotation as needed
plt.legend(title='Decoding Quality ', labels=['Low', 'Moderate', 'High'], fontsize=20)
plt.savefig('Stacked_Bar_Chart_Decoding_Quality_Clarity_Expectations.png', dpi=300, bbox_inches='tight')
plt.show()
