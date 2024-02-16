import random
VACCINES = ["Moderna", "Pfizer","Sputnik", "Covaxcin","AstraZeneca"]

random.shuffle(VACCINES)
print(VACCINES)

LUCKY = random.choice(VACCINES)
print(LUCKY)

for vac in VACCINES:
    print(f"*******TESTING VACCINE {vac}")
    if vac == LUCKY:
        print("##################################")
        print(f"{LUCKY} Vaccine, Test Successful..")
        print("##################################")
        print()
        break

    print("xxxxxxxxxxxxxxxxx")
    print("Test Failed")
    print("xxxxxxxxxxxxxxxxx")
    print()

