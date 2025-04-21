#define a function drug_dosage_calculator, includes two parameters, weight and strength
#check that the weight and strength are within the specified ranges
#use ValueError to output error
#calculate the recommended dose of the drug by multiplying your body weight by 15.
#the volume is calculated based on the different strengths
#input the weight and strength as an example to call my code
#check the function, if it work, print the result, else print the error information

def drug_dosage_calculator(weight, strength):
    #convert a string to a floating point number
    weight = float(weight)
    #check the weight and strength
    if not 10 <= weight <= 100:
        raise ValueError("the weigth must between 10 and 100")
    if strength not in ["120mg/5ml", "250mg/5ml"]:
        raise ValueError("the strength must be 120mg/5ml or 250mg/5ml")
    #calculate the recommended dose with different strength
    recommended_dose = 15 * weight
    if strength == "120mg/5ml":
        volume = recommended_dose / 120 * 5
    else:
        volume = recommended_dose / 250 * 5
    #stop the function
    return volume
#input the weigth and strength
weight ="66"
strength ="120mg/5ml"
#check the function, if it work, print the result, else print the error
result = drug_dosage_calculator(weight, strength)
if result is not None:
    print(f"The drug required is {result} ml.")