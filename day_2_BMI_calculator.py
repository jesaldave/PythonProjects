# 1st input: enter height in meters e.g: 1.65
height = input("please enter your height in metres :\t")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("pleases enter your weight (in kg) :\t")


weight_as_int = int(weight)
height_as_float = float(height)

# formula: 
bmi = weight_as_int/(height_as_float**2)
print(int(bmi))