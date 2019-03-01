# my code to calculate obesity, body mass of a person
# Kevin & Shirley's body mass calculation
# to calculate body mass of individuals at ho.r
# body mass is a person's weight (in kilograms) 
# over a person's height squared in meters or centimeters

name = "Kevin"
height_meters= 3.5 
weight_kg = 160

name2 = "Shirley"
height_meters2= 2.5 
weight_kg2 = 55

# here I define my parameters to included in my calculation 
def bmcalculator(name,height_meters,weight_kg):
    
# here is the body mass formula
    bmindex = weight_kg/(height_meters**2)
  
 # here I state that both parties body mass should be less than 10
    if bmindex < 10:
        return name + " is overweight"
    else:
        return name + " is underweight"

result = bmcalculator(name,height_meters, weight_kg)
result2 =bmcalculator(name2,height_meters2, weight_kg2)

print(result)
print(result2)