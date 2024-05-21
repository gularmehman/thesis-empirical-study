import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('PEmpirical4.csv')

effectiveness_categories = [1, 2, 3, 4, 5]
category_labels_effectiveness = {
    1: 'Not at all helpful',
    2: 'Slightly helpful',
    3: 'Moderately helpful',
    4: 'Very helpful',
    5: 'Extremely helpful'
}
data['Chat GPT effectiveness'] = pd.Categorical(data['Chat GPT effectiveness'], categories=effectiveness_categories, ordered=True)
data['Chat GPT effectiveness'] = data['Chat GPT effectiveness'].map(category_labels_effectiveness)

satisfaction_categories = [1, 2, 3, 4, 5]  # Presuming these are coded similarly in your data
category_labels_satisfaction = {
    1: 'Very Dissatisfied',
    2: 'Somewhat Dissatisfied',
    3: 'Neutral',
    4: 'Somewhat Satisfied',
    5: 'Very Satisfied'
}
data['User satisfaction'] = pd.Categorical(data['User satisfaction'], categories=satisfaction_categories, ordered=True)
data['User satisfaction'] = data['User satisfaction'].map(category_labels_satisfaction)

pivot_data = data.pivot_table(index='Chat GPT effectiveness', columns='User satisfaction', aggfunc='size', fill_value=0)

colors = ['salmon', 'steelblue', 'skyblue', 'plum', 'cornflowerblue']
pivot_data.plot(kind='bar', stacked=True, figsize=(10, 6), color=colors)
plt.title('Stacked Bar Chart of User Satisfaction by Chat GPT Effectiveness')
plt.xlabel('Chat GPT Effectiveness')
plt.ylabel('Count of Responses')
plt.xticks(rotation=0)
plt.legend(title='User Satisfaction', loc='upper right')
plt.savefig('Stacked_Bar_Chart_User_Satisfaction.png', dpi=300, bbox_inches='tight')
plt.show()
