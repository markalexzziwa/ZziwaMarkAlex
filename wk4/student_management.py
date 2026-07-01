"""
Student Record Management System
A menu-driven application that manages student records using CSV and JSON storage
with comprehensive error handling and logging.
"""

import csv
import json
import os
import logging
from datetime import datetime
import re

# Configure logging
logging.basicConfig(
    filename='student_system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Custom Exception Classes
class StudentNotFoundError(Exception):
    """Raised when a student is not found in the system."""
    pass

class InvalidStudentDataError(Exception):
    """Raised when student data is invalid."""
    pass

class DuplicateStudentError(Exception):
    """Raised when trying to add a student that already exists."""
    pass


class StudentManagementSystem:
    """Main class for managing student records."""
    
    def __init__(self, csv_file='students.csv', json_file='students_details.json'):
        """
        Initialize the Student Management System.
        
        Args:
            csv_file (str): Path to CSV file for basic student records
            json_file (str): Path to JSON file for additional student details
        """
        self.csv_file = csv_file
        self.json_file = json_file
        self.initialize_files()
        logging.info("Student Management System initialized")
    
    def initialize_files(self):
        """
        Initialize CSV and JSON files if they don't exist.
        Creates empty files with proper headers.
        """
        try:
            # Initialize CSV file
            if not os.path.exists(self.csv_file):
                with open(self.csv_file, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(['Registration_Number', 'Name', 'Age', 'Grade', 'Email'])
                logging.info(f"Created CSV file: {self.csv_file}")
            
            # Initialize JSON file
            if not os.path.exists(self.json_file):
                with open(self.json_file, 'w', encoding='utf-8') as file:
                    json.dump({}, file, indent=4)
                logging.info(f"Created JSON file: {self.json_file}")
                
        except Exception as e:
            logging.error(f"Error initializing files: {e}")
            raise
    
    def validate_student_data(self, reg_number, name, age, grade, email, address=None, contact=None, program=None):
        """
        Validate student data before adding or updating.
        
        Args:
            reg_number (str): Registration number
            name (str): Student name
            age (str/int): Student age
            grade (str): Student grade
            email (str): Student email
            address (str, optional): Student address
            contact (str, optional): Student contact number
            program (str, optional): Student program
            
        Raises:
            InvalidStudentDataError: If any validation fails
        """
        # Validate registration number (must be alphanumeric and at least 3 characters)
        if not reg_number or not re.match(r'^[A-Za-z0-9]{3,}$', reg_number):
            raise InvalidStudentDataError("Registration number must be alphanumeric and at least 3 characters long")
        
        # Validate name (only letters, spaces, and hyphens)
        if not name or not re.match(r'^[A-Za-z\s\-]{2,50}$', name):
            raise InvalidStudentDataError("Name must contain only letters, spaces, and hyphens (2-50 characters)")
        
        # Validate age (must be between 1 and 150)
        try:
            age_int = int(age)
            if age_int < 1 or age_int > 150:
                raise InvalidStudentDataError("Age must be between 1 and 150")
        except ValueError:
            raise InvalidStudentDataError("Age must be a valid number")
        
        # Validate grade (must be A, B, C, D, or F)
        valid_grades = ['A', 'B', 'C', 'D', 'F']
        if not grade or grade.upper() not in valid_grades:
            raise InvalidStudentDataError(f"Grade must be one of: {', '.join(valid_grades)}")
        
        # Validate email format
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not email or not re.match(email_pattern, email):
            raise InvalidStudentDataError("Invalid email format")
        
        # Validate contact if provided
        if contact and not re.match(r'^\+?[\d\s\-]{10,15}$', contact):
            raise InvalidStudentDataError("Contact number must be 10-15 digits (can include +, spaces, and hyphens)")
        
        return True
    
    def get_all_students(self):
        """
        Retrieve all students from the CSV file.
        
        Returns:
            list: List of student records
        """
        students = []
        try:
            with open(self.csv_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                students = list(reader)
                logging.info(f"Retrieved {len(students)} students from CSV")
        except Exception as e:
            logging.error(f"Error reading CSV file: {e}")
            raise
        
        # Add additional details from JSON
        try:
            with open(self.json_file, 'r', encoding='utf-8') as file:
                details = json.load(file)
                for student in students:
                    reg_number = student['Registration_Number']
                    if reg_number in details:
                        student.update(details[reg_number])
                    else:
                        # Add empty fields if no details exist
                        student.update({
                            'Address': '',
                            'Contact': '',
                            'Program': ''
                        })
        except Exception as e:
            logging.error(f"Error reading JSON file: {e}")
            raise
        
        return students
    
    def find_student(self, reg_number):
        """
        Find a student by registration number.
        
        Args:
            reg_number (str): Registration number to search for
            
        Returns:
            dict: Student record if found
            
        Raises:
            StudentNotFoundError: If student is not found
        """
        students = self.get_all_students()
        for student in students:
            if student['Registration_Number'].lower() == reg_number.lower():
                logging.info(f"Student found: {reg_number}")
                return student
        
        logging.warning(f"Student not found: {reg_number}")
        raise StudentNotFoundError(f"Student with registration number {reg_number} not found")
    
    def add_student(self, reg_number, name, age, grade, email, address='', contact='', program=''):
        """
        Add a new student to the system.
        
        Args:
            reg_number (str): Registration number
            name (str): Student name
            age (str/int): Student age
            grade (str): Student grade
            email (str): Student email
            address (str): Student address
            contact (str): Student contact
            program (str): Student program
            
        Raises:
            DuplicateStudentError: If student already exists
            InvalidStudentDataError: If data validation fails
        """
        # Validate data
        self.validate_student_data(reg_number, name, age, grade, email, address, contact, program)
        
        try:
            # Check if student already exists
            existing_students = self.get_all_students()
            for student in existing_students:
                if student['Registration_Number'].lower() == reg_number.lower():
                    raise DuplicateStudentError(f"Student with registration number {reg_number} already exists")
            
            # Add to CSV
            with open(self.csv_file, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([reg_number, name, age, grade, email])
            
            # Add details to JSON
            with open(self.json_file, 'r+', encoding='utf-8') as file:
                details = json.load(file)
                details[reg_number] = {
                    'Address': address,
                    'Contact': contact,
                    'Program': program
                }
                file.seek(0)
                json.dump(details, file, indent=4)
                file.truncate()
            
            logging.info(f"Student added successfully: {reg_number}")
            print(f"\n✅ Student {name} (ID: {reg_number}) added successfully!")
            
        except Exception as e:
            logging.error(f"Error adding student {reg_number}: {e}")
            raise
    
    def update_student(self, reg_number, field, new_value):
        """
        Update a student's information.
        
        Args:
            reg_number (str): Registration number of student to update
            field (str): Field to update
            new_value (str): New value for the field
            
        Raises:
            StudentNotFoundError: If student is not found
            InvalidStudentDataError: If data validation fails
        """
        students = self.get_all_students()
        found = False
        updated_students = []
        
        # Find and update the student
        for student in students:
            if student['Registration_Number'].lower() == reg_number.lower():
                found = True
                old_value = student.get(field, '')
                
                # Validate if updating specific fields
                if field == 'Age' or field == 'Name' or field == 'Grade' or field == 'Email':
                    # Create a temporary copy for validation
                    temp_student = student.copy()
                    temp_student[field] = new_value
                    
                    # Validate the updated data
                    self.validate_student_data(
                        temp_student.get('Registration_Number', reg_number),
                        temp_student.get('Name', ''),
                        temp_student.get('Age', ''),
                        temp_student.get('Grade', ''),
                        temp_student.get('Email', ''),
                        temp_student.get('Address', ''),
                        temp_student.get('Contact', ''),
                        temp_student.get('Program', '')
                    )
                
                student[field] = new_value
                logging.info(f"Updated {field} for student {reg_number} from '{old_value}' to '{new_value}'")
                print(f"\n✅ Student {reg_number}'s {field} updated from '{old_value}' to '{new_value}'")
            
            updated_students.append(student)
        
        if not found:
            raise StudentNotFoundError(f"Student with registration number {reg_number} not found")
        
        # Update CSV file
        try:
            with open(self.csv_file, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['Registration_Number', 'Name', 'Age', 'Grade', 'Email'])
                writer.writeheader()
                for student in updated_students:
                    # Only include CSV fields
                    csv_data = {
                        'Registration_Number': student.get('Registration_Number', ''),
                        'Name': student.get('Name', ''),
                        'Age': student.get('Age', ''),
                        'Grade': student.get('Grade', ''),
                        'Email': student.get('Email', '')
                    }
                    writer.writerow(csv_data)
            
            # Update JSON file
            with open(self.json_file, 'w', encoding='utf-8') as file:
                details = {}
                for student in updated_students:
                    reg = student.get('Registration_Number', '')
                    details[reg] = {
                        'Address': student.get('Address', ''),
                        'Contact': student.get('Contact', ''),
                        'Program': student.get('Program', '')
                    }
                json.dump(details, file, indent=4)
                
        except Exception as e:
            logging.error(f"Error updating student {reg_number}: {e}")
            raise
    
    def delete_student(self, reg_number):
        """
        Delete a student from the system.
        
        Args:
            reg_number (str): Registration number of student to delete
            
        Raises:
            StudentNotFoundError: If student is not found
        """
        students = self.get_all_students()
        found = False
        remaining_students = []
        
        for student in students:
            if student['Registration_Number'].lower() == reg_number.lower():
                found = True
                logging.info(f"Deleted student: {reg_number}")
                print(f"\n✅ Student {student.get('Name', '')} (ID: {reg_number}) deleted successfully!")
            else:
                remaining_students.append(student)
        
        if not found:
            raise StudentNotFoundError(f"Student with registration number {reg_number} not found")
        
        # Update CSV file
        try:
            with open(self.csv_file, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['Registration_Number', 'Name', 'Age', 'Grade', 'Email'])
                writer.writeheader()
                for student in remaining_students:
                    csv_data = {
                        'Registration_Number': student.get('Registration_Number', ''),
                        'Name': student.get('Name', ''),
                        'Age': student.get('Age', ''),
                        'Grade': student.get('Grade', ''),
                        'Email': student.get('Email', '')
                    }
                    writer.writerow(csv_data)
            
            # Update JSON file
            with open(self.json_file, 'w', encoding='utf-8') as file:
                details = {}
                for student in remaining_students:
                    reg = student.get('Registration_Number', '')
                    details[reg] = {
                        'Address': student.get('Address', ''),
                        'Contact': student.get('Contact', ''),
                        'Program': student.get('Program', '')
                    }
                json.dump(details, file, indent=4)
                
        except Exception as e:
            logging.error(f"Error deleting student {reg_number}: {e}")
            raise
    
    def display_student(self, student):
        """
        Display a student's information in a formatted way.
        
        Args:
            student (dict): Student record to display
        """
        print("\n" + "="*60)
        print(f"📚 STUDENT RECORD")
        print("="*60)
        print(f"Registration Number: {student.get('Registration_Number', 'N/A')}")
        print(f"Name: {student.get('Name', 'N/A')}")
        print(f"Age: {student.get('Age', 'N/A')}")
        print(f"Grade: {student.get('Grade', 'N/A')}")
        print(f"Email: {student.get('Email', 'N/A')}")
        print(f"Address: {student.get('Address', 'N/A')}")
        print(f"Contact: {student.get('Contact', 'N/A')}")
        print(f"Program: {student.get('Program', 'N/A')}")
        print("="*60)
    
    def display_all_students(self):
        """
        Display all students in a formatted table.
        """
        students = self.get_all_students()
        
        if not students:
            print("\n📭 No students found in the system.")
            return
        
        print("\n" + "="*100)
        print(f"📚 ALL STUDENTS ({len(students)} records)")
        print("="*100)
        print(f"{'Reg Number':<15} {'Name':<25} {'Age':<5} {'Grade':<6} {'Email':<30}")
        print("-"*100)
        
        for student in students:
            print(f"{student.get('Registration_Number', ''):<15} "
                  f"{student.get('Name', ''):<25} "
                  f"{student.get('Age', ''):<5} "
                  f"{student.get('Grade', ''):<6} "
                  f"{student.get('Email', ''):<30}")
        
        print("="*100)


def main():
    """Main menu-driven application."""
    system = StudentManagementSystem()
    
    print("\n" + "="*60)
    print("🎓 STUDENT RECORD MANAGEMENT SYSTEM")
    print("="*60)
    
    while True:
        print("\n📋 MAIN MENU")
        print("-"*40)
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student by Registration Number")
        print("4. Update Student Details")
        print("5. Delete Student Record")
        print("6. Exit")
        print("-"*40)
        
        try:
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                # Add New Student
                print("\n" + "="*50)
                print("➕ ADD NEW STUDENT")
                print("="*50)
                
                try:
                    reg_number = input("Registration Number (alphanumeric, min 3 chars): ").strip()
                    name = input("Full Name: ").strip()
                    age = input("Age: ").strip()
                    grade = input("Grade (A, B, C, D, F): ").strip().upper()
                    email = input("Email: ").strip()
                    address = input("Address (optional): ").strip()
                    contact = input("Contact Number (optional): ").strip()
                    program = input("Program/Department (optional): ").strip()
                    
                    system.add_student(reg_number, name, age, grade, email, address, contact, program)
                    
                except (InvalidStudentDataError, DuplicateStudentError) as e:
                    print(f"\n❌ Error: {e}")
                    logging.warning(f"Add student failed: {e}")
                except Exception as e:
                    print(f"\n❌ An unexpected error occurred: {e}")
                    logging.error(f"Unexpected error in add student: {e}")
                finally:
                    input("\nPress Enter to continue...")
            
            elif choice == '2':
                # View All Students
                try:
                    system.display_all_students()
                except Exception as e:
                    print(f"\n❌ Error displaying students: {e}")
                    logging.error(f"Error in display all students: {e}")
                finally:
                    input("\nPress Enter to continue...")
            
            elif choice == '3':
                # Search Student
                print("\n" + "="*50)
                print("🔍 SEARCH STUDENT")
                print("="*50)
                
                try:
                    reg_number = input("Enter Registration Number to search: ").strip()
                    student = system.find_student(reg_number)
                    system.display_student(student)
                except StudentNotFoundError as e:
                    print(f"\n❌ {e}")
                    logging.warning(f"Search failed: {e}")
                except Exception as e:
                    print(f"\n❌ An unexpected error occurred: {e}")
                    logging.error(f"Unexpected error in search: {e}")
                finally:
                    input("\nPress Enter to continue...")
            
            elif choice == '4':
                # Update Student Details
                print("\n" + "="*50)
                print("✏️ UPDATE STUDENT DETAILS")
                print("="*50)
                
                try:
                    reg_number = input("Enter Registration Number to update: ").strip()
                    
                    # Show current details
                    student = system.find_student(reg_number)
                    system.display_student(student)
                    
                    print("\n📝 Fields that can be updated:")
                    print("1. Name")
                    print("2. Age")
                    print("3. Grade")
                    print("4. Email")
                    print("5. Address")
                    print("6. Contact")
                    print("7. Program")
                    
                    field_choice = input("\nSelect field to update (1-7): ").strip()
                    fields = {
                        '1': 'Name',
                        '2': 'Age',
                        '3': 'Grade',
                        '4': 'Email',
                        '5': 'Address',
                        '6': 'Contact',
                        '7': 'Program'
                    }
                    
                    if field_choice not in fields:
                        print("\n❌ Invalid field selection")
                        input("\nPress Enter to continue...")
                        continue
                    
                    field = fields[field_choice]
                    new_value = input(f"Enter new value for {field}: ").strip()
                    
                    if not new_value:
                        print("\n❌ Value cannot be empty")
                        input("\nPress Enter to continue...")
                        continue
                    
                    system.update_student(reg_number, field, new_value)
                    
                except (StudentNotFoundError, InvalidStudentDataError) as e:
                    print(f"\n❌ Error: {e}")
                    logging.warning(f"Update student failed: {e}")
                except Exception as e:
                    print(f"\n❌ An unexpected error occurred: {e}")
                    logging.error(f"Unexpected error in update: {e}")
                finally:
                    input("\nPress Enter to continue...")
            
            elif choice == '5':
                # Delete Student
                print("\n" + "="*50)
                print("🗑️ DELETE STUDENT RECORD")
                print("="*50)
                
                try:
                    reg_number = input("Enter Registration Number to delete: ").strip()
                    
                    # Confirm deletion
                    student = system.find_student(reg_number)
                    system.display_student(student)
                    
                    confirm = input("\n⚠️ Are you sure you want to delete this student? (y/n): ").strip().lower()
                    if confirm == 'y':
                        system.delete_student(reg_number)
                    else:
                        print("\n❌ Deletion cancelled")
                        
                except StudentNotFoundError as e:
                    print(f"\n❌ {e}")
                    logging.warning(f"Delete failed: {e}")
                except Exception as e:
                    print(f"\n❌ An unexpected error occurred: {e}")
                    logging.error(f"Unexpected error in delete: {e}")
                finally:
                    input("\nPress Enter to continue...")
            
            elif choice == '6':
                # Exit
                print("\n👋 Thank you for using the Student Management System!")
                print("Goodbye!")
                logging.info("System exited successfully")
                break
            
            else:
                print("\n❌ Invalid choice! Please select a number between 1 and 6.")
                logging.warning(f"Invalid menu choice: {choice}")
                
        except KeyboardInterrupt:
            print("\n\n👋 Program interrupted by user. Exiting...")
            logging.info("Program interrupted by user")
            break
        except Exception as e:
            print(f"\n❌ An unexpected error occurred: {e}")
            logging.error(f"Unexpected error in main loop: {e}")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()