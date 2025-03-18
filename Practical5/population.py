# Import the `matplotlib.pyplot` library and name it `plt`
import matplotlib.pyplot as plt
# Store the population data of countries in the UK
uk_countries = [57.11, 3.13, 1.91, 5.45]
# Store the population data of provinces bordering Zhejiang
zhejiang_neighbors = [65.77, 41.88, 45.28, 61.27, 85.15]
# Sort uk_countries from smallest to largest
sorted_uk_countries = sorted(uk_countries)
# Sort zhejiang_neighbors from smallest to largest
sorted_zhejiang_neighbors = sorted(zhejiang_neighbors)
# Output sorted data
print("After the population of the UK: ", sorted_uk_countries)
print("After the population of provinces bordering Zhejiang: ", sorted_zhejiang_neighbors)
# Construct and display the pie chart of the population distribution in countries of the UK
# Create a list `labels_uk` and assign it the value
labels_uk = ['England', 'Wales', 'Northern Ireland', 'Scotland']
# Create a figure, where the graph is 8 inches wide and 8 inches high
plt.figure(figsize=(8, 8))
# Draw a pie chart, with data from `uk_countries`, labels from `labels_uk`, display the percentage with one decimal place, and the starting angle of 140 degree
plt.pie(uk_countries, labels=labels_uk, autopct='%1.1f%%', startangle=140)
# Set the figure title, with a font size of 16
plt.title("Population distribution of the United Kingdom by country", fontsize=16)
# Show the figure
plt.show()

# Construct and display the pie chart of the population distribution in provinces bordering Zhejiang
# Create a list `labels_zhejiang` and assign it the value
labels_zhejiang = ['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu']
# Create a figure, where the graph is 8 inches wide and 8 inches high
plt.figure(figsize=(8, 8))
# Draw a pie chart, with data from `zhejiang_neighbors`, labels from `labels_zhejiang`, display the percentage with one decimal place, and the starting angle of 140 degrees
plt.pie(zhejiang_neighbors, labels=labels_zhejiang, autopct='%1.1f%%', startangle=140)
# Set the figure title as "Population Distribution in Provinces Bordering Zhejiang", with a font size of 16
plt.title("Population Distribution in Provinces Bordering Zhejiang", fontsize=16)
# Show the figure
plt.show()