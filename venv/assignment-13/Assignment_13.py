# Question 1: Visualization of Occupations
# Write a Python program to read the Excel file and display a pie chart showing the percentage
# of occupations in Desa
# Cibodas.
# Assessment Criteria:
# - Read data from Excel
# - Group data by 'Profesi'
# - Display pie chart with labels and percentages

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('./images/Data_Penduduk_EN.xlsx')
occupation_counts = df['Profesi'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(occupation_counts, labels=occupation_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Percentage of Occupations in Desa Cibodas')
plt.axis('equal')
plt.savefig('occupation_pie_chart.png')
print("Pie chart saved as occupation_pie_chart.png")


# Question 2: Education and Gender Comparison
# Write a Python program to display a bar chart comparing the number of citizens based on
# education level and gender.
# Assessment Criteria:
# - Read data from Excel
# - Group by 'Pendidikan_Terakhir' and 'Jenis_Kelamin'
# - Display a grouped bar chart with axis labels and a title

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('./images/Data_Penduduk_EN.xlsx')

edu_gender_counts = df.groupby(['last education', 'sex']).size().unstack(fill_value=0)

edu_gender_counts.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Education Level')
plt.ylabel('Number of Citizens')
plt.title('Number of Citizens by Education Level and Gender')
plt.legend(title='Gender')
plt.tight_layout()
plt.savefig('education_gender_bar_chart.png')
print("Bar chart saved as education_gender_bar_chart.png")


# Question 3: Income Distribution
# Write a Python program to categorize citizen income into 4 groups: Very Low, Low, Middle,
# and High. Display the result
# as a pie chart.
# Assessment Criteria:
# - Read data from Excel
# - Categorize income according to criteria
# - Display a pie chart with category labels and percentages
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('./images/Data_Penduduk_EN.xlsx')

bins = [0, 1000000, 3000000, 7000000, float('inf')]
labels = ['Very Low', 'Low', 'Middle', 'High']

df['Income Category'] = pd.cut(df['Monthly Income'], bins=bins, labels=labels, right=True)

income_counts = df['Income Category'].value_counts().sort_index()

plt.figure(figsize=(8, 8))
plt.pie(income_counts, labels=income_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Income Distribution of Citizens')
plt.axis('equal')
plt.savefig('income_distribution_pie_chart.png')
print("Pie chart saved as income_distribution_pie_chart.png")