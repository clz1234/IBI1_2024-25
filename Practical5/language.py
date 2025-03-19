# create an dictionary. key is "language", value is "users"
language_users = { "JavaScript": 62.3,
                   "HTML": 52.9,
                   "Python":51,
                   "SQL": 51,
                   "TypeScript": 38.5 }
# print this dictionary. 
print(language_users)
# import the matplotlib.pyplot module and rename it plt
import matplotlib.pyplot as plt
import numpy as np
# create a new graphics window. The graph is 8 inches wide and 8 inches high
plt.figure(figsize = (8,8))
# create a bar chart with the key as x axis, the value as y axis, and the column width 0.6
plt.bar(language_users.keys(), language_users.values(), width = 0.6)
# sets the title of the graphic, font size of 18 for the title.
plt.title("Programming languages among developers worldwide as of 2024", fontsize = 18)
# set the Y-axis label, font size of 14 for the Y-axis label.
plt.ylabel("Usage Percentage ", fontsize = 14)
# set the X-axis label, font size of 14 for the X-axis label.
plt.xlabel("Programming Languages", fontsize = 14)
# set the scale of the Y-axis
plt.yticks(np.arange(0 , 81 , 10))
# for each key-value pair in language_users, add a text annotation at the coordinates (key, value)
for key, value in language_users.items():
    # annotate the content as the result of converting value to a string
    plt.text(key,value, str(value))
# show the bar chart
plt.show()

# user input programming language
input_language = input("input the programming language")
# check that the language you entered is in the dictionary
if input_language in language_users:
#if in output "The	percentage of input_language is {language_users[input_language]}% ."
    print(f"The percentage of {input_language}is {language_users[input_language]}%")
# If not output "input_language is not in dictionary"
else:
    print(f"{input_language} is not in the dictionary")