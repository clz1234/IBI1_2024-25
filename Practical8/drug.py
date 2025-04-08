#define a function drug_dosage_calculator, includes two parameters, weight and strength
#check that the weight and strength are within the specified ranges
#calculate the recommended dose of the drug by multiplying your body weight by 15.
#the volume is calculated based on the different strengths
#input the weight and strength
#check the function, if it work, print the result, else print the error information

#define the function
def drug_dosage_calculator(weight, strength):
    #convert a string to a floating point number
    weight = float(weight)
    #check the weight and strength
    if not 10 <= weight <= 100:
        raise ValueError
    if strength not in ["120 mg/5 ml", "250 mg/5 ml"]:
        raise ValueError
    #calculate the recommended dose with different strength
    recommended_dose = 15 * weight
    if strength == "120 mg/5 ml":
        volume = recommended_dose / 120 * 5
    else:
        volume = recommended_dose / 250 * 5
    #stop the function
    return volume
#input the weigth and strength
weight = input("the patient's weight")
strength = input("the strength of the drug(120mg/5ml or 250mg/5ml)")
#check the function, if it work, print the result, else print the error
try:
    result = drug_dosage_calculator(weight, strength)
    print(f"the drug required is {result}ml")
except ValueError as e:
    print(f"error: {e}")