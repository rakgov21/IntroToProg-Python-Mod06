# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   Rakshit Govil,11/13/2024,Created Script
#   Rakshit Govil, 11/13/2024, Created several functions
#   Rakshit Govil, 11/13/2024, Added Classes
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
menu_choice: str  # Hold the choice made by the user.
students: list = []  # a table of student data


class FileProcessor:
    """
    A class responsible for file reading and writing operations for student data.
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        Reads student data from a file and updates the provided list of student data.

        Args:
            file_name (str): The name of the file to read the data from.
            student_data (list): The list to store the loaded student data.

        Returns:
            list: The list of student data loaded from the file.
        """
        try:
            with open(file_name, "r") as file:
                student_data = json.load(file)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        Writes the student data to a file in JSON format and outputs the names of registered students.

        Args:
            file_name (str): The name of the file to write the data to.
            student_data (list): The list of student data to write to the file.
        """
        try:
            with open(file_name, "w") as file:
                json.dump(student_data, file, indent=4)
            IO.output_student_courses(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message, error=e)


class IO:
    """
    A class that handles all input and output operations such as displaying menus,
    reading user input, and outputting error messages and student information.
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Displays an error message to the user along with optional technical details.

        Args:
            message (str): The error message to display.
            error (Exception, optional): The exception object for additional technical details.
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        Displays the menu to the user.

        Args:
            menu (str): The menu string to display.
        """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """
        Prompts the user to input a menu choice and validates the input.

        Returns:
            str: The menu choice entered by the user.
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """
        Outputs the names of students and the courses they are enrolled in.

        Args:
            student_data (list): The list of student data to output.
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        Prompts the user for student information, validates the data, and adds it to the student list.

        Args:
            student_data (list): The list where the student data will be stored.

        Returns:
            list: The updated list of student data after the new student is added.
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

while True:

    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        students = IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2":
        IO.output_student_courses(students)
        continue

    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":
        break
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
