
name = input("Enter your name: ")

math = int(input("Enter the math marks: "))
python = int(input("Enter the python marks: "))
english = int(input("Enter the english marks: "))

# Marks validation
if (math < 0 or math > 100 or
    python < 0 or python > 100 or
    english < 0 or english > 100):

    print("Invalid marks! Marks must be between 0 and 100.")

else:
    # Calculate total and percentage
    total_marks = math + python + english
    percentage = (total_marks / 300) * 100

    # Check result
    if math >= 33 and python >= 33 and english >= 33:
        result = "PASS"
    else:
        result = "FAIL"

    # Display result
    print("\n----- STUDENT RESULT -----")
    print("Name:", name)
    print("Math marks:", math)
    print("Python marks:", python)
    print("English marks:", english)
    print("Total marks:", total_marks)
    print(f"Percentage: {percentage:.2f}%")
    print("Result:", result)