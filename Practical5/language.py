language_users = { "JavaScript": 62.3, "HTML": 52.9, "Python":51, "SQL": 51, "TypeScript": 38.5 }
# Create an dictionary. key is "language", value is "users"
print(language_users)
# Print this dictionary. 
import matplotlib.pyplot as plt
# Import the matplotlib.pyplot module and rename it plt
plt.figure(figsize = (8,8))
# Create a new graphics window. The parameter specifies the size of the graph in inches, where the graph is 8 inches wide and 8 inches high
plt.bar(language_users.keys(), language_users.values(), color = 'red', width = 0.6)
# Create a bar chart with the keyword x axis, the value y axis, the fill color red, and the column width 0.6
plt.title("Programming languages among developers worldwide as of 2024", fontsize = 18)
# Sets the title of the graphic, specifying a font size of 18 for the title.
plt.ylim(0,80)
# Set the display range of the Y-axis
plt.ylabel("Usage Percentage ", fontsize = 14)
# Set the Y-axis label, specifying a font size of 16 for the Y-axis label.
plt.xlabel("Programming Languages", fontsize = 14)
# Set the X-axis label, specifying a font size of 16 for the X-axis label.
plt.yticks([20, 40, 60, 80])
# Set the scale of the Y-axis
plt.show()
# Show the bar chart