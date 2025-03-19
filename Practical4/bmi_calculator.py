#       BMI
#       What is their BMI, and from that, which of the three categories they can be placed into
#             if more than 30: the person is obese
#             if less than 18.5: the preson is underweight
#             if in the intermediate range: the person is in normal weight

# get the user's weight (in kg)
w = float(input("the user's weighet in kg"))
# get the user's height (in meters)
h = float(input("the user's height in meters"))
# calculate the BMI value according to the formula BMI = weight/(height * height)
bmi = w/h**2
# determine the BMI category based on the following criteria:
# if BMI < 18.5, category is "underweight"
if bmi < 18.5:
    category = "underweight"
# if 18.5 <= BMI <= 30, the category is "normal weight"
elif 18.5 <= bmi <= 30:
    category = "normal"
# if BMI >= 30, the category is "obese"
else:
    category = "obese"
# output a sentence containing the user's BMI value and category, converts the number into a string
result = f"BMI is {str(bmi)}，you are  {category}."
print(result)