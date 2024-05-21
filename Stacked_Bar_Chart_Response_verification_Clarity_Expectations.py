import pandas as pd
import matplotlib.pyplot as plt

# Load your data - replace this with your actual data loading line
data = pd.read_csv('PEmpirical4.csv')

data['Clarity of expectations'] = pd.Categorical(
    data['Clarity of expectations'],
    categories=[1, 2, 3],
    ordered=True
)
category_labels = {1: 'Low', 2: 'Moderate', 3: 'High'}
data['Clarity of expectations'] = data['Clarity of expectations'].map(category_labels)

pivot_data = data.pivot_table(index='Clarity of expectations', columns='Response verification', aggfunc='size', fill_value=0)

# Plot a stacked bar chart
pivot_data.plot(kind='bar', stacked=True, figsize=(10, 6), color=['steelblue', 'salmon', 'skyblue'])
plt.title('Stacked Bar Chart of Response verification by Clarity of Expectations')
plt.xlabel('Clarity of Expectations')
plt.ylabel('Count of Responses')
plt.xticks(rotation=0)  # Adjust rotation as needed
plt.legend(title='Response verification', labels=['Checks', 'Does not check'])

plt.savefig('Stacked_Bar_Chart_Response_verification_Clarity_Expectations.png', dpi=300, bbox_inches='tight')
plt.show()
