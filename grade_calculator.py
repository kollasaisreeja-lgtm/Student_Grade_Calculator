def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent! Keep it up!"
    elif marks >= 80:
        return "B", "Very Good! Keep it up!"
    elif marks >= 70:
        return "C", "Good effort! Keep improving!"
    elif marks >= 60:
        return "D", "You can do better!"
    else:
        return "F", "Don't give up! Keep practicing!"


def main():
    name = input("Enter student name: ")

    while True:
        try:
            marks = int(input("Enter marks (0-100): "))

            if 0 <= marks <= 100:
                break
            else:
                print("Invalid marks! Enter a number from 0 to 100.")

        except ValueError:
            print("Invalid input! Please enter whole-number marks.")

    grade, message = calculate_grade(marks)

    print("\nRESULT FOR", name.upper() + ":")
    print("Marks:", str(marks) + "/100")
    print("Grade:", grade)
    print("Message:", message)


if __name__ == "__main__":
    main()