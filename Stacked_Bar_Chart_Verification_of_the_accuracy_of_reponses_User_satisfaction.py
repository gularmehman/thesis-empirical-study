import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('PEmpirical4.csv')
data['User satisfaction'] = pd.Categorical(data['User satisfaction'], categories=[1, 2, 3, 4, 5], ordered=True)
category_labels_satisfaction = {1: 'Very Dissatisfied', 2: 'Somewhat Dissatisfied', 3: 'Neutral', 4: 'Somewhat Satisfied', 5: 'Very Satisfied'}
data['User satisfaction'] = data['User satisfaction'].map(category_labels_satisfaction)


pivot_data = data.pivot_table(index='User satisfaction', columns='Perspective taking', aggfunc='size', fill_value=0)
pivot_data.plot(kind='bar', stacked=True, figsize=(10, 6), color=['salmon', 'steelblue', 'skyblue'])
plt.title('Stacked Bar Chart of Perspective taking by User satisfaction', fontsize=20)
plt.xlabel('User satisfaction', fontsize=20)
plt.ylabel('Count of Responses', fontsize=20)
plt.xticks(rotation=0)  # Adjust rotation as needed
plt.legend(title='Perspective taking', labels=['Reserved Perspectives', 'Moderate Perspectives', 'Open Perspectives'], fontsize=20)
plt.savefig('Stacked_Bar_Chart_Verification_of_the_accuracy_of_reponses_User_satisfaction.png', dpi=300, bbox_inches='tight')
plt.show()
