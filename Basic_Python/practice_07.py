def age_cateegory(age):
    if age < 18:
        return "a Child"
    elif age < 50:
        return "an Adult"
    else:
        return "a Senior"

age = int(input("Enter your age: "))
print(f"You are {age_cateegory(age)}")