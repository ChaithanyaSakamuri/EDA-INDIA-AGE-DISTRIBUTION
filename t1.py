import pandas as pd
import matplotlib.pyplot as plt
# Load and filter data
data_path = "t1.csv"  
df = pd.read_csv(data_path, skiprows=4)
india_data = df[df['Country Name'] == 'India']
latest_year = india_data.columns[-2]  
total_population = india_data[latest_year].values[0]
# Age group % and population (in millions)
age_group_percentages = {    '0 to 20 Years': 36.1,
    '21 to 64 Years': 57.0,
    '65+ Years': 6.9
}
age_groups = list(age_group_percentages.keys())
populations_mn = [round((percent / 100) * total_population / 1e6, 2) for percent in age_group_percentages.values()]
colors = ['#4BC0C0', '#FF9F40', '#66BB6A']
# Plot bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(age_groups, populations_mn, color=colors, edgecolor='black')
# Add labels
for bar, percent in zip(bars, age_group_percentages.values()):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 25, 
             f'{yval:.2f} Mn\n({percent}%)',
             ha='center', va='bottom', fontsize=12)
plt.ylim(0, max(populations_mn) + 100)
# Titles and labels
plt.title(f"India's Population Distribution by Age in {latest_year}", fontsize=16, fontweight='bold')
plt.ylabel('Estimated Population (in millions)', fontsize=12)
plt.xlabel('Age Groups', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
