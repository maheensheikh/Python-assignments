def manage_student_database() -> None:
    students: list[tuple[int, str]] = []  # List to store tuples of (ID, name)
    student_names: set[str] = set()  # Set to check for duplicate names
    student_id: int = 1  # Start ID from 1

    # Input loop
    while True:
        name: str = input("Please enter the student's name (or type 'stop' to finish): ").strip()
        
        # Check if the user wants to stop
        if name.lower() == 'stop':
            break
        
        # Check for duplicate names
        if name in student_names:
            print("This name is already in the list.")
        else:
            # Add new student as a tuple (ID, name) to the list
            students.append((student_id, name))
            student_names.add(name)
            student_id += 1

    # Display the complete list of students
    print("\nComplete List of Students (Tuples):")
    print(students)

    # Display each student with their ID and name
    print("\nList of Students with IDs:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}")
    
    # Calculate and display the total number of students
    total_students: int = len(students)
    print(f"\nTotal number of students: {total_students}")

    # Calculate the total length of all student names combined
    total_length_names: int = sum(len(student[1]) for student in students)
    print(f"Total length of all student names combined: {total_length_names}")
    
    # Find the student with the longest and shortest name
    if students:
        longest_name_student: str = max(students, key=lambda student: len(student[1]))[1]
        shortest_name_student: str = min(students, key=lambda student: len(student[1]))[1]
        print(f"The student with the longest name is: {longest_name_student}")
        print(f"The student with the shortest name is: {shortest_name_student}")

# Call the function to run the student database management
manage_student_database()
