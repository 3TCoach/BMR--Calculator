# BMR Calculator Project - Author: Afsheen Golanbar

def bmr_calculator():
    try:
        height = float(input("Enter your height in inches: "))
        weight = float(input("Enter your weight in pounds: "))
        age = int(input("Enter your age: "))
        gender = input("Enter your gender (male/female): ").lower()

        if gender == "male":
            bmr = 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)
        else:
            bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)

        calories = bmr * 1.5
        protein = 0.8 * weight
        carbs = (calories * 0.55) / 4
        fat = (calories * 0.25) / 9
        sugar = 20

        print(f"Daily calories: {calories:.0f}")
        print(f"Protein: {protein:.1f} grams")
        print(f"Carbs: {carbs:.1f} grams")
        print(f"Fat: {fat:.1f} grams")
        print(f"Sugar: {sugar} grams")

    except ValueError:
        print("Invalid input! Please enter numeric values for height, weight, and age.")

if __name__ == "__main__":
    bmr_calculator()
