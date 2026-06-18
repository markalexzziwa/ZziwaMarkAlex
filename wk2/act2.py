'''
Your Tasks
Your job is to extend the functionality of the ContactManager class by 
implementing the following requirements. Ensure you do not break the existing features.

Task 1: Data Validation (20 Points)
Currently, a user can enter any text for a phone number or email. 
Modify the code to add basic validation:

Phone Validation: In add_contact and update_contact, 
ensure the phone number contains only digits and hyphens (e.g., "+256-701"). 
If it contains illegal characters, print an error message and cancel the operation.

Email Validation: Ensure that if an email is provided, it contains an @ symbol and a . (period).


Task 2: Advanced Search (25 Points)
The current Contacts method only filters by name and phone number.

Modify Contactss so that it can also search by email.

Write a helper method or modify the search printout so it displays the search results in a clean, 
user-friendly format rather than just returning a raw Python list of tuples.


Task 3: Interactive CLI Menu (35 Points)
Create an interactive Command Line Interface (CLI) loop inside a function called main(). 
When run, the program should present the user with a recurring menu until they choose to exit.

The menu should look similar to this:

=== Contact Manager Menu ===CRUD
1. Add Contact
2. View Contact
3. Update Contact
4. Delete Contact
5. Search Contacts
6. List All Contacts
7. Exit
Choose an option (1-7):

Implement proper input handling for each menu item, 
prompting the user for necessary arguments (like name, phone, etc.) 
and passing them to your class methods.

Submission Guidelines:
1. Add a single python script to your github link, 
2. Submit a single Python file named name_contact_assignment.py.
'''