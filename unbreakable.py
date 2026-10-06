def get_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                print("Age cannot be negative.")
            else:
                return age
        except ValueError:
            print("Please enter a whole number.")


age = get_age()
print(f"Your age is {age}.")
