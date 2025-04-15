# 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet = "Dog"
age = 4

if pet == "Dog":
    if age < 2:
        food = "Puppy food"
    else:
        food = "Senior dog food"
elif pet == "Cat":
    if age > 5:
        food = "Senior cat food"
    else:
        food = "Kitten food"

print(f"Give a {pet} {food}")