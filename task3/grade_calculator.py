# Grade Calculator Program

# Take marks input
marks = input("Enter your marks (0 to 100): ")

# Check if input is numeric
if marks.isdigit():
    marks = int(marks)

    # Check valid range
    if marks >= 0 and marks <= 100:

        # Nested conditions for grade
        if marks >= 90:
            grade = "A+"
            message = "Excellent!"
        elif marks >= 75 and marks < 90:
            grade = "A"
            message = "Very Good!"
        elif marks >= 60 and marks < 75:
            grade = "B"
            message = "Good!"
        elif marks >= 40 and marks < 60:
            grade = "C"
            message = "Pass"
        else:
            grade = "F"
            message = "Fail"

        # Display result
        print("\nYour Marks:", marks)
        print("Your Grade:", grade)
        print("Message:", message)

    else:
        print("Marks must be between 0 and 100.")

else:
    print("Invalid input! Please enter numbers only.")