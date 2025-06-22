student_name = input("Please enter the student's name: ")
student_class = input("Please enter the student's class: ")
mark1 = float(input("Enter marks for Subject 1 (out of 100): "))
mark2 = float(input("Enter marks for Subject 2 (out of 100): "))
mark3 = float(input("Enter marks for Subject 3 (out of 100): "))
mark4 = float(input("Enter marks for Subject 4 (out of 100): "))
mark5 = float(input("Enter marks for Subject 5 (out of 100): "))
total_marks = mark1 + mark2 + mark3 + mark4 + mark5
max_total_marks = 500
percentage = (total_marks / max_total_marks) * 100
print("\n--- Student Report Card ---")
print(f"Name: {student_name}")
print(f"Class: {student_class}")
print(f"Total Marks Obtained: {total_marks:.2f}")
print(f"Percentage: {percentage:.2f}%")
print("---------------------------")




print("Welcome to the String Concatenation and Methods Demo!")



string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")


concatenated_string = string1 + " " + string2


print(f"The first string was: '{string1}'")
print(f"The second string was: '{string2}'")
print(f"The concatenated string is: '{concatenated_string}'")


print("\n--- Demonstrating Common String Methods ---")


print(f"1. Length: {len(concatenated_string)}")


print(f"2. Uppercase: '{concatenated_string.upper()}'")


print(f"3. Lowercase: '{concatenated_string.lower()}'")


print(f"4. Capitalized: '{concatenated_string.capitalize()}'")


print(f"5. Title-cased: '{concatenated_string.title()}'")


print(f"6. Stripped ('  Hi  '): '{'  Hi  '.strip()}'")


print(f"7. Replace (' ' with '-'): '{concatenated_string.replace(' ', '-')}'")


print(f"8. Find ('o'): Index {concatenated_string.find('o')}")


print(f"9. Count ('a'): {concatenated_string.count('a')} occurrence(s)")


print(f"10. Starts with 'Hello'? {concatenated_string.startswith('Hello')}")


print(f"11. Ends with 'World'? {concatenated_string.endswith('World')}")


