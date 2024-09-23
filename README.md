# Student Manager
#### Video Demo:  <https://youtu.be/-aiwMsD5x3E>

## Description:

Student Manager is a terminal menu for managing students' names and grades stored into a .csv file. 

The software was designed to be simple to operate, this way the user can add, edit and remove students and their grades by navigating with the keyboard.

For those features to work properly, the code’s logic consists of two important parts: the class “Grades” and the function “main” with its support functions.

## Usage
Users must enter numbers according to the tables shown to navigate through the interface, and type the desired names and grades in order to enter data.

Student Manager has error checking for each input asked, which makes sure only valid data is stored. 

## class Grades
### Description:
As a way to apply the desired functionalities, making use of OOP was the best choice for the project. That’s because the class “Grades” holds methods for everything related to reading and writing information from the “students.csv” file. 

### Methods:
A get method reads the “students.csv” file and returns a dictionary when called, and a write method writes the class attribute “self.students” to the same file, without the need of arguments.

Three action methods, “add_student”, “remove_student” and “edit_student” are responsible for editing the dictionary returned by the get method and updating “self.students” before calling the write method. 

The table methods, “main_table” and “student_table” clear the terminal and return a formatted string that is later printed on screen. This way, only the “Grades” class deals with File IO and editing the data, making it easier to apply it on “main”.

## def main()
### Description:
Main is a function responsible for the project’s interface logic, including printing the tables and deciding what path to lead for each input given by the user.

### Design:
Despite having a reasonable complexity, the main function is designed to be simple enough to read, delegating harder to read lines of code to other sections of the project.

Usage of get functions outside of “main” when asking for inputs was a key choice in maintaining the “main” function organized and more readable.

### Logic:
A “while True” statement ensures the interface is always running and, for each loop, the code clears the terminal, prints the menu with the “main_menu” method and asks for a digit input with the “get_menu” function in order to continue to any of four possible paths in the terminal. 

Those paths are controlled by applying the “match” statement, where “case 1” and “case 2” lead to adding and removing a student from the students database, “case 3” leads to a chosen student’s detailed information table and ”case 4” closes the terminal.

A student’s detailed table is shown when required with a “while True” statement, similar to the main table, that sits inside “case 3”.

The next user’s input matches with an action to edit one of the student’s grades or go back to the main table using “break”, which loops everything once more.

## Conclusion
Ultimately, coding the Student Manager was a great way to learn from new challenges. Having to organize a program larger than I was used to and dealing more extensively with OOP and File IO certainly brought me knowledge that will be used in future projects. Yet, most importantly it was a fun experience to face those challenges and discover solutions throughout the complete duration of CS50P.