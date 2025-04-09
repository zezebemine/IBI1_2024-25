
#define a fuction to calculate the paracetamol dosage
def drug_dosage_calculator(weight,strength):
    
    #check whether weight is in the range of 10kg to 100kg
    if weight<10 or weight>100:
        return("Wrong! Weight shoud be between 10kg and 100kg")
    
    #check whether paracetamol strength is either 120mg/5ml or 250mg/5ml or not
    paracetamol_strength=[120/5,250/5]
    if strength not in paracetamol_strength:
        return("Wrong! Strength shoud be either 120mg/5ml or 250mg/5ml")
    
    #the formula to calculate the volume
    recommended_dose=15
    required_dose=weight*recommended_dose
    volume=required_dose/strength

    return(f"The required volume is {volume} ml")

#example of function calls
test_weight=67
test_strength=120/5

test_result=drug_dosage_calculator(test_weight,test_strength)
print(test_result)

#enter other else weught and strength to calculate dosage
weight=float(input("Please enter child weight in kg:"))
strength=float(eval(input("Please enter paracetamol strength (120mg/5ml or 250mg/5ml):")))

result=drug_dosage_calculator(weight,strength)
print(result)