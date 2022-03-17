age = int(input("What is the patients name age?"))

if age < 12:
    weight = float(input("What is the childs weight (KG)"))
    dose = weight * 10
    print(f"the recomended amount is {dose} mgs of paracetamal")

else:
    print("take 2 500mg tablets")







